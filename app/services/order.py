from typing import List, Optional, Dict, Any
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete, desc
from sqlalchemy.sql import func

from app.models.order import Order, OrderItem, OrderStatus
from app.models.transaction import TransactionHistory
from app.models.cart import Cart, CartItem
from app.models.address import Address
from app.models.product import Product, ProductVariant
from app.models.shipment import Shipment, ShipmentStatus
from app.schemas.order import OrderCreate, OrderUpdate, OrderItemCreate, OrderItemUpdate, TransactionCreate
from app.services.notification import create_notification
from app.services.shipment import create_shipment_from_order, update_shipment_status


async def create_order(db: AsyncSession, order_in: OrderCreate, user_id: int) -> Order:
    """
    Create a new order with the provided items

    This function verifies that all products in the order have sufficient stock
    before creating the order. Stock is not reduced at this point, only when
    payment is completed.

    Args:
        db: Database session
        order_in: Order data
        user_id: ID of the user creating the order

    Returns:
        Created order

    Raises:
        ValueError: If shipping address is invalid or any product has insufficient stock
    """
    # Check if shipping address exists
    address = await db.get(Address, order_in.shipping_address_id)
    if not address or address.user_id != user_id:
        raise ValueError("Invalid shipping address")

    # Verify stock for all items before creating the order
    for item_data in order_in.items:
        product = await db.get(Product, item_data.product_id)
        if not product:
            raise ValueError(f"Product with ID {item_data.product_id} not found")

        # Check if product has variants
        variant_result = await db.execute(
            select(ProductVariant).where(ProductVariant.product_id == item_data.product_id)
        )
        variants = variant_result.scalars().all()

        if variants:
            total_variant_stock = sum(variant.stock for variant in variants)
            if total_variant_stock < item_data.quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {total_variant_stock}, Requested: {item_data.quantity}")
        else:
            if product.quantity < item_data.quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {product.quantity}, Requested: {item_data.quantity}")

    # Create order record
    order = Order(
        user_id=user_id,
        total_amount=order_in.total_amount,
        status="pending",
        shipping_address_id=order_in.shipping_address_id,
        payment_method="card",
        payment_status="completed",
        # shipping_carrier=order_in.shipping_carrier,
        # tracking_number=order_in.tracking_number,
        # estimated_delivery_date=order_in.estimated_delivery_date
    )
    db.add(order)
    await db.flush()  # To get the order ID

    # Create order items
    total_amount = 0
    for item_data in order_in.items:
        product = await db.get(Product, item_data.product_id)
        if not product:
            raise ValueError(f"Product with ID {item_data.product_id} not found")

        # check variant stock
        variant_result = await db.execute(
            select(ProductVariant).where(ProductVariant.product_id == item_data.product_id)
        )
        variants = variant_result.scalars().all()

        if variants:
            total_variant_stock = sum(variant.stock for variant in variants)
            if total_variant_stock < item_data.quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {total_variant_stock}, Requested: {item_data.quantity}")
        else:
            if product.quantity < item_data.quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {product.quantity}, Requested: {item_data.quantity}")

        # Calculate subtotal for this item
        # subtotal = item_data.unit_price * item_data.quantity
        total_amount += product.price * item_data.quantity

        # Create order item
        order_item = OrderItem(
            order_id=order.id,
            product_id=item_data.product_id,
            quantity=item_data.quantity,
            # unit_price=product.price,
            # subtotal=subtotal
        )
        db.add(order_item)

    # Update total amount (in case it was calculated incorrectly in the request)
    order.total_amount = total_amount
    await db.commit()
    await db.refresh(order)

    # Create notification for order creation
    # await create_notification(
    #     db=db,
    #     user_id=user_id,
    #     notification_type="ORDER_CREATED",
    #     content=f"Your order #{order.id} has been created.",
    #     related_entity_id=order.id
    # )

    return order


async def create_order_from_cart(
    db: AsyncSession, user_id: int, cart_id: int, shipping_address_id: int, payment_method: str
) -> Order:
    """
    Create a new order from the items in a user's cart

    This function verifies that all products in the cart have sufficient stock
    before creating the order. Stock is not reduced at this point, only when
    payment is completed.

    Args:
        db: Database session
        user_id: ID of the user creating the order
        cart_id: ID of the cart to convert to an order
        shipping_address_id: ID of the shipping address to use
        payment_method: Payment method to use

    Returns:
        Created order

    Raises:
        ValueError: If cart is empty, shipping address is invalid, or any product has insufficient stock
    """
    # Get cart items
    cart_items = await get_cart_items(db, cart_id)
    if not cart_items:
        raise ValueError("Cart is empty")

    # Check if shipping address exists
    address = await db.get(Address, shipping_address_id)
    if not address or address.user_id != user_id:
        raise ValueError("Invalid shipping address")

    # Verify stock for all items before creating the order
    for cart_item in cart_items:
        product = await db.get(Product, cart_item.product_id)
        if not product:
            raise ValueError(f"Product with ID {cart_item.product_id} not found")

        # Check if product has variants
        variant_result = await db.execute(
            select(ProductVariant).where(ProductVariant.product_id == cart_item.product_id)
        )
        variants = variant_result.scalars().all()

        if variants:
            total_variant_stock = sum(variant.stock for variant in variants)
            if total_variant_stock < cart_item.quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {total_variant_stock}, Requested: {cart_item.quantity}")
        else:
            if product.quantity < cart_item.quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {product.quantity}, Requested: {cart_item.quantity}")

    # Calculate total
    total_amount = 0.0
    for item in cart_items:
        total_amount += item.quantity * item.unit_price

    # Create order
    db_order = Order(
        user_id=user_id,
        total_amount=total_amount,
        status="pending",
        shipping_address_id=shipping_address_id,
        payment_method=payment_method,
        payment_status="pending"
    )
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)

    # Add order items
    for cart_item in cart_items:
        db_order_item = OrderItem(
            order_id=db_order.id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity,
            unit_price=cart_item.unit_price,
            subtotal=cart_item.quantity * cart_item.unit_price
        )
        db.add(db_order_item)

    await db.commit()

    # Mark cart as abandoned
    await abandon_cart(db, cart_id, user_id)

    # Send notification
    await create_notification(
        db=db,
        user_id=user_id,
        notification_type="order_created",
        content=f"Your order #{db_order.id} has been created and is pending payment.",
        related_entity_id=db_order.id
    )

    return db_order


async def get_order(db: AsyncSession, order_id: int) -> Optional[Order]:
    """
    Get an order by ID
    """
    result = await db.execute(select(Order).where(Order.id == order_id))
    return result.scalars().first()


async def get_user_orders(
    db: AsyncSession,
    user_id: int,
    pagination: Any = None,
    status: str = None
) -> Dict[str, Any]:
    """
    Get all orders for a user with pagination and optional status filtering
    """
    # Build base query
    query = select(Order).where(Order.user_id == user_id)

    # Apply status filter if provided
    if status:
        query = query.where(Order.status == status)

    # Get total count for pagination
    count_query = select(func.count()).select_from(query.subquery())
    total = await db.scalar(count_query) or 0

    # Apply pagination
    if pagination:
        skip = (pagination.page - 1) * pagination.limit
        limit_val = pagination.limit
    else:
        skip = 0
        limit_val = 10

    # Calculate total pages
    total_pages = (total + limit_val - 1) // limit_val if limit_val > 0 else 0

    # Apply pagination to query
    query = query.order_by(desc(Order.order_date)).offset(skip).limit(limit_val)

    # Execute final query
    result = await db.execute(query)
    orders = result.scalars().all()

    # Return paginated result
    return {
        "page": pagination.page if pagination else 1,
        "limit": limit_val,
        "total": total,
        "pages": total_pages,
        "data": orders
    }


async def get_order_items_by_order_id(db: AsyncSession, order_id: int) -> List[OrderItem]:
    """
    Get all items in an order
    """
    result = await db.execute(
        select(OrderItem)
        .where(OrderItem.order_id == order_id)
    )
    return result.scalars().all()


async def update_order_status(
    db: AsyncSession, order: Order, status: str, user_id: int
) -> Order:
    """
    Update an order's status and synchronize with shipment status

    Args:
        db: Database session
        order: Order to update
        status: New status
        user_id: ID of the user performing the update

    Returns:
        Updated order
    """
    old_status = order.status
    order.status = status
    await db.commit()
    await db.refresh(order)

    # # Send notification
    # await create_notification(
    #     db=db,
    #     user_id=order.user_id,
    #     notification_type="order_status_updated",
    #     content=f"Your order #{order.id} status has been updated to {status}.",
    #     related_entity_id=order.id
    # )

    return order


async def update_payment_status(
    db: AsyncSession, order: Order, payment_status: str, user_id: int
) -> Order:
    """
    Update an order's payment status

    If payment status is changed to "completed", this will:
    1. Update the order status to "processing"
    2. Reduce the stock quantity for all products in the order

    Args:
        db: Database session
        order: Order to update
        payment_status: New payment status
        user_id: ID of the user performing the update

    Returns:
        Updated order

    Raises:
        ValueError: If stock reduction fails
    """
    old_status = order.payment_status
    order.payment_status = payment_status

    # If payment is completed, update order status accordingly and reduce stock
    if payment_status == "completed" and order.status == "pending":
        order.status = "processing"

        # Commit the status change first
        await db.commit()
        await db.refresh(order)

        try:
            # Update product stock quantities
            await update_product_stock_for_order(db, order.id)
        except ValueError as e:
            # If stock update fails, revert the payment status
            order.payment_status = old_status
            order.status = "pending"
            await db.commit()
            await db.refresh(order)
            raise ValueError(f"Failed to update product stock: {str(e)}")
    else:
        # For other status changes, just commit
        await db.commit()
        await db.refresh(order)

    # Send notification
    await create_notification(
        db=db,
        user_id=order.user_id,
        notification_type="payment_status_updated",
        content=f"Payment status for order #{order.id} has been updated to {payment_status}.",
        related_entity_id=order.id
    )

    return order


async def update_shipping_details(
    db: AsyncSession, order: Order, tracking_number: str, shipping_carrier: str,
    estimated_delivery_date: str, user_id: int
) -> Order:
    """
    Update shipping details for an order and create/update shipment

    Args:
        db: Database session
        order: Order to update
        tracking_number: Tracking number
        shipping_carrier: Shipping carrier
        estimated_delivery_date: Estimated delivery date
        user_id: ID of the user performing the update

    Returns:
        Updated order
    """
    order.tracking_number = tracking_number
    order.shipping_carrier = shipping_carrier

    # Parse estimated_delivery_date if it's a string
    if isinstance(estimated_delivery_date, str):
        try:
            order.estimated_delivery_date = datetime.fromisoformat(estimated_delivery_date)
        except ValueError:
            # If parsing fails, keep the original value
            pass
    else:
        order.estimated_delivery_date = estimated_delivery_date

    # If this is the first time shipping details are added, update status to "shipped"
    status_changed = False
    if order.status == OrderStatus.PROCESSING:
        order.status = OrderStatus.SHIPPED
        status_changed = True

    await db.commit()
    await db.refresh(order)

    # Create or update shipment
    shipment_result = await db.execute(select(Shipment).where(Shipment.order_id == order.id))
    shipment = shipment_result.scalars().first()

    if shipment:
        # Update existing shipment
        shipment.carrier = shipping_carrier
        shipment.tracking_number = tracking_number
        shipment.estimated_delivery_date = order.estimated_delivery_date

        # Update shipment status if order status changed
        if status_changed:
            await update_shipment_status(
                db=db,
                shipment=shipment,
                status=ShipmentStatus.IN_TRANSIT,
                description=f"Order shipped with {shipping_carrier}. Tracking number: {tracking_number}",
                user_id=user_id
            )
        else:
            await db.commit()
    else:
        # Create new shipment
        shipment_status = ShipmentStatus.PENDING
        if order.status == OrderStatus.SHIPPED:
            shipment_status = ShipmentStatus.IN_TRANSIT

        await create_shipment_from_order(
            db=db,
            order=order,
            carrier=shipping_carrier,
            tracking_number=tracking_number,
            estimated_delivery_date=order.estimated_delivery_date
        )

    # Send notification
    await create_notification(
        db=db,
        user_id=order.user_id,
        notification_type="order_shipped",
        content=f"Your order #{order.id} has shipped! Tracking number: {tracking_number}",
        related_entity_id=order.id
    )

    return order


async def cancel_order(db: AsyncSession, order: Order, user_id: int) -> Order:
    """
    Cancel an order if it hasn't shipped yet and update shipment status

    Args:
        db: Database session
        order: Order to cancel
        user_id: ID of the user performing the cancellation

    Returns:
        Cancelled order

    Raises:
        ValueError: If order has already shipped or been delivered
    """
    if order.status in [OrderStatus.SHIPPED, OrderStatus.DELIVERED]:
        raise ValueError("Cannot cancel an order that has already shipped or been delivered")

    old_status = order.status
    order.status = OrderStatus.CANCELLED
    await db.commit()
    await db.refresh(order)

    # Update shipment status if exists
    shipment_result = await db.execute(select(Shipment).where(Shipment.order_id == order.id))
    shipment = shipment_result.scalars().first()

    if shipment:
        await update_shipment_status(
            db=db,
            shipment=shipment,
            status=ShipmentStatus.CANCELLED,
            description="Order was cancelled",
            user_id=user_id
        )

    # Send notification
    await create_notification(
        db=db,
        user_id=order.user_id,
        notification_type="order_cancelled",
        content=f"Your order #{order.id} has been cancelled.",
        related_entity_id=order.id
    )

    return order


# Transaction methods
async def create_transaction(db: AsyncSession, transaction: TransactionCreate, user_id: int) -> TransactionHistory:
    """
    Create a new transaction record for an order

    If the transaction is successful, this will:
    1. Update the order payment status to "completed"
    2. Update the order status to "processing"
    3. Reduce the stock quantity for all products in the order

    Args:
        db: Database session
        transaction: Transaction data
        user_id: ID of the user creating the transaction

    Returns:
        Created transaction record

    Raises:
        ValueError: If payment status update or stock reduction fails
    """
    db_transaction = TransactionHistory(
        order_id=transaction.order_id,
        transaction_type=transaction.transaction_type,
        amount=transaction.amount,
        payment_method=transaction.payment_method,
        status=transaction.status
    )
    db.add(db_transaction)
    await db.commit()
    await db.refresh(db_transaction)

    # Update order payment status if transaction is successful
    if transaction.status == "success":
        result = await db.execute(select(Order).where(Order.id == transaction.order_id))
        order = result.scalars().first()
        if order:
            try:
                # This will also update product stock
                await update_payment_status(db, order, "completed", user_id)
            except ValueError as e:
                # If payment status update fails (e.g., due to stock issues),
                # mark the transaction as failed
                db_transaction.status = "failed"
                db_transaction.notes = str(e)
                await db.commit()
                await db.refresh(db_transaction)
                raise ValueError(f"Transaction recorded but payment processing failed: {str(e)}")

    return db_transaction


async def get_order_transactions(db: AsyncSession, order_id: int) -> List[TransactionHistory]:
    """
    Get all transactions for an order
    """
    result = await db.execute(
        select(TransactionHistory)
        .where(TransactionHistory.order_id == order_id)
        .order_by(desc(TransactionHistory.transaction_date))
    )
    return result.scalars().all()


async def update_product_stock_for_order(db: AsyncSession, order_id: int) -> None:
    """
    Update product stock quantities after an order is successfully placed

    This function reduces the stock quantity for each product in the order.
    It should be called only when an order is confirmed (payment completed).

    Args:
        db: Database session
        order_id: ID of the order to process

    Raises:
        ValueError: If any product doesn't have enough stock
    """
    # Get order items
    order_items = await get_order_items(db, order_id)
    if not order_items:
        return

    # Process each order item
    for item in order_items:
        # Get the product
        product = await db.get(Product, item.product_id)
        if not product:
            continue

        # Check if product has variants
        variant_result = await db.execute(
            select(ProductVariant).where(ProductVariant.product_id == item.product_id)
        )
        variants = variant_result.scalars().all()

        if variants:
            # For products with variants, we should specify which variant to reduce
            # This is a simplified approach - in a real app, you'd have a variant_id in the order item

            # Find the variant with the most stock (simplified approach)
            variant_to_update = max(variants, key=lambda v: v.stock)

            # Check if there's enough stock
            if variant_to_update.stock < item.quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}, variant {variant_to_update.size}")

            # Update variant stock
            variant_to_update.stock -= item.quantity

        else:
            # Check if there's enough stock
            if product.quantity < item.quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}")

            # Update product stock
            product.quantity -= item.quantity

    # Commit all stock updates
    await db.commit()
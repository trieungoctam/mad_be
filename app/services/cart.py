from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from datetime import datetime
from fastapi import HTTPException, status

from app.models.cart import Cart, CartItem
from app.models.product import Product
from app.schemas.cart import CartCreate, CartItemCreate, CartItemUpdate


async def create_cart(db: AsyncSession, cart_in: CartCreate, user_id: int) -> Cart:
    """
    Create a new cart
    """
    db_cart = Cart(
        user_id=user_id,
        status=cart_in.status
    )
    db.add(db_cart)
    await db.commit()
    await db.refresh(db_cart)
    return db_cart


async def get_cart(db: AsyncSession, cart_id: int) -> Optional[Cart]:
    """
    Get a cart by ID
    """
    result = await db.execute(select(Cart).where(Cart.id == cart_id))
    return result.scalars().first()


async def get_cart_items(db: AsyncSession, cart_id: int):
    """
    Get all items in a cart
    """
    result = await db.execute(
        select(CartItem)
        .where(CartItem.cart_id == cart_id)
        .order_by(CartItem.added_at.desc())
    )
    return result.scalars().all()

async def get_active_cart(db: AsyncSession, user_id: int) -> Optional[Cart]:
    """
    Get the active cart for a user, creating one if it doesn't exist
    """
    result = await db.execute(
        select(Cart)
        .where(Cart.user_id == user_id)
        .where(Cart.status == "active")
    )
    cart = result.scalars().first()

    if not cart:
        # Create a new cart
        cart = Cart(
            user_id=user_id,
            status="active"
        )
        db.add(cart)
        await db.commit()
        await db.refresh(cart)

    return cart


async def add_to_cart(db: AsyncSession, cart_item: CartItemCreate, user_id: int) -> CartItem:
    """
    Add an item to the user's active cart

    Checks if there's sufficient stock before adding to cart.
    Stock is not reduced when adding to cart, only when an order is placed.

    Args:
        db: Database session
        cart_item: Cart item data with product_id and quantity
        user_id: ID of the user adding to cart

    Returns:
        The created or updated cart item

    Raises:
        ValueError: If product not found or insufficient stock
    """
    # Get/create active cart for user
    cart = await get_active_cart(db, user_id)
    if not cart:
        cart_data = CartCreate(user_id=user_id, status="active")
        cart = await create_cart(db, cart_data)

    # Check if product exists
    product = await db.get(Product, cart_item.product_id)
    if not product:
        raise ValueError(f"Product with ID {cart_item.product_id} not found")

    # Check if product has variants
    from sqlalchemy import select
    from app.models.product import ProductVariant

    variant_result = await db.execute(
        select(ProductVariant).where(ProductVariant.product_id == cart_item.product_id)
    )
    variants = variant_result.scalars().all()

    # If product has variants, we should check variant stock instead of product stock
    if variants:
        # For products with variants, we should specify which variant to add
        # This is a simplified check - in a real app, you'd have a variant_id in the cart item
        total_variant_stock = sum(variant.stock for variant in variants)
        if total_variant_stock < cart_item.quantity:
            raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {total_variant_stock}")
    else:
        # Check if there's enough stock for the product
        if product.quantity < cart_item.quantity:
            raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {product.quantity}")

    # Check if item already in cart, update quantity if so
    result = await db.execute(
        select(CartItem)
        .where(CartItem.cart_id == cart.id)
        .where(CartItem.product_id == cart_item.product_id)
    )
    existing_item = result.scalars().first()

    if existing_item:
        # Check if the new total quantity exceeds available stock
        new_quantity = existing_item.quantity + cart_item.quantity

        if variants:
            if total_variant_stock < new_quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {total_variant_stock}, Requested: {new_quantity}")
        else:
            if product.quantity < new_quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {product.quantity}, Requested: {new_quantity}")

        existing_item.quantity = new_quantity
        await db.commit()
        await db.refresh(existing_item)
        return existing_item
    else:
        # Add new item to cart
        db_item = CartItem(
            cart_id=cart.id,
            user_id=user_id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity,
            unit_price=product.price,
        )

        db.add(db_item)
        await db.commit()
        await db.refresh(db_item)
        return db_item


async def add_item_to_cart(db: AsyncSession, cart_id: int, item_in: CartItemCreate) -> Cart:
    """
    Add an item to a specific cart by ID

    Checks if there's sufficient stock before adding to cart.
    Stock is not reduced when adding to cart, only when an order is placed.

    Args:
        db: Database session
        cart_id: ID of the cart to add item to
        item_in: Cart item data with product_id and quantity

    Returns:
        The updated cart

    Raises:
        ValueError: If cart not found, product not found, or insufficient stock
    """
    # Check if cart exists
    cart = await db.get(Cart, cart_id)
    if not cart:
        raise ValueError(f"Cart with ID {cart_id} not found")

    # Check if product exists
    product = await db.get(Product, item_in.product_id)
    if not product:
        raise ValueError(f"Product with ID {item_in.product_id} not found")

    # Check if product has variants
    from sqlalchemy import select
    from app.models.product import ProductVariant

    variant_result = await db.execute(
        select(ProductVariant).where(ProductVariant.product_id == item_in.product_id)
    )
    variants = variant_result.scalars().all()

    # If product has variants, we should check variant stock instead of product stock
    if variants:
        # For products with variants, we should specify which variant to add
        # This is a simplified check - in a real app, you'd have a variant_id in the cart item
        total_variant_stock = sum(variant.stock for variant in variants)
        if total_variant_stock < item_in.quantity:
            raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {total_variant_stock}")
    else:
        # Check if there's enough stock for the product
        if product.quantity < item_in.quantity:
            raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {product.quantity}")

    # Check if item already in cart, update quantity if so
    result = await db.execute(
        select(CartItem)
        .where(CartItem.cart_id == cart_id)
        .where(CartItem.product_id == item_in.product_id)
    )
    existing_item = result.scalars().first()

    if existing_item:
        # Check if the new total quantity exceeds available stock
        new_quantity = existing_item.quantity + item_in.quantity

        if variants:
            if total_variant_stock < new_quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {total_variant_stock}, Requested: {new_quantity}")
        else:
            if product.quantity < new_quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {product.quantity}, Requested: {new_quantity}")

        existing_item.quantity = new_quantity
        await db.commit()
    else:
        # Add new item to cart
        db_item = CartItem(
            cart_id=cart_id,
            user_id=cart.user_id,  # Get user_id from the cart
            product_id=item_in.product_id,
            quantity=item_in.quantity,
            unit_price=product.price,  # Changed from default_price to price
        )
        db.add(db_item)
        await db.commit()

    # Return updated cart
    result = await db.execute(
        select(Cart)
        .where(Cart.id == cart_id)
    )
    return result.scalars().first()


async def update_cart_item(
    db: AsyncSession, cart_id: int, item_id: int, item_in: CartItemUpdate
) -> Cart:
    """
    Update a cart item's quantity

    Checks if there's sufficient stock before updating quantity.

    Args:
        db: Database session
        cart_id: ID of the cart containing the item
        item_id: ID of the cart item to update
        item_in: Updated cart item data with new quantity

    Returns:
        The updated cart

    Raises:
        ValueError: If cart item not found or insufficient stock
    """
    # Find the cart item
    result = await db.execute(
        select(CartItem)
        .where(CartItem.id == item_id)
        .where(CartItem.cart_id == cart_id)
    )
    cart_item = result.scalars().first()

    if not cart_item:
        raise ValueError(f"Cart item with ID {item_id} not found in cart {cart_id}")

    # If quantity is 0, remove the item
    if item_in.quantity == 0:
        await db.execute(delete(CartItem).where(CartItem.id == item_id))
    else:
        # Get product to check stock
        product = await db.get(Product, cart_item.product_id)
        if not product:
            raise ValueError(f"Product with ID {cart_item.product_id} not found")

        # Check if product has variants
        from app.models.product import ProductVariant

        variant_result = await db.execute(
            select(ProductVariant).where(ProductVariant.product_id == cart_item.product_id)
        )
        variants = variant_result.scalars().all()

        # Check if there's enough stock
        if variants:
            total_variant_stock = sum(variant.stock for variant in variants)
            if total_variant_stock < item_in.quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {total_variant_stock}, Requested: {item_in.quantity}")
        else:
            if product.quantity < item_in.quantity:
                raise ValueError(f"Insufficient stock for product {product.product_name}. Available: {product.quantity}, Requested: {item_in.quantity}")

        # Update the item
        cart_item.quantity = item_in.quantity

    await db.commit()

    # Return the updated cart
    result = await db.execute(
        select(Cart)
        .where(Cart.id == cart_id)
    )
    return result.scalars().first()


async def remove_from_cart(db: AsyncSession, cart_item_id: int, user_id: int) -> None:
    """
    Remove an item from the cart
    """
    # Get the cart item first to log details
    result = await db.execute(select(CartItem).where(CartItem.id == cart_item_id))
    cart_item = result.scalars().first()

    if cart_item:
        product_id = cart_item.product_id

        # Delete the item
        await db.execute(delete(CartItem).where(CartItem.id == cart_item_id))
        await db.commit()


async def clear_cart(db: AsyncSession, cart_id: int, user_id: int) -> None:
    """
    Remove all items from the cart
    """
    await db.execute(delete(CartItem).where(CartItem.cart_id == cart_id))
    await db.commit()


async def abandon_cart(db: AsyncSession, cart_id: int, user_id: int) -> Cart:
    """
    Mark a cart as abandoned
    """
    result = await db.execute(select(Cart).where(Cart.id == cart_id))
    cart = result.scalars().first()

    if cart:
        cart.status = "abandoned"
        await db.commit()
        await db.refresh(cart)

    return cart


async def calculate_cart_total(db: AsyncSession, cart_id: int) -> float:
    """
    Calculate the total price of all items in the cart
    """
    result = await db.execute(
        select(CartItem)
        .where(CartItem.cart_id == cart_id)
    )
    cart_items = result.scalars().all()

    total = 0.0
    for item in cart_items:
        total += item.quantity * item.unit_price

    return total


async def delete_cart_item(db: AsyncSession, cart_item_id: int, user_id: int) -> None:
    """
    Delete a specific item from the cart
    """
    # Verify that the item exists
    result = await db.execute(select(CartItem).where(CartItem.id == cart_item_id))
    cart_item = result.scalars().first()

    if not cart_item:
        raise ValueError(f"Cart item with ID {cart_item_id} not found")

    # Verify that the cart belongs to the user
    cart_result = await db.execute(
        select(Cart)
        .where(Cart.id == cart_item.cart_id)
        .where(Cart.user_id == user_id)
    )
    cart = cart_result.scalars().first()

    if not cart:
        raise ValueError("You do not have permission to delete this cart item")

    # Delete the item
    await db.execute(delete(CartItem).where(CartItem.id == cart_item_id))
    await db.commit()


async def delete_cart(db: AsyncSession, cart_id: int, user_id: int) -> None:
    """
    Delete an entire cart and its items
    """
    # Verify that the cart exists and belongs to the user
    result = await db.execute(
        select(Cart)
        .where(Cart.id == cart_id)
        .where(Cart.user_id == user_id)
    )
    cart = result.scalars().first()

    if not cart:
        raise ValueError(f"Cart with ID {cart_id} not found or you don't have permission to delete it")

    # Delete all cart items first
    await db.execute(delete(CartItem).where(CartItem.cart_id == cart_id))

    # Then delete the cart
    await db.execute(delete(Cart).where(Cart.id == cart_id))
    await db.commit()


async def get_cart_item(db: AsyncSession, item_id: int) -> Optional[CartItem]:
    """
    Get a specific cart item by ID
    """
    result = await db.execute(
        select(CartItem)
        .where(CartItem.id == item_id)
    )
    return result.scalars().first()


async def update_item_quantity(db: AsyncSession, item_id: int, quantity: int) -> Cart:
    """
    Update a cart item's quantity

    Checks if there's sufficient stock before updating quantity.

    Args:
        db: Database session
        item_id: ID of the cart item to update
        quantity: New quantity for the cart item

    Returns:
        The updated cart

    Raises:
        HTTPException: If cart item not found or insufficient stock
    """
    # Find the cart item
    result = await db.execute(
        select(CartItem)
        .where(CartItem.id == item_id)
    )
    cart_item = result.scalars().first()

    if not cart_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart item not found"
        )

    # If quantity is 0, remove the item
    if quantity == 0:
        await db.delete(cart_item)
        await db.commit()
        return await get_cart(db=db, cart_id=cart_item.cart_id)

    # Get product to check stock
    product = await db.get(Product, cart_item.product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {cart_item.product_id} not found"
        )

    # Check if product has variants
    from app.models.product import ProductVariant

    variant_result = await db.execute(
        select(ProductVariant).where(ProductVariant.product_id == cart_item.product_id)
    )
    variants = variant_result.scalars().all()

    # Check if there's enough stock
    if variants:
        total_variant_stock = sum(variant.stock for variant in variants)
        if total_variant_stock < quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient stock for product {product.product_name}. Available: {total_variant_stock}, Requested: {quantity}"
            )
    else:
        if product.quantity < quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Insufficient stock for product {product.product_name}. Available: {product.quantity}, Requested: {quantity}"
            )

    # Update quantity
    cart_item.quantity = quantity
    await db.commit()
    await db.refresh(cart_item)

    # Return the updated cart
    return await get_cart(db=db, cart_id=cart_item.cart_id)


async def remove_item_from_cart(db: AsyncSession, item_id: int) -> None:
    """
    Remove an item from cart
    """
    # Find the cart item
    result = await db.execute(
        select(CartItem)
        .where(CartItem.id == item_id)
    )
    cart_item = result.scalars().first()

    if not cart_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart item not found"
        )

    # Delete the cart item
    await db.delete(cart_item)
    await db.commit()
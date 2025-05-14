from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.deps import get_current_active_user, get_current_superuser
from app.db.session import get_db
from app.models.user import User
from app.models.order import OrderStatus
from app.schemas.base import PaginationParams
from app.schemas.order import Order, OrderCreate, OrderUpdate, OrderPaginated
from app.services.order import (
    create_order,
    get_order,
    get_user_orders,
    update_order_status,
    update_payment_status,
    update_shipping_details,
    cancel_order,
    get_order_items
)

router = APIRouter()


@router.get("/")
async def read_orders(
    pagination: PaginationParams = Depends(),
    status: OrderStatus = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get all current user's orders with pagination and filtering
    """
    data = await get_user_orders(
        db=db, user_id=current_user.id, pagination=pagination, status=status
    )
    orders = data["data"]
    orders_list = [
        {
            "id": order.id,
            "user_id": order.user_id,
            "order_date": order.order_date,
            "status": order.status,
            "total_amount": order.total_amount,
            "payment_status": order.payment_status,
            "payment_method": order.payment_method
        } for order in orders
    ]
    return orders_list

@router.get("/{order_id}", response_model=Order)
async def read_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get a specific order by ID
    """
    order = await get_order(db=db, order_id=order_id)

    # Check if order exists and belongs to current user
    if not order or (order.user_id != current_user.id and not current_user.is_superuser):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    # Convert SQLAlchemy model to dict for Pydantic
    return {
        "id": order.id,
        "user_id": order.user_id,
        "order_date": order.order_date,
        "status": order.status,
        "total_amount": order.total_amount,
        "payment_status": order.payment_status,
        "payment_method": order.payment_method,
        "shipping_address_id": order.shipping_address_id,
        "shipping_carrier": order.shipping_carrier,
        "tracking_number": order.tracking_number,
        "estimated_delivery_date": order.estimated_delivery_date,
        "created_at": order.created_at,
        "updated_at": order.updated_at,
        "items": order.items
    }

@router.put("/{order_id}/status")
async def update_order_status(
    order_id: int,
    status: OrderStatus,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Update the status of an order
    """
    order = await get_order(db=db, order_id=order_id)

    # Update order status
    await update_order_status(db=db, order_id=order_id, status=status)

    return {"message": "Order status updated successfully"}

@router.get("/{order_id}/items")
async def get_order_items(db: AsyncSession, order_id: int) -> List[Any]:
    """
    Get all items in an order
    """
    order_items = await get_order_items(db=db, order_id=order_id)
    return order_items
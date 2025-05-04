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
    cancel_order
)

router = APIRouter()


@router.get("/", response_model=OrderPaginated)
async def read_orders(
    pagination: PaginationParams = Depends(),
    status: OrderStatus = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get all current user's orders with pagination and filtering
    """
    return await get_user_orders(
        db=db, user_id=current_user.id, pagination=pagination, status=status
    )


@router.post("/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_new_order(
    order_in: OrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Create a new order
    """
    order = await create_order(db=db, user_id=current_user.id, order_in=order_in)

    return order


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

    return order


@router.put("/{order_id}", response_model=Order)
async def update_order_status_endpoint(
    order_id: int,
    order_in: OrderUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_superuser),
) -> Any:
    """
    Update order status (admin only)
    """
    order = await get_order(db=db, order_id=order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    if order_in.status:
        order = await update_order_status(db=db, order=order, status=order_in.status, user_id=current_user.id)

    if order_in.payment_status:
        order = await update_payment_status(db=db, order=order, payment_status=order_in.payment_status, user_id=current_user.id)

    if order_in.shipping_carrier or order_in.tracking_number or order_in.estimated_delivery_date:
        order = await update_shipping_details(
            db=db,
            order=order,
            shipping_carrier=order_in.shipping_carrier or order.shipping_carrier,
            tracking_number=order_in.tracking_number or order.tracking_number,
            estimated_delivery_date=order_in.estimated_delivery_date or order.estimated_delivery_date,
            user_id=current_user.id
        )

    return order


@router.get("/{order_id}/track", response_model=None)
async def track_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Track order shipping status

    This endpoint redirects to the shipment tracking endpoint for more detailed tracking information.
    """
    order = await get_order(db=db, order_id=order_id)

    # Check if order exists and belongs to current user
    if not order or (order.user_id != current_user.id and not current_user.is_superuser):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

    # Redirect to shipment tracking endpoint
    from app.services.shipment import track_shipment
    tracking_info = await track_shipment(db=db, order_id=order_id)

    if not tracking_info:
        # If no tracking info is available, return the order with basic info
        return {
            "order_id": order.id,
            "status": order.status,
            "tracking_number": order.tracking_number,
            "shipping_carrier": order.shipping_carrier,
            "estimated_delivery_date": order.estimated_delivery_date,
            "message": "No detailed tracking information available yet"
        }

    return tracking_info
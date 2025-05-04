from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.deps import get_current_active_user, get_current_superuser
from app.db.session import get_db
from app.models.user import User
from app.models.shipment import ShipmentStatus
from app.schemas.base import PaginationParams
from app.schemas.shipment import (
    Shipment,
    ShipmentCreate,
    ShipmentUpdate,
    ShipmentTrackingEvent,
    ShipmentTrackingEventCreate,
    TrackingResponse,
    ShipmentPaginated
)
from app.services.shipment import (
    add_tracking_event,
    create_shipment,
    get_shipment,
    get_shipment_by_order,
    get_shipments,
    get_tracking_events,
    track_shipment,
    update_shipment_status
)
from app.services.order import get_order

router = APIRouter()


@router.get("/", response_model=ShipmentPaginated)
async def read_shipments(
    pagination: PaginationParams = Depends(),
    status: Optional[ShipmentStatus] = None,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_superuser),
) -> Any:
    """
    Get all shipments with pagination and filtering (admin only)
    """
    shipments = await get_shipments(
        db=db,
        skip=(pagination.page - 1) * pagination.limit,
        limit=pagination.limit,
        status=status
    )
    
    # Calculate total count (simplified for now)
    total = len(shipments)
    total_pages = (total + pagination.limit - 1) // pagination.limit if pagination.limit > 0 else 0
    
    return {
        "page": pagination.page,
        "limit": pagination.limit,
        "total": total,
        "pages": total_pages,
        "data": shipments
    }


@router.post("/", response_model=Shipment, status_code=status.HTTP_201_CREATED)
async def create_new_shipment(
    shipment_in: ShipmentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_superuser),
) -> Any:
    """
    Create a new shipment (admin only)
    """
    # Check if order exists
    order = await get_order(db=db, order_id=shipment_in.order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    # Check if shipment already exists for this order
    existing_shipment = await get_shipment_by_order(db=db, order_id=shipment_in.order_id)
    if existing_shipment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Shipment already exists for this order"
        )
    
    return await create_shipment(db=db, shipment_in=shipment_in)


@router.get("/{shipment_id}", response_model=Shipment)
async def read_shipment(
    shipment_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get a specific shipment
    """
    shipment = await get_shipment(db=db, shipment_id=shipment_id)
    if not shipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found"
        )
    
    # Check if user has access to this shipment
    order = await get_order(db=db, order_id=shipment.order_id)
    if not order or (order.user_id != current_user.id and not current_user.is_superuser):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this shipment"
        )
    
    return shipment


@router.put("/{shipment_id}", response_model=Shipment)
async def update_shipment(
    shipment_id: int,
    shipment_in: ShipmentUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_superuser),
) -> Any:
    """
    Update a shipment (admin only)
    """
    shipment = await get_shipment(db=db, shipment_id=shipment_id)
    if not shipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found"
        )
    
    # Update shipment status if provided
    if shipment_in.status and shipment_in.status != shipment.status:
        shipment = await update_shipment_status(
            db=db,
            shipment=shipment,
            status=shipment_in.status,
            user_id=current_user.id
        )
    
    # Update other fields
    if shipment_in.carrier is not None:
        shipment.carrier = shipment_in.carrier
    
    if shipment_in.tracking_number is not None:
        shipment.tracking_number = shipment_in.tracking_number
    
    if shipment_in.estimated_delivery_date is not None:
        shipment.estimated_delivery_date = shipment_in.estimated_delivery_date
    
    if shipment_in.actual_delivery_date is not None:
        shipment.actual_delivery_date = shipment_in.actual_delivery_date
    
    if shipment_in.shipping_cost is not None:
        shipment.shipping_cost = shipment_in.shipping_cost
    
    await db.commit()
    await db.refresh(shipment)
    
    return shipment


@router.post("/{shipment_id}/events", response_model=ShipmentTrackingEvent)
async def add_tracking_event_endpoint(
    shipment_id: int,
    event_in: ShipmentTrackingEventCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_superuser),
) -> Any:
    """
    Add a tracking event to a shipment (admin only)
    """
    shipment = await get_shipment(db=db, shipment_id=shipment_id)
    if not shipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found"
        )
    
    return await add_tracking_event(db=db, shipment_id=shipment_id, event_in=event_in)


@router.get("/{shipment_id}/events", response_model=List[ShipmentTrackingEvent])
async def read_tracking_events_endpoint(
    shipment_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get all tracking events for a shipment
    """
    shipment = await get_shipment(db=db, shipment_id=shipment_id)
    if not shipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found"
        )
    
    # Check if user has access to this shipment
    order = await get_order(db=db, order_id=shipment.order_id)
    if not order or (order.user_id != current_user.id and not current_user.is_superuser):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this shipment"
        )
    
    return await get_tracking_events(db=db, shipment_id=shipment_id)


@router.get("/order/{order_id}", response_model=Shipment)
async def get_shipment_by_order_endpoint(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get shipment by order ID
    """
    # Check if order exists and user has access
    order = await get_order(db=db, order_id=order_id)
    if not order or (order.user_id != current_user.id and not current_user.is_superuser):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    shipment = await get_shipment_by_order(db=db, order_id=order_id)
    if not shipment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No shipment found for this order"
        )
    
    return shipment


@router.get("/track/{order_id}", response_model=TrackingResponse)
async def track_shipment_endpoint(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Track a shipment by order ID
    """
    # Check if order exists and user has access
    order = await get_order(db=db, order_id=order_id)
    if not order or (order.user_id != current_user.id and not current_user.is_superuser):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    
    tracking_info = await track_shipment(db=db, order_id=order_id)
    if not tracking_info:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No tracking information available for this order"
        )
    
    return tracking_info

from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete, desc
from sqlalchemy.sql import func

from app.models.shipment import Shipment, ShipmentTrackingEvent, ShipmentStatus
from app.models.order import Order, OrderStatus
from app.models.user import User
from app.schemas.shipment import (
    ShipmentCreate, 
    ShipmentUpdate, 
    ShipmentTrackingEventCreate,
    TrackingResponse
)
from app.services.notification import create_notification


async def create_shipment(db: AsyncSession, shipment_in: ShipmentCreate) -> Shipment:
    """
    Create a new shipment for an order
    
    Args:
        db: Database session
        shipment_in: Shipment data
        
    Returns:
        Created shipment
    """
    # Create shipment record
    db_shipment = Shipment(
        order_id=shipment_in.order_id,
        status=shipment_in.status,
        carrier=shipment_in.carrier,
        tracking_number=shipment_in.tracking_number,
        estimated_delivery_date=shipment_in.estimated_delivery_date,
        actual_delivery_date=shipment_in.actual_delivery_date,
        shipping_cost=shipment_in.shipping_cost
    )
    db.add(db_shipment)
    await db.commit()
    await db.refresh(db_shipment)
    
    # Create initial tracking event
    if db_shipment.status:
        event = ShipmentTrackingEvent(
            shipment_id=db_shipment.id,
            event_date=datetime.now(),
            status=db_shipment.status,
            description=f"Shipment created with status: {db_shipment.status}"
        )
        db.add(event)
        await db.commit()
    
    return db_shipment


async def get_shipment(db: AsyncSession, shipment_id: int) -> Optional[Shipment]:
    """
    Get a shipment by ID
    
    Args:
        db: Database session
        shipment_id: ID of the shipment
        
    Returns:
        Shipment if found, None otherwise
    """
    result = await db.execute(select(Shipment).where(Shipment.id == shipment_id))
    return result.scalars().first()


async def get_shipment_by_order(db: AsyncSession, order_id: int) -> Optional[Shipment]:
    """
    Get a shipment by order ID
    
    Args:
        db: Database session
        order_id: ID of the order
        
    Returns:
        Shipment if found, None otherwise
    """
    result = await db.execute(select(Shipment).where(Shipment.order_id == order_id))
    return result.scalars().first()


async def get_shipments(
    db: AsyncSession, 
    skip: int = 0, 
    limit: int = 100, 
    status: Optional[str] = None
) -> List[Shipment]:
    """
    Get all shipments with optional filtering
    
    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return
        status: Filter by status
        
    Returns:
        List of shipments
    """
    query = select(Shipment)
    
    if status:
        query = query.where(Shipment.status == status)
    
    query = query.order_by(desc(Shipment.created_at)).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


async def update_shipment_status(
    db: AsyncSession, 
    shipment: Shipment, 
    status: str,
    location: Optional[str] = None,
    description: Optional[str] = None,
    user_id: Optional[int] = None
) -> Shipment:
    """
    Update a shipment's status and create a tracking event
    
    Args:
        db: Database session
        shipment: Shipment to update
        status: New status
        location: Current location (optional)
        description: Event description (optional)
        user_id: ID of the user performing the update (optional)
        
    Returns:
        Updated shipment
    """
    old_status = shipment.status
    shipment.status = status
    
    # Update actual delivery date if status is DELIVERED
    if status == ShipmentStatus.DELIVERED and not shipment.actual_delivery_date:
        shipment.actual_delivery_date = datetime.now()
    
    # Create tracking event
    event = ShipmentTrackingEvent(
        shipment_id=shipment.id,
        event_date=datetime.now(),
        status=status,
        location=location,
        description=description or f"Status updated from {old_status} to {status}"
    )
    db.add(event)
    
    # Update order status if needed
    if shipment.order_id:
        result = await db.execute(select(Order).where(Order.id == shipment.order_id))
        order = result.scalars().first()
        
        if order:
            # Map shipment status to order status
            if status == ShipmentStatus.PICKED_UP or status == ShipmentStatus.IN_TRANSIT:
                order.status = OrderStatus.SHIPPED
            elif status == ShipmentStatus.DELIVERED:
                order.status = OrderStatus.DELIVERED
            elif status == ShipmentStatus.RETURNED:
                order.status = OrderStatus.RETURNED
            elif status == ShipmentStatus.CANCELLED:
                order.status = OrderStatus.CANCELLED
            
            # Send notification to user
            if user_id and order.user_id:
                await create_notification(
                    db=db,
                    user_id=order.user_id,
                    notification_type="shipment_update",
                    content=f"Your shipment for order #{order.id} has been updated to {status}.",
                    related_entity_id=order.id
                )
    
    await db.commit()
    await db.refresh(shipment)
    
    return shipment


async def add_tracking_event(
    db: AsyncSession, 
    shipment_id: int, 
    event_in: ShipmentTrackingEventCreate
) -> ShipmentTrackingEvent:
    """
    Add a tracking event to a shipment
    
    Args:
        db: Database session
        shipment_id: ID of the shipment
        event_in: Tracking event data
        
    Returns:
        Created tracking event
    """
    # Create tracking event
    db_event = ShipmentTrackingEvent(
        shipment_id=shipment_id,
        event_date=event_in.event_date,
        status=event_in.status,
        location=event_in.location,
        description=event_in.description
    )
    db.add(db_event)
    
    # Update shipment status
    result = await db.execute(select(Shipment).where(Shipment.id == shipment_id))
    shipment = result.scalars().first()
    
    if shipment:
        shipment.status = event_in.status
        
        # Update actual delivery date if status is DELIVERED
        if event_in.status == ShipmentStatus.DELIVERED and not shipment.actual_delivery_date:
            shipment.actual_delivery_date = event_in.event_date
    
    await db.commit()
    await db.refresh(db_event)
    
    return db_event


async def get_tracking_events(db: AsyncSession, shipment_id: int) -> List[ShipmentTrackingEvent]:
    """
    Get all tracking events for a shipment
    
    Args:
        db: Database session
        shipment_id: ID of the shipment
        
    Returns:
        List of tracking events
    """
    result = await db.execute(
        select(ShipmentTrackingEvent)
        .where(ShipmentTrackingEvent.shipment_id == shipment_id)
        .order_by(desc(ShipmentTrackingEvent.event_date))
    )
    return result.scalars().all()


async def track_shipment(db: AsyncSession, order_id: int) -> Optional[TrackingResponse]:
    """
    Track a shipment by order ID
    
    Args:
        db: Database session
        order_id: ID of the order
        
    Returns:
        Tracking response if found, None otherwise
    """
    # Get order
    order_result = await db.execute(select(Order).where(Order.id == order_id))
    order = order_result.scalars().first()
    
    if not order:
        return None
    
    # Get shipment
    shipment_result = await db.execute(select(Shipment).where(Shipment.order_id == order_id))
    shipment = shipment_result.scalars().first()
    
    if not shipment:
        # Create a default shipment if none exists
        shipment = await create_shipment(
            db=db,
            shipment_in=ShipmentCreate(
                order_id=order_id,
                status=ShipmentStatus.PENDING,
                carrier=order.shipping_carrier,
                tracking_number=order.tracking_number,
                estimated_delivery_date=order.estimated_delivery_date
            )
        )
    
    # Get user
    user_result = await db.execute(select(User).where(User.id == order.user_id))
    user = user_result.scalars().first()
    
    # Get tracking events
    events_result = await db.execute(
        select(ShipmentTrackingEvent)
        .where(ShipmentTrackingEvent.shipment_id == shipment.id)
        .order_by(desc(ShipmentTrackingEvent.event_date))
    )
    shipment.tracking_events = events_result.scalars().all()
    
    # Generate tracking URL (this would be carrier-specific in a real app)
    tracking_url = None
    if shipment.carrier and shipment.tracking_number:
        if shipment.carrier.lower() == "ghn":
            tracking_url = f"https://ghn.vn/tracking?code={shipment.tracking_number}"
        elif shipment.carrier.lower() == "ghtk":
            tracking_url = f"https://ghtk.vn/tracking?code={shipment.tracking_number}"
        elif shipment.carrier.lower() == "viettel_post":
            tracking_url = f"https://viettelpost.com.vn/tracking?code={shipment.tracking_number}"
        else:
            # Generic tracking URL
            tracking_url = f"/api/v1/shipments/{shipment.id}/track"
    
    # Build response
    return TrackingResponse(
        shipment=shipment,
        order_id=order.id,
        order_status=order.status,
        customer_name=user.full_name if user else None,
        shipping_address=order.shipping_address.dict() if order.shipping_address else None,
        estimated_delivery_date=shipment.estimated_delivery_date,
        tracking_url=tracking_url
    )


async def create_shipment_from_order(
    db: AsyncSession, 
    order: Order,
    carrier: Optional[str] = None,
    tracking_number: Optional[str] = None,
    estimated_delivery_date: Optional[datetime] = None
) -> Shipment:
    """
    Create a shipment from an order
    
    Args:
        db: Database session
        order: Order to create shipment for
        carrier: Shipping carrier
        tracking_number: Tracking number
        estimated_delivery_date: Estimated delivery date
        
    Returns:
        Created shipment
    """
    # Check if shipment already exists
    result = await db.execute(select(Shipment).where(Shipment.order_id == order.id))
    existing_shipment = result.scalars().first()
    
    if existing_shipment:
        return existing_shipment
    
    # Map order status to shipment status
    status = ShipmentStatus.PENDING
    if order.status == OrderStatus.PROCESSING:
        status = ShipmentStatus.PROCESSING
    elif order.status == OrderStatus.SHIPPED:
        status = ShipmentStatus.IN_TRANSIT
    elif order.status == OrderStatus.DELIVERED:
        status = ShipmentStatus.DELIVERED
    elif order.status == OrderStatus.CANCELLED:
        status = ShipmentStatus.CANCELLED
    elif order.status == OrderStatus.RETURNED:
        status = ShipmentStatus.RETURNED
    
    # Use order shipping details if not provided
    carrier = carrier or order.shipping_carrier
    tracking_number = tracking_number or order.tracking_number
    estimated_delivery_date = estimated_delivery_date or order.estimated_delivery_date
    
    # If no estimated delivery date, set a default (7 days from now)
    if not estimated_delivery_date:
        estimated_delivery_date = datetime.now() + timedelta(days=7)
    
    # Create shipment
    shipment_in = ShipmentCreate(
        order_id=order.id,
        status=status,
        carrier=carrier,
        tracking_number=tracking_number,
        estimated_delivery_date=estimated_delivery_date
    )
    
    return await create_shipment(db=db, shipment_in=shipment_in)

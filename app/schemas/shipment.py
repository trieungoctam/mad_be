from datetime import datetime
from typing import List, Optional

from app.models.shipment import ShipmentStatus
from app.schemas.base import BaseModel, PaginatedResponse


class ShipmentTrackingEventBase(BaseModel):
    """Base schema for shipment tracking event data"""
    event_date: datetime
    status: str
    location: Optional[str] = None
    description: Optional[str] = None


class ShipmentTrackingEventCreate(ShipmentTrackingEventBase):
    """Schema for creating a new shipment tracking event"""
    pass


class ShipmentTrackingEvent(ShipmentTrackingEventBase):
    """Schema for shipment tracking event returned from API"""
    id: int
    shipment_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ShipmentBase(BaseModel):
    """Base schema for shipment data"""
    order_id: int
    status: str = ShipmentStatus.PENDING
    carrier: Optional[str] = None
    tracking_number: Optional[str] = None
    estimated_delivery_date: Optional[datetime] = None
    actual_delivery_date: Optional[datetime] = None
    shipping_cost: Optional[float] = None


class ShipmentCreate(ShipmentBase):
    """Schema for creating a new shipment"""
    pass


class ShipmentUpdate(BaseModel):
    """Schema for updating an existing shipment"""
    status: Optional[str] = None
    carrier: Optional[str] = None
    tracking_number: Optional[str] = None
    estimated_delivery_date: Optional[datetime] = None
    actual_delivery_date: Optional[datetime] = None
    shipping_cost: Optional[float] = None


class Shipment(ShipmentBase):
    """Schema for shipment returned from API"""
    id: int
    created_at: datetime
    updated_at: datetime
    tracking_events: List[ShipmentTrackingEvent] = []

    class Config:
        from_attributes = True


class ShipmentWithOrder(Shipment):
    """Schema for shipment with order details"""
    order_number: str
    order_date: datetime
    customer_name: str
    shipping_address: dict


class ShipmentPaginated(PaginatedResponse):
    """Schema for paginated shipments"""
    data: List[Shipment]


class TrackingResponse(BaseModel):
    """Schema for tracking response"""
    shipment: Shipment
    order_id: int
    order_status: str
    customer_name: Optional[str] = None
    shipping_address: Optional[dict] = None
    estimated_delivery_date: Optional[datetime] = None
    tracking_url: Optional[str] = None

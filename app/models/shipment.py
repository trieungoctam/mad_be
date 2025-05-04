from datetime import datetime
from enum import Enum
from typing import List

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class ShipmentStatus(str, Enum):
    """Shipment status enum"""
    PENDING = "pending"
    PROCESSING = "processing"
    PICKED_UP = "picked_up"
    IN_TRANSIT = "in_transit"
    OUT_FOR_DELIVERY = "out_for_delivery"
    DELIVERED = "delivered"
    FAILED_DELIVERY = "failed_delivery"
    RETURNED = "returned"
    CANCELLED = "cancelled"


class Shipment(Base):
    """Shipment tracking information"""
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    status = Column(String(50), default=ShipmentStatus.PENDING)
    carrier = Column(String(100), nullable=True)
    tracking_number = Column(String(100), nullable=True)
    estimated_delivery_date = Column(DateTime(timezone=True), nullable=True)
    actual_delivery_date = Column(DateTime(timezone=True), nullable=True)
    shipping_cost = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Relationships
    order = relationship("Order", back_populates="shipment")
    tracking_events = relationship("ShipmentTrackingEvent", back_populates="shipment", cascade="all, delete-orphan")


class ShipmentTrackingEvent(Base):
    """Tracking events for a shipment"""
    __tablename__ = "shipment_tracking_events"

    id = Column(Integer, primary_key=True, index=True)
    shipment_id = Column(Integer, ForeignKey("shipments.id", ondelete="CASCADE"), nullable=False)
    event_date = Column(DateTime(timezone=True), nullable=False)
    location = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    shipment = relationship("Shipment", back_populates="tracking_events")

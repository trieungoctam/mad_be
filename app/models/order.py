from datetime import datetime
from enum import Enum

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class OrderStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"

class PaymentStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
    REFUNDED = "refunded"

class Order(Base):
    """User orders"""
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    order_date = Column(DateTime(timezone=True), server_default=func.now())
    total_amount = Column(Float, nullable=False)
    status = Column(String(20), default="pending")  # pending, processing, shipped, delivered, cancelled, returned
    shipping_address_id = Column(Integer, ForeignKey("addresses.id"), nullable=False)
    payment_method = Column(String(50), nullable=False)
    payment_status = Column(String(20), default="pending")  # pending, paid, failed, refunded

    # Shipping tracking
    # shipping_carrier = Column(String(100), nullable=True)
    # tracking_number = Column(String(100), nullable=True)
    # estimated_delivery_date = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    user = relationship("User", back_populates="orders")
    shipping_address = relationship("Address")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
    # transactions = relationship("TransactionHistory", back_populates="order", cascade="all, delete-orphan")
    shipment = relationship("Shipment", back_populates="order", cascade="all, delete-orphan")


class OrderItem(Base):
    """Items included in an order"""
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    # subtotal = Column(Float, nullable=False)

    # Relationships
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")
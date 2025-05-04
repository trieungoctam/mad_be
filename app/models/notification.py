from datetime import datetime
from enum import Enum

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class NotificationType(str, Enum):
    PROMOTION = "promotion"
    ORDER_STATUS = "order_status"
    PRODUCT_RESTOCK = "product_restock"
    PRICE_DROP = "price_drop"
    SYSTEM = "system"


class Notification(Base):
    """User notifications"""
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    notification_type = Column(String(20), default=NotificationType.SYSTEM)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    related_entity_id = Column(Integer, nullable=True)
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User", back_populates="notifications")
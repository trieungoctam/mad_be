from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class UserSettings(Base):
    """User preferences and settings"""
    __tablename__ = "user_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    language = Column(String(10), default="en")
    theme = Column(String(20), default="light")
    notification_enabled = Column(Boolean, default=True)
    marketing_emails = Column(Boolean, default=False)
    currency = Column(String(3), default="VND")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="settings")
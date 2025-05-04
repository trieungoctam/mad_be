from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class UserPreference(Base):
    """User preferences for product recommendations"""
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    preferred_categories = Column(Text, nullable=True)  # JSON array of category IDs
    preferred_brands = Column(Text, nullable=True)  # JSON array of brand IDs
    price_range_min = Column(Float, nullable=True)
    price_range_max = Column(Float, nullable=True)
    notification_preferences = Column(Text, nullable=True)  # JSON object with notification settings

    # Relationships
    user = relationship("User", back_populates="preferences")
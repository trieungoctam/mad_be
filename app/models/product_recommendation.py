from datetime import datetime
from enum import Enum

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class RecommendationType(str, Enum):
    HISTORY_BASED = "history_based"
    PROMOTION = "promotion"
    POPULAR = "popular"
    SIMILAR = "similar"


class ProductRecommendation(Base):
    """Product recommendations for users"""
    __tablename__ = "product_recommendations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    recommendation_type = Column(String(20), default=RecommendationType.HISTORY_BASED)
    score = Column(Float, default=0)  # Relevance score
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user = relationship("User")
    product = relationship("Product")
from datetime import datetime
from sqlalchemy.sql import func

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class SearchHistory(Base):
    """User search history"""
    __tablename__ = "search_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    search_query = Column(String(255), nullable=False)
    search_date = Column(DateTime, default=func.now())
    result_count = Column(Integer, default=0)
    selected_product_id = Column(Integer, ForeignKey("products.id"), nullable=True)

    # Relationships
    user = relationship("User", back_populates="search_history")
    product = relationship("Product", back_populates="search_history")
from datetime import datetime

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class PurchaseHistory(Base):
    """User purchase history"""
    __tablename__ = "purchase_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Float, nullable=False)
    purchase_date = Column(DateTime(timezone=True), server_default=func.now())
    price = Column(Float, nullable=False)

    # Relationships
    user = relationship("User")
    product = relationship("Product")
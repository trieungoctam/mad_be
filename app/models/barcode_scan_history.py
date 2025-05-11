from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class BarcodeScanHistory(Base):
    """History of barcode scans by users"""
    __tablename__ = "barcode_scan_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    barcode = Column(String(100), nullable=False)
    scanned_at = Column(DateTime(timezone=True), default=func.now())
    # shopping_list_id = Column(Integer, ForeignKey("shopping_lists.id"), nullable=True)

    # Relationships
    user = relationship("User", back_populates="barcode_scans")
    product = relationship("Product", back_populates="barcode_scans")
    # shopping_list = relationship("ShoppingList", back_populates="barcode_scans")
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class BarcodeScanHistory(Base):
    """History of user barcode scans"""
    __tablename__ = "barcode_scan_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    barcode = Column(String(50), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    scanned_at = Column(DateTime(timezone=True), server_default=func.now())
    added_to_list_id = Column(Integer, ForeignKey("shopping_lists.id"), nullable=True)

    # Relationships
    user = relationship("User", back_populates="barcode_scans")
    product = relationship("Product", back_populates="barcode_scans")
    shopping_list = relationship("ShoppingList", back_populates="barcode_scans")
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class ShoppingList(Base):
    """User shopping lists"""
    __tablename__ = "shopping_lists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    list_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    is_completed = Column(Boolean, default=False)

    # Relationships
    user = relationship("User", back_populates="shopping_lists")
    items = relationship("ListItem", back_populates="shopping_list", cascade="all, delete-orphan")
    shared_with = relationship("SharedList", back_populates="shopping_list", cascade="all, delete-orphan")
    barcode_scans = relationship("BarcodeScanHistory", back_populates="shopping_list")


class ListItem(Base):
    """Items in shopping lists"""
    __tablename__ = "list_items"

    id = Column(Integer, primary_key=True, index=True)
    list_id = Column(Integer, ForeignKey("shopping_lists.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=True)
    quantity = Column(Float, default=1)
    unit = Column(String(20), nullable=True)
    is_purchased = Column(Boolean, default=False)
    note = Column(Text, nullable=True)
    added_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    shopping_list = relationship("ShoppingList", back_populates="items")
    product = relationship("Product")


class SharedList(Base):
    """Shopping lists shared with other users"""
    __tablename__ = "shared_lists"

    id = Column(Integer, primary_key=True, index=True)
    list_id = Column(Integer, ForeignKey("shopping_lists.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    permission_type = Column(String(20), default="view")  # view, edit
    shared_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    shopping_list = relationship("ShoppingList", back_populates="shared_with")
    user = relationship("User")
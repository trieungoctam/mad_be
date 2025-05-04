from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func

from app.db.base_class import Base

if TYPE_CHECKING:
    from .category import Category  # noqa: F401
    from .brand import Brand  # noqa: F401


class Product(Base):
    """Main product information"""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    barcode = Column(String(50), index=True, unique=True, nullable=True)
    brand_id = Column(Integer, ForeignKey("brands.id"), nullable=True, index=True)
    product_name = Column(String(200), nullable=False, index=True)
    description = Column(Text, nullable=True)
    price = Column(Integer, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    quantity = Column(Integer, default=0)

    # Relationships
    images = relationship("ProductImage", back_populates="product", cascade="all, delete-orphan")
    variants = relationship("ProductVariant", back_populates="product", cascade="all, delete-orphan")
    favorites = relationship("Favorite", back_populates="product", cascade="all, delete-orphan")
    list_items = relationship("ListItem", back_populates="product")
    reviews = relationship("ProductReview", back_populates="product", cascade="all, delete-orphan")
    cart_items = relationship("CartItem", back_populates="product")
    order_items = relationship("OrderItem", back_populates="product")
    search_history = relationship("SearchHistory", back_populates="product")
    recommendations = relationship("ProductRecommendation", back_populates="product", cascade="all, delete-orphan")
    barcode_scans = relationship("BarcodeScanHistory", back_populates="product")
    category = relationship("Category", back_populates="products")
    brand = relationship("Brand", back_populates="products")


class ProductVariant(Base):
    """Product variants for different sizes with stock quantity"""
    __tablename__ = "product_variants"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    size = Column(String(20), nullable=False)  # S, M, L, XL, 39, 40, 41...
    stock = Column(Integer, default=0)  # Số lượng tồn cho size này
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    product = relationship("Product", back_populates="variants")

class ProductImage(Base):
    """Product images"""
    __tablename__ = "product_images"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    image_url = Column(String(255), nullable=False)
    is_primary = Column(Boolean, default=False)
    upload_date = Column(DateTime, default=func.now())

    # Relationships
    product = relationship("Product", back_populates="images")
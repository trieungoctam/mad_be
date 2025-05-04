from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.types import DateTime as SQLADateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.favorite import Favorite

if TYPE_CHECKING:
    from .address import Address  # noqa: F401
    from .shopping_list import ShoppingList  # noqa: F401
    from .order import Order  # noqa: F401


class User(Base):
    """User model for authentication and personalization"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100))
    avatar_url = Column(String(255))
    phone_number = Column(String(20))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    last_login = Column(DateTime, nullable=True)

    # Relationships
    settings = relationship("UserSettings", back_populates="user", uselist=False, cascade="all, delete-orphan")
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    payments = relationship("PaymentSettings", back_populates="user", cascade="all, delete-orphan")
    cart_items = relationship("CartItem", back_populates="user")
    orders = relationship("Order", back_populates="user")
    preferences = relationship("UserPreference", back_populates="user", cascade="all, delete-orphan")
    search_history = relationship("SearchHistory", back_populates="user", cascade="all, delete-orphan")
    barcode_scans = relationship("BarcodeScanHistory", back_populates="user", cascade="all, delete-orphan")
    shopping_lists = relationship("ShoppingList", back_populates="user", cascade="all, delete-orphan")
    shared_lists = relationship("SharedList", back_populates="user")
    favorites = relationship("Favorite", back_populates="user", cascade="all, delete-orphan")
    recommendations = relationship("ProductRecommendation", back_populates="user", cascade="all, delete-orphan")
    reviews = relationship("ProductReview", back_populates="user", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
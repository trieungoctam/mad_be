from datetime import datetime
from typing import List, Optional

from app.schemas.base import BaseModel


class CartItemBase(BaseModel):
    """Base schema for cart item data"""
    product_id: int
    quantity: int = 1


class CartItemCreate(CartItemBase):
    """Schema for adding an item to cart"""
    pass


class CartItemUpdate(BaseModel):
    """Schema for updating a cart item"""
    quantity: Optional[int] = None


class CartItem(CartItemBase):
    """Schema for cart item returned from API"""
    id: int
    cart_id: int
    unit_price: float
    added_at: datetime
    product_name: Optional[str] = None
    product_image: Optional[str] = None
    subtotal: float


class CartBase(BaseModel):
    """Base schema for cart data"""
    status: str = "active"


class CartCreate(CartBase):
    """Schema for creating a new cart"""
    items: Optional[List[CartItemCreate]] = None


class Cart(CartBase):
    """Schema for cart returned from API"""
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    items: List[CartItem] = []
    total_items: int = 0
    total_amount: float = 0
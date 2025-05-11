from datetime import datetime
from typing import List, Optional

from app.models.order import OrderStatus
from app.models.transaction import TransactionStatus, TransactionType
from app.schemas.base import BaseModel, PaginatedResponse


class OrderItemBase(BaseModel):
    """Base schema for order item data"""
    product_id: int
    quantity: int = 1


class OrderItemCreate(OrderItemBase):
    """Schema for creating a new order item"""
    pass


class OrderItemUpdate(BaseModel):
    """Schema for updating an existing order item"""
    quantity: Optional[int] = None


class OrderItem(OrderItemBase):
    """Schema for order item returned from API"""
    id: int
    order_id: int
    created_at: datetime
    updated_at: datetime
    subtotal: float
    product_name: Optional[str] = None
    product_image: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True


class OrderBase(BaseModel):
    """Base schema for order data"""
    user_id: int
    total_amount: float
    status: str = OrderStatus.PENDING
    shipping_address_id: int
    payment_method: str
    shipping_carrier: Optional[str] = None
    tracking_number: Optional[str] = None


class OrderCreate(OrderBase):
    """Schema for creating a new order"""
    items: List[OrderItemCreate]


class OrderUpdate(BaseModel):
    """Schema for updating an existing order"""
    status: Optional[str] = None
    payment_status: Optional[str] = None
    shipping_carrier: Optional[str] = None
    tracking_number: Optional[str] = None
    estimated_delivery_date: Optional[datetime] = None


class Order(OrderBase):
    """Schema for order returned from API"""
    id: int
    user_id: int
    status: str
    created_at: datetime
    updated_at: datetime
    total_amount: float
    shipping_address_id: int
    payment_method: str
    payment_status: str
    shipping_carrier: Optional[str] = None
    tracking_number: Optional[str] = None
    estimated_delivery_date: Optional[datetime] = None
    order_date: datetime
    items: List[OrderItem] = []
    shipping_address: Optional[dict] = None
    tracking_url: Optional[str] = None

    class Config:
        from_attributes = True

class OrderIn(BaseModel):
    """Schema for order input"""
    user_id: int
    idempotency_key: str
    total_amount: float
    status: str = OrderStatus.PENDING
    shipping_address_id: int
    items: List[OrderItemBase]
    cvv: int


class OrderPaginated(PaginatedResponse):
    """Schema for paginated orders"""
    data: List[Order]


class TransactionCreate(BaseModel):
    """Schema for creating a new transaction"""
    order_id: int
    transaction_type: str = TransactionType.PAYMENT
    amount: float
    payment_method: str
    status: str = TransactionStatus.PENDING


class Transaction(BaseModel):
    """Schema for transaction returned from API"""
    id: int
    order_id: int
    created_at: datetime
    updated_at: datetime
    transaction_type: str
    amount: float
    payment_method: str
    status: str
    transaction_date: datetime

    class Config:
        from_attributes = True
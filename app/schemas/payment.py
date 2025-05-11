from datetime import datetime
from typing import Dict, List, Optional

from app.models.transaction import TransactionStatus, TransactionType
from app.schemas.base import BaseModel, PaginatedResponse


class PaymentSettingBase(BaseModel):
    """Base schema for payment setting data"""
    payment_method: str
    payment_details: str  # Encrypted payment details
    is_default: bool = False


class PaymentSettingCreate(PaymentSettingBase):
    """Schema for creating a new payment setting"""
    pass


class PaymentSettingUpdate(BaseModel):
    """Schema for updating an existing payment setting"""
    payment_method: Optional[str] = None
    payment_details: Optional[str] = None
    is_default: Optional[bool] = None


class PaymentSetting(PaymentSettingBase):
    """Schema for payment setting returned from API"""
    id: int
    user_id: int
    created_at: datetime


class TransactionBase(BaseModel):
    """Base schema for transaction data"""
    order_id: int
    transaction_type: TransactionType = TransactionType.PAYMENT
    amount: float
    payment_method: str
    payment_details: Optional[str] = None


class TransactionCreate(TransactionBase):
    """Schema for creating a new transaction"""
    pass


class Transaction(TransactionBase):
    """Schema for transaction returned from API"""
    id: int
    transaction_date: datetime
    status: TransactionStatus


class BankCardDetails(BaseModel):
    """Schema for bank card payment details"""
    card_number: str
    card_holder_name: str
    expiry_month: str
    expiry_year: str
    cvv: str
    class Config:
        schema_extra = {
            "example": {
                "card_number": "4111111111111111",
                "card_holder_name": "NGUYEN VAN A",
                "expiry_month": "12",
                "expiry_year": "2025",
                "cvv": "123"
            }
        }


class PaymentRequest(BaseModel):
    """Schema for payment request"""
    order_id: int
    payment_method: str
    payment_details: Dict[str, str]  # Gateway-specific payment details
    payment_setting_id: Optional[int] = None  # ID of saved payment setting (if using saved method)


class PaymentResponse(BaseModel):
    """Schema for payment response"""
    success: bool
    message: str
    payment_status: str

    class Config:
        schema_extra = {
            "example": {
                "success": True,
                "message": "Payment successful",
                "payment_status": "completed",
            }
        }


class TransactionPaginated(PaginatedResponse[List[Transaction]]):
    """Schema for paginated transactions"""
    pass

class PaymentSchema (BaseModel):
    """Schema for payment details"""
    user_id: int
    card_id: int
    order_id: int
    amount: float
    status: str
    created_at: datetime
    updated_at: datetime


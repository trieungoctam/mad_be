from typing import Optional, Literal
from enum import Enum

from app.schemas.base import BaseModel


# Define AddressType as an Enum for use in the schemas
class AddressType(str, Enum):
    SHIPPING = "shipping"
    BILLING = "billing"


class AddressBase(BaseModel):
    """Base schema for address data"""
    address_type: AddressType = AddressType.SHIPPING
    street: str
    city: str
    district: str
    postal_code: Optional[str] = None
    country: str
    is_default: bool = False


class AddressCreate(AddressBase):
    """Schema for creating a new address"""
    pass


class AddressUpdate(BaseModel):
    """Schema for updating an existing address"""
    address_type: Optional[AddressType] = None
    street: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    is_default: Optional[bool] = None


class Address(AddressBase):
    """Schema for address information returned from API"""
    id: int
    user_id: int
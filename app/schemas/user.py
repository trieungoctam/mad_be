from datetime import datetime
from typing import Optional

from pydantic import EmailStr, Field, BaseModel


class UserBase(BaseModel):
    """Base schema for user data"""
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    phone_number: Optional[str] = None


class UserCreate(BaseModel):
    """Schema for creating a new user"""
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr = Field(..., format="email")
    full_name: Optional[str] = Field(None, min_length=3, max_length=100)
    avatar_url: Optional[str] = Field(None, format="uri")
    phone_number: Optional[str] = Field(None, min_length=10, max_length=15)
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    """Schema for updating an existing user"""
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    phone_number: Optional[str] = None
    password: Optional[str] = Field(None, min_length=8)


class User(UserBase):
    """Schema for user information returned from API"""
    id: int
    is_active: bool
    created_at: datetime
    last_login: Optional[datetime] = None


class UserLogin(BaseModel):
    """Schema for user login credentials"""
    username: str
    password: str


class Token(BaseModel):
    """Schema for authentication token"""
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """Schema for token payload data"""
    sub: str  # User ID
    exp: datetime  # Expiration time


class ForgotPassword(BaseModel):
    """Schema for forgot password"""
    email: EmailStr
    new_password: Optional[str] = Field(None, min_length=8)
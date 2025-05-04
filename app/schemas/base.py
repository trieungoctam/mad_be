from datetime import datetime
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel, EmailStr, Field

T = TypeVar('T')

class PaginationParams(BaseModel):
    """Common pagination parameters"""
    page: int = Field(1, ge=1, description="Current page number (1-indexed)")
    limit: int = Field(10, ge=1, le=100, description="Items per page")

class PaginatedResponse(BaseModel, Generic[T]):
    """Base paginated response schema"""
    page: int
    limit: int
    total: int
    pages: int
    data: T

    class Config:
        from_attributes = True


class BaseAPIResponse(BaseModel):
    """Base API response schema"""
    success: bool = True
    message: str = "Operation completed successfully"
    data: Optional[Any] = None
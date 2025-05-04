from datetime import datetime
from typing import List, Optional, Any

from app.schemas.base import BaseModel, PaginatedResponse


class BarcodeScanBase(BaseModel):
    """Base schema for barcode scan data"""
    barcode: str


class BarcodeScanCreate(BarcodeScanBase):
    """Schema for recording a new barcode scan"""
    product_id: Optional[int] = None
    added_to_list_id: Optional[int] = None


class BarcodeScan(BarcodeScanBase):
    """Schema for barcode scan returned from API"""
    id: int
    user_id: int
    product_id: Optional[int] = None
    scanned_at: datetime
    added_to_list_id: Optional[int] = None
    product_name: Optional[str] = None
    product_image: Optional[str] = None


class BarcodeScanResult(BaseModel):
    """Barcode scan result schema"""
    barcode: str
    product_found: bool
    product: Optional[Any] = None
    message: Optional[str] = None
    error: Optional[str] = None


class BarcodeScanHistoryPaginated(PaginatedResponse):
    """Schema for paginated barcode scan history"""
    data: List[BarcodeScan]
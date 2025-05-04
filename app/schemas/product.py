from datetime import datetime
from typing import Dict, List, Optional, Union

from app.schemas.base import BaseModel, PaginatedResponse


# class ProductDetailBase(BaseModel):
#     """Base schema for product detail data"""
#     attribute_type: str
#     attribute_key: str
#     data_type: str
#     value_string: Optional[str] = None
#     value_number: Optional[float] = None
#     value_date: Optional[datetime] = None
#     unit: Optional[str] = None


# class ProductDetailCreate(ProductDetailBase):
#     """Schema for adding a new product detail"""
#     pass


# class ProductDetailUpdate(BaseModel):
#     """Schema for updating an existing product detail"""
#     attribute_type: Optional[str] = None
#     attribute_key: Optional[str] = None
#     data_type: Optional[str] = None
#     value_string: Optional[str] = None
#     value_number: Optional[float] = None
#     value_date: Optional[datetime] = None
#     unit: Optional[str] = None


# class ProductDetail(ProductDetailBase):
#     """Schema for product detail returned from API"""
#     id: int
#     product_id: int
#     value_string: Optional[str] = None
#     value_number: Optional[float] = None
#     value_date: Optional[datetime] = None
#     unit: Optional[str] = None
#     created_at: datetime
#     updated_at: datetime

#     class Config:
#         from_attributes = True


class ProductBase(BaseModel):
    """Base schema for product data"""
    barcode: Optional[str] = None
    product_name: str
    description: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None
    brand_id: Optional[int] = None


class ProductCreate(ProductBase):
    """Schema for creating a new product"""
    pass


class ProductUpdate(BaseModel):
    """Schema for updating an existing product"""
    barcode: Optional[str] = None
    product_name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    category_id: Optional[int] = None
    brand_id: Optional[int] = None


class Product(ProductBase):
    """Schema for product returned from API"""
    id: int
    created_at: datetime
    updated_at: datetime
    category_name: Optional[str] = None
    brand_name: Optional[str] = None
    images: Optional[list[str]] = None
    quantity: Optional[int] = None
    review_count: Optional[int] = None
    average_rating: Optional[float] = None

    class Config:
        from_attributes = True


class ProductCompare(BaseModel):
    """Schema for product comparison"""
    id: int
    product_name: str
    image_url: Optional[str] = None
    prices: List[int]
    lowest_price: float
    highest_price: float


class ProductPaginated(PaginatedResponse[List[Product]]):
    """Schema for paginated products"""
    pass


class CategoryBase(BaseModel):
    """Base schema for category data"""
    name: str
    description: Optional[str] = None
    parent_id: Optional[int] = None
    image_url: Optional[str] = None


class CategoryCreate(CategoryBase):
    """Schema for creating a new category"""
    pass


class CategoryUpdate(BaseModel):
    """Schema for updating an existing category"""
    name: Optional[str] = None
    description: Optional[str] = None
    parent_id: Optional[int] = None
    image_url: Optional[str] = None


class Category(CategoryBase):
    """Schema for category returned from API"""
    id: int
    created_at: datetime
    updated_at: datetime
    products_count: Optional[int] = None

    class Config:
        from_attributes = True


class BrandBase(BaseModel):
    """Base schema for brand data"""
    name: str
    description: Optional[str] = None
    logo_url: Optional[str] = None
    website: Optional[str] = None


class BrandCreate(BrandBase):
    """Schema for creating a new brand"""
    pass


class BrandUpdate(BaseModel):
    """Schema for updating an existing brand"""
    name: Optional[str] = None
    description: Optional[str] = None
    logo_url: Optional[str] = None
    website: Optional[str] = None


class Brand(BrandBase):
    """Schema for brand returned from API"""
    id: int
    created_at: datetime
    updated_at: datetime
    products_count: Optional[int] = None

    class Config:
        from_attributes = True


class ProductVariantBase(BaseModel):
    """Base schema for product variant data"""
    product_id: int
    size: str
    stock: int = 0


class ProductVariantCreate(ProductVariantBase):
    """Schema for creating a new product variant"""
    pass


class ProductVariantUpdate(BaseModel):
    """Schema for updating an existing product variant"""
    size: Optional[str] = None
    stock: Optional[int] = None


class ProductVariant(ProductVariantBase):
    """Schema for product variant returned from API"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ProductImageBase(BaseModel):
    """Base schema for product image data"""
    image_url: str
    is_primary: bool = False


class ProductImageCreate(ProductImageBase):
    """Schema for adding a new product image"""
    product_id: int


class ProductImage(ProductImageBase):
    """Schema for product image returned from API"""
    id: int
    product_id: int
    upload_date: datetime

    class Config:
        from_attributes = True
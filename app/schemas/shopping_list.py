from datetime import datetime
from typing import List, Optional

from app.schemas.base import BaseModel, PaginatedResponse


class ListItemBase(BaseModel):
    """Base schema for shopping list item data"""
    product_id: Optional[int] = None
    quantity: int = 1
    unit: Optional[str] = None
    note: Optional[str] = None
    is_purchased: bool = False


class ListItemCreate(ListItemBase):
    """Schema for creating a new shopping list item"""
    pass


class ListItemUpdate(BaseModel):
    """Schema for updating an existing shopping list item"""
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    unit: Optional[str] = None
    note: Optional[str] = None
    is_purchased: Optional[bool] = None


class ListItem(ListItemBase):
    """Schema for shopping list item returned from API"""
    id: int
    list_id: int
    added_at: datetime
    product_name: Optional[str] = None
    product_image: Optional[str] = None
    product_price: Optional[float] = None


class ShoppingListBase(BaseModel):
    """Base schema for shopping list data"""
    list_name: str
    description: Optional[str] = None
    is_completed: bool = False


class ShoppingListCreate(ShoppingListBase):
    """Schema for creating a new shopping list"""
    items: Optional[List[ListItemCreate]] = None


class ShoppingListUpdate(BaseModel):
    """Schema for updating an existing shopping list"""
    list_name: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class ShoppingList(ShoppingListBase):
    """Schema for shopping list returned from API"""
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    items: List[ListItem] = []
    items_count: int = 0
    purchased_count: int = 0


class SharedListBase(BaseModel):
    """Base schema for shared shopping list data"""
    permission_type: str = "view"


class SharedListCreate(SharedListBase):
    """Schema for sharing a shopping list with user"""
    user_id: int
    list_id: int


class SharedList(SharedListBase):
    """Schema for shared shopping list returned from API"""
    id: int
    list_id: int
    user_id: int
    shared_at: datetime
    user_name: str


class ShoppingListPaginated(PaginatedResponse):
    """Schema for paginated shopping lists"""
    data: List[ShoppingList]
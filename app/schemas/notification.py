from datetime import datetime
from typing import List, Optional

from app.models.notification import NotificationType
from app.schemas.base import BaseModel, PaginatedResponse


class NotificationBase(BaseModel):
    """Base schema for notification data"""
    notification_type: NotificationType = NotificationType.SYSTEM
    title: str
    content: str
    related_entity_id: Optional[int] = None
    is_read: bool = False


class NotificationCreate(NotificationBase):
    """Schema for creating a new notification"""
    user_id: int


class NotificationUpdate(BaseModel):
    """Schema for updating an existing notification"""
    is_read: Optional[bool] = None


class Notification(NotificationBase):
    """Schema for notification returned from API"""
    id: int
    user_id: int
    created_at: datetime


class NotificationPaginated(PaginatedResponse):
    """Schema for paginated notifications"""
    data: List[Notification]


class NotificationSettings(BaseModel):
    """Schema for notification settings"""
    order_status: bool = True
    promotions: bool = True
    price_drops: bool = True
    product_restocks: bool = True
    system_messages: bool = True
    email_notifications: bool = True
    push_notifications: bool = True
from typing import Any, Dict

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.deps import get_current_active_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.base import PaginationParams
from app.schemas.notification import (
    Notification,
    NotificationPaginated,
)
from app.services.notification import (
    get_notification,
    get_user_notifications,
    mark_all_notifications_as_read,
    mark_notification_as_read,
    count_unread_notifications,
)

router = APIRouter()


@router.get("/", response_model=NotificationPaginated)
async def read_notifications(
    pagination: PaginationParams = Depends(),
    unread_only: bool = False,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get user's notifications with pagination
    """
    return await get_user_notifications(
        db=db, user_id=current_user.id, limit=pagination.limit, offset=pagination.offset, unread_only=unread_only
    )


@router.get("/count", response_model=Dict[str, int])
async def get_unread_count(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get count of unread notifications
    """
    count = await count_unread_notifications(db=db, user_id=current_user.id)
    return {"count": count}


@router.put("/{notification_id}", response_model=Notification)
async def mark_as_read(
    notification_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Mark a notification as read
    """
    notification = await get_notification(db=db, notification_id=notification_id)

    # Check if notification exists and belongs to current user
    if not notification or notification.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Notification not found",
        )

    return await mark_notification_as_read(db=db, notification=notification)


@router.put("/read-all", response_model=Dict[str, str])
async def mark_all_read(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Mark all notifications as read
    """
    await mark_all_notifications_as_read(db=db, user_id=current_user.id)
    return {"message": "All notifications marked as read"}


# @router.get("/settings", response_model=NotificationSettings)
# async def read_notification_settings(
#     db: AsyncSession = Depends(get_db),
#     current_user: User = Depends(get_current_active_user),
# ) -> Any:
#     """
#     Get user's notification settings
#     """
#     return await get_notification_settings(db=db, user_id=current_user.id)


# @router.put("/settings", response_model=NotificationSettings)
# async def update_settings(
#     settings: NotificationSettings,
#     db: AsyncSession = Depends(get_db),
#     current_user: User = Depends(get_current_active_user),
# ) -> Any:
#     """
#     Update notification settings
#     """
#     return await update_notification_settings(db=db, user_id=current_user.id, settings=settings)
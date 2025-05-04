from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete, desc

from app.models.notification import Notification
from app.schemas.notification import NotificationCreate, NotificationUpdate


async def create_notification(
    db: AsyncSession,
    user_id: int,
    notification_type: str,
    content: str,
    related_entity_id: Optional[int] = None
) -> Notification:
    """
    Create a new notification for a user
    """
    db_notification = Notification(
        user_id=user_id,
        notification_type=notification_type,
        content=content,
        related_entity_id=related_entity_id,
        is_read=False
    )
    db.add(db_notification)
    await db.commit()
    await db.refresh(db_notification)

    return db_notification


async def get_notification(db: AsyncSession, notification_id: int) -> Optional[Notification]:
    """
    Get a notification by ID
    """
    result = await db.execute(select(Notification).where(Notification.id == notification_id))
    return result.scalars().first()


async def get_user_notifications(
    db: AsyncSession,
    user_id: int,
    limit: int = 20,
    offset: int = 0,
    unread_only: bool = False
) -> List[Notification]:
    """
    Get notifications for a user, optionally filtered by read status
    """
    query = select(Notification).where(Notification.user_id == user_id)

    if unread_only:
        query = query.where(Notification.is_read == False)

    query = query.order_by(desc(Notification.created_at)).limit(limit).offset(offset)

    result = await db.execute(query)
    return result.scalars().all()


async def mark_notification_as_read(db: AsyncSession, notification: Notification) -> Notification:
    """
    Mark a notification as read
    """
    if not notification.is_read:
        notification.is_read = True
        await db.commit()
        await db.refresh(notification)

    return notification


async def mark_all_notifications_as_read(db: AsyncSession, user_id: int) -> int:
    """
    Mark all notifications for a user as read
    Returns the number of updated notifications
    """
    result = await db.execute(
        select(Notification)
        .where(Notification.user_id == user_id)
        .where(Notification.is_read == False)
    )
    unread_notifications = result.scalars().all()

    for notification in unread_notifications:
        notification.is_read = True

    await db.commit()

    return len(unread_notifications)


async def delete_notification(db: AsyncSession, notification: Notification) -> None:
    """
    Delete a notification
    """
    await db.delete(notification)
    await db.commit()


async def delete_old_notifications(db: AsyncSession, user_id: int, days: int = 30) -> int:
    """
    Delete notifications older than the specified number of days
    Returns the number of deleted notifications
    """
    from datetime import datetime, timedelta

    cutoff_date = datetime.utcnow() - timedelta(days=days)

    result = await db.execute(
        select(Notification)
        .where(Notification.user_id == user_id)
        .where(Notification.created_at < cutoff_date)
    )
    old_notifications = result.scalars().all()

    for notification in old_notifications:
        await db.delete(notification)

    await db.commit()

    return len(old_notifications)


async def count_unread_notifications(db: AsyncSession, user_id: int) -> int:
    """
    Count the number of unread notifications for a user
    """
    result = await db.execute(
        select(Notification)
        .where(Notification.user_id == user_id)
        .where(Notification.is_read == False)
    )
    unread_notifications = result.scalars().all()

    return len(unread_notifications)
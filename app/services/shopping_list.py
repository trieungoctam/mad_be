from typing import List, Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from sqlalchemy.sql import func

from app.models.shopping_list import ShoppingList, ListItem, SharedList
from app.models.user import User
from app.schemas.shopping_list import (
    ShoppingListCreate, ShoppingListUpdate,
    ListItemCreate, ListItemUpdate,
    SharedListCreate
)


async def create_shopping_list(
    db: AsyncSession,
    user_id: int,
    shopping_list_in: ShoppingListCreate
) -> ShoppingList:
    """
    Create a new shopping list for the user
    """
    db_list = ShoppingList(
        user_id=user_id,
        list_name=shopping_list_in.list_name,
        description=shopping_list_in.description
    )

    db.add(db_list)
    await db.commit()
    await db.refresh(db_list)

    return db_list


async def get_shopping_list(db: AsyncSession, list_id: int) -> Optional[ShoppingList]:
    """
    Get a shopping list by ID
    """
    result = await db.execute(select(ShoppingList).where(ShoppingList.id == list_id))
    return result.scalars().first()


async def get_user_shopping_lists(db: AsyncSession, user_id: int) -> List[ShoppingList]:
    """
    Get all shopping lists for a user
    """
    result = await db.execute(
        select(ShoppingList)
        .where(ShoppingList.user_id == user_id)
    )
    return result.scalars().all()


async def get_shopping_lists(
    db: AsyncSession,
    user_id: int,
    pagination: Any,
    is_completed: Optional[bool] = None
) -> Dict[str, Any]:
    """
    Get paginated shopping lists for a user with optional filtering
    """
    # Start with base query
    query = select(ShoppingList).where(ShoppingList.user_id == user_id)

    # Apply filter if provided
    if is_completed is not None:
        query = query.where(ShoppingList.is_completed == is_completed)

    # Get total count for pagination
    count_query = select(func.count()).select_from(query.subquery())
    total = await db.scalar(count_query) or 0

    # Apply pagination
    skip = (pagination.page - 1) * pagination.limit
    query = query.offset(skip).limit(pagination.limit)

    # Execute query
    result = await db.execute(query)
    shopping_lists = result.scalars().all()

    # Calculate total pages
    total_pages = (total + pagination.limit - 1) // pagination.limit

    # Return paginated result
    return {
        "page": pagination.page,
        "limit": pagination.limit,
        "total": total,
        "pages": total_pages,
        "data": shopping_lists
    }


async def get_shared_shopping_lists(db: AsyncSession, user_id: int) -> List[ShoppingList]:
    """
    Get all shopping lists shared with a user
    """
    result = await db.execute(
        select(ShoppingList)
        .join(SharedList, SharedList.list_id == ShoppingList.id)
        .where(SharedList.user_id == user_id)
    )
    return result.scalars().all()


async def update_shopping_list(
    db: AsyncSession, shopping_list: ShoppingList, shopping_list_update: ShoppingListUpdate, user_id: int
) -> ShoppingList:
    """
    Update a shopping list
    """
    update_data = shopping_list_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(shopping_list, field, value)

    await db.commit()
    await db.refresh(shopping_list)

    return shopping_list


async def delete_shopping_list(db: AsyncSession, shopping_list: ShoppingList, user_id: int) -> None:
    """
    Delete a shopping list
    """
    list_name = shopping_list.list_name
    list_id = shopping_list.id

    await db.execute(delete(ShoppingList).where(ShoppingList.id == list_id))
    await db.commit()


# List Item Methods
async def add_item_to_list(db: AsyncSession, list_item: ListItemCreate, user_id: int) -> ListItem:
    """
    Add an item to a shopping list
    """
    db_list_item = ListItem(
        list_id=list_item.list_id,
        product_id=list_item.product_id,
        quantity=list_item.quantity,
        unit=list_item.unit,
        is_purchased=False,
        note=list_item.note
    )
    db.add(db_list_item)
    await db.commit()
    await db.refresh(db_list_item)

    return db_list_item


async def get_list_items(db: AsyncSession, list_id: int) -> List[ListItem]:
    """
    Get all items in a shopping list
    """
    result = await db.execute(
        select(ListItem)
        .where(ListItem.list_id == list_id)
        .order_by(ListItem.added_at.desc())
    )
    return result.scalars().all()


async def update_list_item(
    db: AsyncSession, list_item: ListItem, list_item_update: ListItemUpdate, user_id: int
) -> ListItem:
    """
    Update a shopping list item
    """
    update_data = list_item_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(list_item, field, value)

    await db.commit()
    await db.refresh(list_item)

    return list_item


async def delete_list_item(db: AsyncSession, list_item: ListItem, user_id: int) -> None:
    """
    Delete a shopping list item
    """
    item_id = list_item.id

    await db.execute(delete(ListItem).where(ListItem.id == item_id))
    await db.commit()


# Shared List Methods
async def share_shopping_list(db: AsyncSession, shared_list: SharedListCreate, user_id: int) -> SharedList:
    """
    Share a shopping list with another user
    """
    db_shared_list = SharedList(
        list_id=shared_list.list_id,
        user_id=shared_list.user_id,
        permission_type=shared_list.permission_type
    )
    db.add(db_shared_list)
    await db.commit()
    await db.refresh(db_shared_list)

    return db_shared_list


async def remove_shopping_list_share(db: AsyncSession, share_id: int, user_id: int) -> None:
    """
    Remove a user's access to a shared shopping list
    """
    await db.execute(delete(SharedList).where(SharedList.id == share_id))
    await db.commit()
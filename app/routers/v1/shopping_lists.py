from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.deps import get_current_active_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.base import PaginationParams
from app.schemas.shopping_list import (
    ListItem,
    ListItemCreate,
    ListItemUpdate,
    SharedList,
    SharedListCreate,
    ShoppingList,
    ShoppingListCreate,
    ShoppingListPaginated,
    ShoppingListUpdate,
)
from app.services.shopping_list import (
    add_item_to_list,
    create_shopping_list,
    delete_list_item,
    delete_shopping_list,
    get_shopping_list,
    get_shopping_lists,
    share_shopping_list,
    update_list_item,
    update_shopping_list,
)

router = APIRouter()


@router.get("/", response_model=ShoppingListPaginated)
async def read_shopping_lists(
    pagination: PaginationParams = Depends(),
    is_completed: bool = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get all current user's shopping lists with pagination
    """
    return await get_shopping_lists(
        db=db, user_id=current_user.id, pagination=pagination, is_completed=is_completed
    )


@router.post("/", response_model=ShoppingList, status_code=status.HTTP_201_CREATED)
async def create_list(
    list_in: ShoppingListCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Create new shopping list
    """
    return await create_shopping_list(db=db, user_id=current_user.id, list_in=list_in)


@router.get("/{list_id}", response_model=ShoppingList)
async def read_shopping_list(
    list_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get a specific shopping list by ID
    """
    shopping_list = await get_shopping_list(db=db, list_id=list_id, user_id=current_user.id)
    if not shopping_list:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shopping list not found",
        )
    return shopping_list


@router.put("/{list_id}", response_model=ShoppingList)
async def update_list(
    list_id: int,
    list_in: ShoppingListUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Update a shopping list
    """
    return await update_shopping_list(
        db=db, list_id=list_id, user_id=current_user.id, list_in=list_in
    )


@router.delete("/{list_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_list(
    list_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> None:
    """
    Delete a shopping list
    """
    await delete_shopping_list(db=db, list_id=list_id, user_id=current_user.id)


# List items endpoints
@router.post("/{list_id}/items", response_model=ListItem, status_code=status.HTTP_201_CREATED)
async def create_list_item(
    list_id: int,
    item_in: ListItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Add item to shopping list
    """
    return await add_item_to_list(
        db=db, list_id=list_id, user_id=current_user.id, item_in=item_in
    )


@router.put("/{list_id}/items/{item_id}", response_model=ListItem)
async def update_item(
    list_id: int,
    item_id: int,
    item_in: ListItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Update a list item
    """
    return await update_list_item(
        db=db, list_id=list_id, item_id=item_id, user_id=current_user.id, item_in=item_in
    )


@router.delete("/{list_id}/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(
    list_id: int,
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> None:
    """
    Delete an item from shopping list
    """
    await delete_list_item(db=db, list_id=list_id, item_id=item_id, user_id=current_user.id)


# Sharing endpoints
@router.post("/{list_id}/share", response_model=SharedList, status_code=status.HTTP_201_CREATED)
async def share_list(
    list_id: int,
    share_in: SharedListCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Share a shopping list with another user
    """
    return await share_shopping_list(
        db=db, list_id=list_id, owner_id=current_user.id, share_in=share_in
    )
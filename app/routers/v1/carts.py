from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.deps import get_current_active_user, get_optional_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.cart import Cart, CartCreate, CartItemCreate, CartItemUpdate
from app.services.cart import (
    add_item_to_cart,
    create_cart,
    delete_cart,
    delete_cart_item,
    get_active_cart,
    update_cart_item,
    get_cart_item,
    get_cart_items,
    update_item_quantity,
    remove_item_from_cart,
)

router = APIRouter()


@router.get("/", response_model=None)
async def read_active_cart(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get current user's active cart
    """
    cart = await get_active_cart(db=db, user_id=current_user.id)
    items = await get_cart_items(db, cart.id)
    if not cart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Active cart not found",
        )

    return {"cart": cart, "items": items}

@router.post("/", response_model=None, status_code=status.HTTP_201_CREATED)
async def create_new_cart(
    cart_in: CartCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Create a new cart for current user
    """
    # Check if user already has an active cart
    existing_cart = await get_active_cart(db=db, user_id=current_user.id)
    if existing_cart:
        return existing_cart

    return await create_cart(db=db, cart_in=cart_in, user_id=current_user.id)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_active_cart(
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_current_user),
) -> None:
    """
    Delete current user's active cart
    """
    # Use hardcoded user_id if not authenticated
    user_id = current_user.id if current_user else 1

    cart = await get_active_cart(db=db, user_id=user_id)
    if not cart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No active cart found",
        )

    await delete_cart(db=db, cart_id=cart.id, user_id=user_id)


@router.post("/items", response_model=None, status_code=status.HTTP_201_CREATED)
async def add_to_cart(
    item_in: CartItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_current_user),
) -> Any:
    """
    Add item to cart
    """
    # Use hardcoded user_id if not authenticated
    user_id = current_user.id if current_user else 1

    # Get active cart or create if doesn't exist
    cart = await get_active_cart(db=db, user_id=user_id)
    if not cart:
        cart = await create_cart(
            db=db,
            cart_in=CartCreate(status="active", user_id=user_id),
            user_id=user_id
        )

    return await add_item_to_cart(db=db, cart_id=cart.id, item_in=item_in)


@router.put("/items/{item_id}", response_model=None)
async def update_cart_item(
    item_id: int,
    item_in: CartItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Update quantity of a cart item
    """
    cart = await get_active_cart(db=db, user_id=current_user.id)
    if not cart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No active cart found",
        )

    # Verify the item belongs to user's cart
    item = await get_cart_item(db=db, item_id=item_id)

    print(item)

    if not item or item.cart_id != cart.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart item not found",
        )

    return await update_item_quantity(db=db, item_id=item_id, quantity=item_in.quantity)


@router.delete("/items/{item_id}", response_model=None)
async def remove_cart_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Remove item from cart
    """
    cart = await get_active_cart(db=db, user_id=current_user.id)
    if not cart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No active cart found",
        )

    # Verify the item belongs to user's cart
    item = await get_cart_item(db=db, item_id=item_id)
    if not item or item.cart_id != cart.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart item not found",
        )

    await remove_item_from_cart(db=db, item_id=item_id)
    return await get_active_cart(db=db, user_id=current_user.id)
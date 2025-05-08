from typing import Any, Optional, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.deps import get_current_active_user, get_optional_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.cart import Cart, CartCreate, CartItemCreate, CartItemUpdate, CartItemCreateList
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


@router.get("/")
async def read_active_cart(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get current user's active cart
    """
    cart = await get_active_cart(db=db, user_id=current_user.id)

    print("GETTING CART ITEMS")
    items = await get_cart_items(db, cart.id)
    if not cart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Active cart not found",
        )

    cart_items = []
    for item in items:
        cart_items.append({
            "id": item.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "unit_price": item.unit_price,
        })

    cart_dict = {
        "id": cart.id,
        "user_id": cart.user_id,
        "status": cart.status,
        "items": cart_items
    }

    return cart_dict

@router.post("/", status_code=status.HTTP_201_CREATED)
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

    print("EXISTING CART")

    if existing_cart:
        await delete_cart(db=db, cart_id=existing_cart.id, user_id=current_user.id)

    cart = await create_cart(db=db, cart_in=cart_in, user_id=current_user.id)

    cart_dict = {
        "id": cart.id,
        "user_id": cart.user_id,
        "status": cart.status,
        "items": []
    }
    items = cart_in.items
    for item in items:
        await add_item_to_cart(db=db, cart_id=cart.id, item_in=item)

    items = await get_cart_items(db, cart.id)
    for item in items:
        cart_dict["items"].append({
            "id": item.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "unit_price": item.unit_price,
        })

    return cart_dict

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_active_cart(
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_active_user),
) -> None:
    """
    Delete current user's active cart
    """
    # Use hardcoded user_id if not authenticated
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )
    user_id = current_user.id

    cart = await get_active_cart(db=db, user_id=user_id)
    if not cart:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No active cart found",
        )

    await delete_cart(db=db, cart_id=cart.id, user_id=user_id)
    return {"message": "Cart deleted successfully"}

@router.post("/items", status_code=status.HTTP_201_CREATED)
async def add_to_cart(
    item_in: CartItemCreateList,
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_active_user),
) -> Any:
    """
    Add item to cart
    """
    # Use hardcoded user_id if not authenticated
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )
    user_id = current_user.id

    # Get active cart or create if doesn't exist
    cart = await get_active_cart(db=db, user_id=user_id)
    if not cart:
        cart = await create_cart(
            db=db,
            cart_in=CartCreate(status="active", user_id=user_id),
            user_id=user_id
        )
    items = item_in.items
    for item in items:
        await add_item_to_cart(db=db, cart_id=cart.id, item_in=item)

    cart_dict = {
        "id": cart.id,
        "user_id": cart.user_id,
        "status": cart.status,
        "items": []
    }
    items = await get_cart_items(db, cart.id)
    for item in items:
        cart_dict["items"].append({
            "id": item.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "unit_price": item.unit_price,
        })
    return cart_dict


@router.put("/items/{item_id}")
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

    if not item or item.cart_id != cart.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cart item not found",
        )

    await update_item_quantity(db=db, item_id=item_id, quantity=item_in.quantity)

    cart_dict = {
        "id": cart.id,
        "user_id": cart.user_id,
        "status": cart.status,
        "items": []
    }
    items = await get_cart_items(db, cart.id)
    for item in items:
        cart_dict["items"].append({
            "id": item.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "unit_price": item.unit_price,
        })
    return cart_dict


@router.delete("/items/{item_id}")
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
    cart_dict = {
        "id": cart.id,
        "user_id": cart.user_id,
        "status": cart.status,
        "items": []
    }
    items = await get_cart_items(db, cart.id)
    for item in items:
        cart_dict["items"].append({
            "id": item.id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "unit_price": item.unit_price,
        })
    return cart_dict

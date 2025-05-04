from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.deps import get_current_active_user, get_current_superuser
from app.core.security import get_password_hash
from app.db.session import get_db
from app.models.user import User
from app.schemas.address import Address, AddressCreate, AddressUpdate
from app.schemas.user import User as UserSchema, UserUpdate
from app.services.user import (
    create_user_address,
    get_user_addresses,
    get_user_by_id,
    get_users,
    update_user,
    update_user_address,
    delete_user_address,
)

router = APIRouter()


@router.get("/me", response_model=UserSchema)
async def read_user_me(
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get current user information
    """
    return current_user


@router.put("/me", response_model=UserSchema)
async def update_user_me(
    user_in: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Update current user information
    """
    return await update_user(db=db, user_id=current_user.id, user_in=user_in)


@router.get("/", response_model=List[UserSchema], dependencies=[Depends(get_current_superuser)])
async def read_users(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
) -> Any:
    """
    Retrieve users (admin only)
    """
    return await get_users(db=db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserSchema)
async def read_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get user by ID
    """
    if user_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions to access other user data",
        )

    user = await get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


# Address endpoints
@router.get("/me/addresses", response_model=List[Address])
async def read_user_addresses(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Get current user's addresses
    """
    return await get_user_addresses(db=db, user_id=current_user.id)


@router.post("/me/addresses", response_model=Address, status_code=status.HTTP_201_CREATED)
async def create_address(
    address_in: AddressCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Create a new address for current user
    """
    return await create_user_address(db=db, user_id=current_user.id, address_in=address_in)


@router.put("/me/addresses/{address_id}", response_model=Address)
async def update_address(
    address_id: int,
    address_in: AddressUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> Any:
    """
    Update an address
    """
    return await update_user_address(
        db=db, user_id=current_user.id, address_id=address_id, address_in=address_in
    )


# @router.delete("/me/addresses/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_address(
#     address_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user: User = Depends(get_current_active_user),
# ) -> None:
#     """
#     Delete an address
#     """
#     await delete_user_address(db=db, user_id=current_user.id, address_id=address_id)
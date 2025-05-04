from typing import List, Optional

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_password_hash
from app.models.address import Address
from app.models.user import User
from app.schemas.address import AddressCreate, AddressUpdate
from app.schemas.user import UserUpdate


async def get_users(
    db: AsyncSession, skip: int = 0, limit: int = 100
) -> List[User]:
    """
    Get all users with pagination
    """
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()


async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
    """
    Get user by ID
    """
    return await db.get(User, user_id)


async def get_user_by_username(db: AsyncSession, username: str) -> Optional[User]:
    """
    Get user by username
    """
    result = await db.execute(select(User).where(User.username == username))
    return result.scalars().first()


async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    """
    Get user by email
    """
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()


async def update_user(
    db: AsyncSession, user_id: int, user_in: UserUpdate
) -> User:
    """
    Update user information
    """
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    # Update user attributes
    if user_in.username is not None:
        # Check if username already exists
        existing_user = await get_user_by_username(db, user_in.username)
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists",
            )
        user.username = user_in.username

    if user_in.email is not None:
        # Check if email already exists
        existing_user = await get_user_by_email(db, user_in.email)
        if existing_user and existing_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists",
            )
        user.email = user_in.email

    if user_in.full_name is not None:
        user.full_name = user_in.full_name

    if user_in.avatar_url is not None:
        user.avatar_url = user_in.avatar_url

    if user_in.phone_number is not None:
        user.phone_number = user_in.phone_number

    if user_in.password is not None:
        user.hashed_password = get_password_hash(user_in.password)

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


# Address services
async def get_user_addresses(
    db: AsyncSession, user_id: int
) -> List[Address]:
    """
    Get all addresses for a user
    """
    result = await db.execute(
        select(Address).where(Address.user_id == user_id)
    )
    return result.scalars().all()


async def create_user_address(
    db: AsyncSession, user_id: int, address_in: AddressCreate
) -> Address:
    """
    Create a new address for a user
    """
    # Check if this is the first address for the user
    addresses = await get_user_addresses(db, user_id)

    # If it's the first address or if is_default is True, set as default
    is_default = address_in.is_default
    if not addresses or is_default:
        # If a default address already exists and this new one is also default,
        # un-default the previous default address
        if is_default and addresses:
            for address in addresses:
                if address.is_default:
                    address.is_default = False
                    db.add(address)

    # Create new address
    db_address = Address(
        user_id=user_id,
        address_type=address_in.address_type,
        street=address_in.street,
        city=address_in.city,
        district=address_in.district,
        postal_code=address_in.postal_code,
        country=address_in.country,
        is_default=is_default or not addresses,  # First address is default
    )

    db.add(db_address)
    await db.commit()
    await db.refresh(db_address)
    return db_address


async def update_user_address(
    db: AsyncSession, user_id: int, address_id: int, address_in: AddressUpdate
) -> Address:
    """
    Update a user's address
    """
    # Get the address
    result = await db.execute(
        select(Address).where(Address.id == address_id, Address.user_id == user_id)
    )
    address = result.scalars().first()

    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Address not found",
        )

    # Update address attributes
    if address_in.address_type is not None:
        address.address_type = address_in.address_type

    if address_in.street is not None:
        address.street = address_in.street

    if address_in.city is not None:
        address.city = address_in.city

    if address_in.district is not None:
        address.district = address_in.district

    if address_in.postal_code is not None:
        address.postal_code = address_in.postal_code

    if address_in.country is not None:
        address.country = address_in.country

    # Handle default address changes
    if address_in.is_default is not None and address_in.is_default and not address.is_default:
        # If setting this address as default, unset others
        all_addresses = await get_user_addresses(db, user_id)
        for addr in all_addresses:
            if addr.id != address_id and addr.is_default:
                addr.is_default = False
                db.add(addr)

        address.is_default = True

    db.add(address)
    await db.commit()
    await db.refresh(address)
    return address


async def delete_user_address(
    db: AsyncSession, user_id: int, address_id: int
) -> None:
    """
    Delete a user's address
    """
    result = await db.execute(
        select(Address).where(Address.id == address_id, Address.user_id == user_id)
    )
    address = result.scalars().first()

    if not address:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Address not found",
        )

    was_default = address.is_default

    # Delete the address
    await db.delete(address)

    # If the deleted address was the default one, set a new default if any addresses remain
    if was_default:
        result = await db.execute(
            select(Address).where(Address.user_id == user_id).order_by(Address.id)
        )
        remaining_address = result.scalars().first()

        if remaining_address:
            remaining_address.is_default = True
            db.add(remaining_address)

    await db.commit()
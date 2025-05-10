from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import logging

from app.core.config import settings
from app.core.security import create_access_token, get_password_hash, verify_password
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import Token, UserCreate, User as UserSchema, UserLogin, ForgotPassword

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/register", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def register(
    user_in: UserCreate, db: AsyncSession = Depends(get_db)
) -> Any:
    """
    Register a new user
    """
    try:
        # Check if user with same username exists
        logger.info(f"Checking if username {user_in.username} exists")
        result = await db.execute(select(User).where(User.username == user_in.username))
        user = result.scalars().first()
        if user:
            logger.warning(f"Username {user_in.username} already registered")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered",
            )

        # Check if user with same email exists
        logger.info(f"Checking if email {user_in.email} exists")
        result = await db.execute(select(User).where(User.email == user_in.email))
        user = result.scalars().first()
        if user:
            logger.warning(f"Email {user_in.email} already registered")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        # Create new user
        logger.info(f"Creating new user: {user_in.username}")
        db_user = User(
            username=user_in.username,
            email=user_in.email,
            full_name=user_in.full_name,
            avatar_url=user_in.avatar_url,
            phone_number=user_in.phone_number,
            hashed_password=get_password_hash(user_in.password),
        )
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)

        logger.info(f"User {db_user.id} registered successfully")
        return db_user
    except Exception as e:
        logger.error(f"Error during registration: {str(e)}")
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error during registration: {str(e)}",
        )


@router.post("/login", response_model=Token)
async def login(
    login_data: UserLogin, db: AsyncSession = Depends(get_db)
) -> Any:
    """
    Simple login to get an access token for future requests
    """
    try:
        # Authenticate user
        logger.info(f"Authenticating user: {login_data.username}")
        result = await db.execute(select(User).where(User.username == login_data.username))
        user = result.scalars().first()
        if not user or not verify_password(login_data.password, user.hashed_password):
            logger.warning(f"Failed login attempt for username: {login_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Check if user is active
        if not user.is_active:
            logger.warning(f"Inactive user attempted login: {login_data.username}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user"
            )

        # Create access token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            subject=user.id, expires_delta=access_token_expires
        )

        logger.info(f"User {user.id} logged in successfully")
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException:
        # Re-raise HTTP exceptions as they are already properly formatted
        raise
    except Exception as e:
        logger.error(f"Error during login: {str(e)}")
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error during login: {str(e)}",
        )


@router.post("/verify-email")
async def verify_email(
    email: str, db: AsyncSession = Depends(get_db)
) -> Any:
    """
    Verify email
    """
    try:
        # Check if user with same email exists
        logger.info(f"Checking if email {email} exists")
        result = await db.execute(select(User).where(User.email == email))
        user = result.scalars().first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Email not found",
            )

        return {"message": "Email verified successfully"}

    except Exception as e:
        logger.error(f"Error during email verification: {str(e)}")
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error during email verification: {str(e)}",
        )


@router.post("/google")
async def login_with_google(
    email: str, db: AsyncSession = Depends(get_db)
) -> Any:
    """
    Login with Google
    """
    try:
        # Check if user with same email exists
        logger.info(f"Checking if email {email} exists")
        result = await db.execute(select(User).where(User.email == email))
        user = result.scalars().first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Email not found",
            )

        # Create access token
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            subject=user.id, expires_delta=access_token_expires
        )

        logger.info(f"User {user.id} logged in successfully")
        return {"access_token": access_token, "token_type": "bearer"}

    except Exception as e:
        logger.error(f"Error during email verification: {str(e)}")
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error during email verification: {str(e)}",
        )

@router.post("/forgot-password")
async def forgot_password(
    forgot_password_data: ForgotPassword, db: AsyncSession = Depends(get_db)
) -> Any:
    """
    Forgot password
    """
    try:
        # Check if user with same email exists
        logger.info(f"Checking if email {forgot_password_data.email} exists")
        result = await db.execute(select(User).where(User.email == forgot_password_data.email))
        user = result.scalars().first()
        if not user:
            logger.warning(f"Email {forgot_password_data.email} not found")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Email not found",
            )

        # Generate a new password
        new_password = forgot_password_data.new_password
        user.hashed_password = get_password_hash(new_password)
        await db.commit()
        await db.refresh(user)

        logger.info(f"Password reset for email: {forgot_password_data.email}")
        return {"message": "Password reset successfully"}

    except Exception as e:
        logger.error(f"Error during forgot password: {str(e)}")
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error during forgot password: {str(e)}",
        )
import logging
from datetime import datetime, timezone
from typing import Optional, Callable, Annotated, Any
from functools import wraps

from fastapi import Depends, HTTPException, status, Header, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, HTTPBasic, HTTPBasicCredentials
from jose import JWTError, jwt
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import TokenPayload
from app.services.user import get_user_by_id

# Setup logging
logger = logging.getLogger(__name__)

# Setup Bearer token authentication security
oauth2_scheme = HTTPBearer(
    scheme_name="Authorization",
    description="JWT Bearer token authentication",
    auto_error=True
)

# Optional OAuth2 scheme that doesn't raise an exception if token is missing
oauth2_scheme_optional = HTTPBearer(auto_error=False)

# Create a function that returns None if no token, replacing the original function with auto_error=False
def get_optional_token(authorization: str = Header(None)) -> Optional[str]:
    if not authorization:
        return None
    scheme, _, param = authorization.partition(" ")
    if not authorization or scheme.lower() != "bearer":
        return None
    return param

async def get_token(credentials: Optional[HTTPAuthorizationCredentials] = Security(oauth2_scheme)) -> str:
    """
    Extract and validate Bearer token from authorization header
    """
    logger.debug(f"Getting token from credentials: {credentials}")
    if not credentials:
        logger.warning("No credentials provided in the request")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if credentials.scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication scheme",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return credentials.credentials

async def get_current_user(
    db: AsyncSession = Depends(get_db),
    token: str = Depends(get_token)
) -> User:
    """
    Validate JWT token and get current user
    """
    logger.debug(f"Processing token for authentication")
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decode and verify JWT token
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        # Extract user ID from token subject claim
        user_id: str = payload.get("sub")
        if not user_id:
            raise credential_exception

        # Create token data with expiration info
        token_data = TokenPayload(sub=user_id, exp=payload.get("exp"))

        # Check if token has expired
        if datetime.now(timezone.utc) >= token_data.exp:
            raise credential_exception

        # Get user from database
        user = await db.get(User, int(token_data.sub))
        if not user:
            logger.warning(f"User not found for token with user_id: {user_id}")
            raise credential_exception

        return user

    except (JWTError, ValidationError) as e:
        logger.debug(f"Token validation error: {str(e)}")
        raise credential_exception

async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Verify user is active
    """
    logger.debug(f"Checking if user {current_user.id} is active")
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user account"
        )
    return current_user

async def get_current_superuser(
    current_user: User = Depends(get_current_active_user)
) -> User:
    """
    Verify user has admin privileges
    """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions"
        )
    return current_user

async def get_current_active_user_optional(
    db: AsyncSession = Depends(get_db),
    authorization: Optional[str] = Header(None)
) -> Optional[User]:
    """
    Try to get the current user, but return None if authentication fails
    instead of raising an exception
    """
    logger.debug(f"Trying optional authentication with header: {authorization}")

    if not authorization:
        return None

    try:
        # Extract token from header
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            return None

        # Decode and verify JWT token
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        # Extract user ID from token subject claim
        user_id: str = payload.get("sub")
        if not user_id:
            return None

        # Check if token has expired
        exp = payload.get("exp")
        if not exp or datetime.now(timezone.utc) >= datetime.fromtimestamp(exp, tz=timezone.utc):
            return None

        # Get user from database
        user = await db.get(User, int(user_id))
        if not user or not user.is_active:
            return None

        return user
    except (JWTError, ValidationError, ValueError):
        return None

async def get_optional_current_user(
    db: AsyncSession = Depends(get_db),
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(oauth2_scheme_optional)
) -> Optional[User]:
    """
    Get current user if authenticated, return None if not
    This function doesn't raise exceptions for unauthenticated users
    """
    if not credentials:
        return None

    token = credentials.credentials
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)

        # Check if token is expired
        if isinstance(token_data.exp, datetime):
            exp_datetime = token_data.exp
        else:
            # If token_data.exp is an integer (timestamp)
            exp_datetime = datetime.fromtimestamp(token_data.exp)

        # Ensure both datetimes are timezone-aware or timezone-naive before comparing
        # Convert both to UTC timezone-aware
        current_time = datetime.now(timezone.utc)

        # If exp_datetime is naive (no timezone info), assume it's in UTC
        if exp_datetime.tzinfo is None:
            exp_datetime = exp_datetime.replace(tzinfo=timezone.utc)

        if exp_datetime < current_time:
            return None
    except (JWTError, ValidationError):
        return None

    user = await get_user(db, user_id=token_data.sub)
    if not user:
        return None

    return user

async def get_user(db: AsyncSession, user_id: int) -> Optional[User]:
    """Helper function to get user by ID"""
    return await get_user_by_id(db, user_id)
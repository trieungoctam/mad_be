from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional, Union

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(
    subject: Union[str, Any],
    expires_delta: Optional[timedelta] = None,
    claims: Optional[Dict[str, Any]] = None
) -> str:
    """
    Create a JWT access token

    Args:
        subject: The subject of the token (usually user ID)
        expires_delta: Optional custom expiration time
        claims: Optional additional claims to include in the token

    Returns:
        JWT token as string
    """
    # Set expiration time
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    # Prepare token payload
    to_encode = {"exp": expire, "sub": str(subject)}

    # Add additional claims if provided
    if claims:
        to_encode.update(claims)

    # Encode and return the JWT
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against a hash

    Args:
        plain_password: Plain text password to check
        hashed_password: Hashed password to verify against

    Returns:
        True if password matches, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Hash a password

    Args:
        password: Plain text password to hash

    Returns:
        Secure hash of the password
    """
    return pwd_context.hash(password)

from cryptography.fernet import Fernet
import base64
import hashlib

# Tạo khóa đúng định dạng 32 byte cho Fernet
key = "MAD_PTIT_KEY_FOR_ENCRYPTION_AND_SECURITY"
# Sử dụng SHA-256 để đảm bảo độ dài 32 byte
key_bytes = hashlib.sha256(key.encode()).digest()
# Mã hóa base64 url-safe
fernet_key = base64.urlsafe_b64encode(key_bytes)
# Khởi tạo đối tượng Fernet
fernet = Fernet(fernet_key)

def encrypt_data(data: str) -> str:
    """Mã hóa dữ liệu nhạy cảm"""
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data: str) -> str:
    """Giải mã dữ liệu"""
    return fernet.decrypt(encrypted_data.encode()).decode()
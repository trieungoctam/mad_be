import os
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "Ecommerce Backend API"
    DEBUG: bool = True

    API_PREFIX: str = "/api"
    API_V1_STR: str = "/v1"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

    # CORS Configuration
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    # PostgreSQL Configuration
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "ecommerce"
    POSTGRES_PORT: str = "5432"
    SQLALCHEMY_DATABASE_URI: str = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SYNC_SQLALCHEMY_DATABASE_URI: str = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # MongoDB Configuration
    MONGO_URL: str
    MONGO_DB: str

    # Redis Configuration
    REDIS_HOST: str
    REDIS_PORT: int

    # Email Configuration
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    # Payment Gateway Configuration
    PAYMENT_GATEWAY_API_KEY: str
    PAYMENT_GATEWAY_SECRET: str

    class Config:
        case_sensitive = True
        env_file = ".env"
        model_extra = "ignore"  # Allow extra fields in settings


settings = Settings()
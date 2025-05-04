from fastapi import APIRouter

from app.routers.v1 import api_router as api_router_v1

api_router = APIRouter()

# Include version-specific routers
api_router.include_router(api_router_v1)
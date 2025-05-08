from fastapi import APIRouter

from app.core.config import settings
from app.routers.v1.auth import router as auth_router
from app.routers.v1.users import router as users_router
from app.routers.v1.shopping_lists import router as shopping_lists_router
from app.routers.v1.products import router as products_router
from app.routers.v1.barcodes import router as barcodes_router
from app.routers.v1.carts import router as carts_router
from app.routers.v1.orders import router as orders_router
from app.routers.v1.payments import router as payments_router
from app.routers.v1.shipments import router as shipments_router
from app.routers.v1.notifications import router as notifications_router

api_router = APIRouter(prefix=settings.API_V1_STR)

# Include all API routes
api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(products_router, prefix="/products", tags=["Products"])
api_router.include_router(carts_router, prefix="/carts", tags=["Carts"])
api_router.include_router(orders_router, prefix="/orders", tags=["Orders"])
api_router.include_router(shipments_router, prefix="/shipments", tags=["Shipments"])
# api_router.include_router(barcodes_router, prefix="/barcodes", tags=["Barcodes"])
api_router.include_router(payments_router, prefix="/payments", tags=["Payments"])
api_router.include_router(notifications_router, prefix="/notifications", tags=["Notifications"])
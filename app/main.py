import logging

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.openapi.utils import get_openapi

from app.core.config import settings
# from app.db.mongo import connect_to_mongo, close_mongo_connection
# from app.db.redis import connect_to_redis, close_redis_connection
from app.routers import api_router

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Ecommerce API",
    description="""
    Backend API for Ecommerce Mobile Application
    """,
    version="1.0.0",
    docs_url=f"{settings.API_PREFIX}/docs",
    redoc_url=f"{settings.API_PREFIX}/redoc",
    openapi_url=f"{settings.API_PREFIX}/openapi.json",
)

# Custom OpenAPI schema to include JWT Auth
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    # Ensure components object exists
    if "components" not in openapi_schema:
        openapi_schema["components"] = {}

    # Ensure schemas object exists
    if "schemas" not in openapi_schema["components"]:
        openapi_schema["components"]["schemas"] = {}

    # Add JWT Bearer Authentication security scheme
    openapi_schema["components"]["securitySchemes"] = {
        "Authorization": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Enter your JWT token in the format **Bearer &lt;token&gt;**"
        }
    }

    # Apply security to all routes except login/register
    openapi_schema["security"] = [{"Authorization": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add session middleware
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
    max_age=86400  # 24 hours
)

# Register startup and shutdown events
@app.on_event("startup")
async def startup_event():
    logger.info("Starting up application")
    # await connect_to_mongo()
    # await connect_to_redis()
    pass

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down application")
    # await close_mongo_connection()
    # await close_redis_connection()
    pass


# Include API router
app.include_router(api_router, prefix=settings.API_PREFIX)


# Health check endpoint
@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "ok", "message": "Service is healthy"}


# Test endpoint for debugging auth headers
@app.get("/test-auth-headers", tags=["Debug"])
async def test_auth_headers(request: Request):
    headers = dict(request.headers)
    auth_header = headers.get("authorization", "No authorization header found")
    return {
        "headers": headers,
        "authorization": auth_header,
    }

if __name__=='__main__':
  import uvicorn
  uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

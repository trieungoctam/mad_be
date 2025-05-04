import redis.asyncio as redis

from app.core.config import settings

redis_client = None


async def connect_to_redis():
    """
    Connect to Redis
    """
    global redis_client
    redis_client = redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        decode_responses=True
    )
    print("Connected to Redis")


async def close_redis_connection():
    """
    Close Redis connection
    """
    global redis_client
    if redis_client:
        await redis_client.close()
        print("Closed Redis connection")


def get_redis():
    """
    Get Redis client
    """
    return redis_client
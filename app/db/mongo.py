from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings

mongo_client = None
mongo_db = None


async def connect_to_mongo():
    """
    Connect to MongoDB
    """
    global mongo_client, mongo_db
    mongo_client = AsyncIOMotorClient(settings.MONGO_URL)
    mongo_db = mongo_client[settings.MONGO_DB]
    print("Connected to MongoDB")


async def close_mongo_connection():
    """
    Close MongoDB connection
    """
    global mongo_client
    if mongo_client:
        mongo_client.close()
        print("Closed MongoDB connection")


def get_database():
    """
    Get MongoDB database object
    """
    return mongo_db
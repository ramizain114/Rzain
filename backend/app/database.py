"""Database initialization and connection management."""

from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
import logging

from app.config import settings

logger = logging.getLogger(__name__)


class Database:
    """Database connection manager."""

    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect_db(cls, document_models: List):
        """Initialize database connection and Beanie ODM."""
        try:
            cls.client = AsyncIOMotorClient(settings.mongodb_url)
            cls.db = cls.client[settings.mongodb_db_name]

            await init_beanie(
                database=cls.db,
                document_models=document_models
            )

            logger.info(f"Connected to MongoDB database: {settings.mongodb_db_name}")
        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise

    @classmethod
    async def close_db(cls):
        """Close database connection."""
        if cls.client:
            cls.client.close()
            logger.info("Closed MongoDB connection")


async def get_database():
    """Dependency for getting database instance."""
    return Database.db

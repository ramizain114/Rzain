"""Pytest configuration and fixtures."""

import pytest
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.config import settings
from app.models import DOCUMENT_MODELS


@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def db():
    """Initialize test database."""
    client = AsyncIOMotorClient(settings.mongodb_url)
    db = client["amana_grc_test"]

    await init_beanie(database=db, document_models=DOCUMENT_MODELS)

    yield db

    # Cleanup
    await db.client.drop_database("amana_grc_test")

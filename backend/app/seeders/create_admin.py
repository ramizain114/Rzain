"""Create default admin user."""

import asyncio
import logging
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.config import settings
from app.models import DOCUMENT_MODELS
from app.models.user import User, Role
from app.core.security import get_password_hash

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def create_admin():
    """Create default admin user."""
    # Connect to database
    client = AsyncIOMotorClient(settings.mongodb_url)
    db = client[settings.mongodb_db_name]

    await init_beanie(database=db, document_models=DOCUMENT_MODELS)

    # Check if admin exists
    existing_admin = await User.find_one(User.username == settings.default_admin_username)

    if existing_admin:
        logger.info(f"Admin user '{settings.default_admin_username}' already exists")
        return

    # Create admin user
    admin = User(
        username=settings.default_admin_username,
        email=settings.default_admin_email,
        full_name_en="System Administrator",
        full_name_ar="مدير النظام",
        hashed_password=get_password_hash(settings.default_admin_password),
        role=Role.ADMIN,
        is_active=True,
        is_ldap_user=False,
    )

    await admin.insert()
    logger.info(f"Created admin user: {settings.default_admin_username}")
    logger.info("Please change the default password after first login!")


if __name__ == "__main__":
    asyncio.run(create_admin())

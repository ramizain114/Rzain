"""Authentication tests."""

import pytest
from app.services.auth_service import AuthService
from app.models.user import User, Role


@pytest.mark.asyncio
async def test_create_local_user(db):
    """Test creating a local user."""
    auth_service = AuthService()

    user = await auth_service.create_local_user(
        username="testuser",
        email="test@example.com",
        password="testpass123",
        full_name_en="Test User",
        full_name_ar="مستخدم تجريبي",
        role=Role.VIEWER,
    )

    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.is_ldap_user is False
    assert user.hashed_password is not None


@pytest.mark.asyncio
async def test_authenticate_local_user(db):
    """Test local user authentication."""
    auth_service = AuthService()

    # Create user
    await auth_service.create_local_user(
        username="testuser",
        email="test@example.com",
        password="testpass123",
        full_name_en="Test User",
        full_name_ar="مستخدم تجريبي",
        role=Role.VIEWER,
    )

    # Authenticate
    user, access_token, refresh_token = await auth_service.authenticate_user(
        "testuser",
        "testpass123"
    )

    assert user is not None
    assert access_token is not None
    assert refresh_token is not None

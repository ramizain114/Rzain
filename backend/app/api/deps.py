"""API dependencies for dependency injection."""

from typing import Optional
from fastapi import Depends, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.models.user import User, Role
from app.core.security import decode_token
from app.core.exceptions import raise_unauthorized, raise_forbidden

security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> User:
    """Get current authenticated user from JWT token."""
    token = credentials.credentials
    payload = decode_token(token)

    if not payload:
        raise_unauthorized("Invalid or expired token")

    user_id = payload.get("sub")
    if not user_id:
        raise_unauthorized("Invalid token payload")

    user = await User.get(user_id)
    if not user:
        raise_unauthorized("User not found")

    if not user.is_active:
        raise_unauthorized("User account is inactive")

    return user


async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """Get current active user."""
    if not current_user.is_active:
        raise_unauthorized("Inactive user")
    return current_user


def require_role(*allowed_roles: Role):
    """Dependency to check if user has required role."""

    async def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in allowed_roles:
            raise_forbidden(f"This action requires one of these roles: {', '.join(r.value for r in allowed_roles)}")
        return current_user

    return role_checker


def require_admin(current_user: User = Depends(get_current_user)) -> User:
    """Require admin role."""
    if current_user.role != Role.ADMIN:
        raise_forbidden("Admin access required")
    return current_user

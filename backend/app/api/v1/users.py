"""User management endpoints."""

from typing import List
from fastapi import APIRouter, Depends, status

from app.schemas.user import UserResponse, UserCreate, UserUpdate
from app.models.user import User, Role
from app.api.deps import get_current_user, require_admin
from app.core.exceptions import raise_not_found, raise_bad_request
from app.services.auth_service import AuthService

router = APIRouter()


@router.get("/", response_model=List[UserResponse], dependencies=[Depends(require_admin)])
async def list_users():
    """List all users (admin only)."""
    users = await User.find_all().to_list()
    return [
        UserResponse(
            id=str(user.id),
            username=user.username,
            email=user.email,
            full_name_en=user.full_name_en,
            full_name_ar=user.full_name_ar,
            role=user.role.value,
            is_active=user.is_active,
            is_ldap_user=user.is_ldap_user,
        )
        for user in users
    ]


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_admin)])
async def create_user(user_data: UserCreate):
    """Create a new local user (admin only)."""
    if user_data.is_ldap_user:
        raise_bad_request("Cannot create LDAP users via API")

    if not user_data.password:
        raise_bad_request("Password is required for local users")

    auth_service = AuthService()
    user = await auth_service.create_local_user(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password,
        full_name_en=user_data.full_name_en,
        full_name_ar=user_data.full_name_ar,
        role=Role(user_data.role),
    )

    return UserResponse(
        id=str(user.id),
        username=user.username,
        email=user.email,
        full_name_en=user.full_name_en,
        full_name_ar=user.full_name_ar,
        role=user.role.value,
        is_active=user.is_active,
        is_ldap_user=user.is_ldap_user,
    )


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str, current_user: User = Depends(get_current_user)):
    """Get user by ID."""
    # Users can view their own profile, admins can view any profile
    if str(current_user.id) != user_id and current_user.role != Role.ADMIN:
        raise_bad_request("Cannot view other users' profiles")

    user = await User.get(user_id)
    if not user:
        raise_not_found("User not found")

    return UserResponse(
        id=str(user.id),
        username=user.username,
        email=user.email,
        full_name_en=user.full_name_en,
        full_name_ar=user.full_name_ar,
        role=user.role.value,
        is_active=user.is_active,
        is_ldap_user=user.is_ldap_user,
    )

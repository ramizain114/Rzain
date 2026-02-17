"""Authentication endpoints."""

from fastapi import APIRouter, Depends, status

from app.schemas.auth import LoginRequest, TokenResponse, UserProfile
from app.services.auth_service import AuthService
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter()


@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(request: LoginRequest):
    """
    Authenticate user via LDAP or local database.

    Returns JWT access and refresh tokens.
    """
    auth_service = AuthService()
    user, access_token, refresh_token = await auth_service.authenticate_user(
        request.username,
        request.password
    )

    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="bearer"
    )


@router.get("/me", response_model=UserProfile, status_code=status.HTTP_200_OK)
async def get_current_user_profile(current_user: User = Depends(get_current_user)):
    """Get current user profile."""
    return UserProfile(
        id=str(current_user.id),
        username=current_user.username,
        email=current_user.email,
        full_name_en=current_user.full_name_en,
        full_name_ar=current_user.full_name_ar,
        role=current_user.role.value,
        is_active=current_user.is_active,
        is_ldap_user=current_user.is_ldap_user,
        last_login=current_user.last_login.isoformat() if current_user.last_login else None
    )

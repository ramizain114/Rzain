"""Custom exception classes."""

from typing import Any, Dict, Optional
from fastapi import HTTPException, status


class AmanaGRCException(Exception):
    """Base exception for Amana-GRC."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)


class AuthenticationError(AmanaGRCException):
    """Authentication failed."""
    pass


class AuthorizationError(AmanaGRCException):
    """User not authorized for this action."""
    pass


class NotFoundError(AmanaGRCException):
    """Resource not found."""
    pass


class ValidationError(AmanaGRCException):
    """Validation error."""
    pass


class LDAPConnectionError(AmanaGRCException):
    """LDAP server connection failed."""
    pass


class AIServiceError(AmanaGRCException):
    """AI service error."""
    pass


# HTTP exceptions
def raise_unauthorized(detail: str = "Could not validate credentials"):
    """Raise 401 Unauthorized."""
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"},
    )


def raise_forbidden(detail: str = "Not enough permissions"):
    """Raise 403 Forbidden."""
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=detail,
    )


def raise_not_found(detail: str = "Resource not found"):
    """Raise 404 Not Found."""
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=detail,
    )


def raise_bad_request(detail: str = "Bad request"):
    """Raise 400 Bad Request."""
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=detail,
    )

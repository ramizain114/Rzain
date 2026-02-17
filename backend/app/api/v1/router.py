"""API v1 router aggregation."""

from fastapi import APIRouter

from app.api.v1 import auth, users, standards, controls, risks

api_router = APIRouter(prefix="/v1")

# Include all v1 route modules
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(standards.router, prefix="/standards", tags=["Standards"])
api_router.include_router(controls.router, prefix="/controls", tags=["Controls"])
api_router.include_router(risks.router, prefix="/risks", tags=["Risks"])

"""API v1 router aggregation."""

from fastapi import APIRouter

from app.api.v1 import (
    auth, users, standards, controls, risks, audits,
    dashboard, ai, evidence, export, analytics
)

api_router = APIRouter(prefix="/v1")

# Include all v1 route modules
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(standards.router, prefix="/standards", tags=["Standards"])
api_router.include_router(controls.router, prefix="/controls", tags=["Controls"])
api_router.include_router(risks.router, prefix="/risks", tags=["Risks"])
api_router.include_router(audits.router, prefix="/audits", tags=["Audits"])
api_router.include_router(evidence.router, prefix="/evidence", tags=["Evidence"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
api_router.include_router(ai.router, prefix="/ai", tags=["AI"])
api_router.include_router(export.router, prefix="/export", tags=["Export"])
api_router.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])

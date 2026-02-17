"""Main FastAPI application."""

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import Database
from app.models import DOCUMENT_MODELS
from app.core.middleware import RequestLoggingMiddleware, setup_cors
from app.api.v1.router import api_router
from app.api.health import router as health_router

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if settings.app_debug else logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    # Startup
    logger.info("Starting Amana-GRC application...")
    await Database.connect_db(DOCUMENT_MODELS)
    logger.info("Database connection established")

    yield

    # Shutdown
    logger.info("Shutting down Amana-GRC application...")
    await Database.close_db()
    logger.info("Database connection closed")


# Create FastAPI application
app = FastAPI(
    title="Amana-GRC API",
    description="Governance, Risk, and Compliance platform for Saudi municipal government",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Setup CORS
setup_cors(app)

# Add middleware
app.add_middleware(RequestLoggingMiddleware)

# Include routers
app.include_router(health_router, tags=["Health"])
app.include_router(api_router, prefix="/api")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "Amana-GRC API",
        "version": "0.1.0",
        "status": "running",
        "docs": "/docs",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.app_debug,
    )

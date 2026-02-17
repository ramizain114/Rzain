"""Middleware configuration."""

import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware for logging requests and response times."""

    async def dispatch(self, request: Request, call_next):
        """Process the request and log it."""
        start_time = time.time()

        # Log request
        logger.info(f"Request: {request.method} {request.url.path}")

        # Process request
        response = await call_next(request)

        # Calculate processing time
        process_time = time.time() - start_time
        logger.info(
            f"Response: {response.status_code} - "
            f"Completed in {process_time:.2f}s"
        )

        # Add processing time to response headers
        response.headers["X-Process-Time"] = str(process_time)

        return response


def setup_cors(app):
    """Configure CORS middleware."""
    from app.config import settings

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

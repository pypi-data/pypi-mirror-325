from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request
import logging
import time

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)

        duration = time.time() - start_time
        logger.info(
            f"{request.method} {request.url.path} "
            f"completed in {duration:.2f}s with status {response.status_code}"
        )

        return response

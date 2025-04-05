from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
import os


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        api_key = request.headers.get("X-API-Key")

        # Skip auth for docs
        if request.url.path in ["/docs", "/openapi.json", "/redoc"]:
            return await call_next(request)

        if not api_key or api_key not in os.getenv("ALLOWED_API_KEYS", "").split(","):
            raise HTTPException(status_code=401, detail="Invalid API key")

        return await call_next(request)

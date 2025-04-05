from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from collections import defaultdict
import time


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, requests_per_minute: int = 60):
        super().__init__(app)
        self.requests_per_minute = requests_per_minute
        self.request_counts = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        now = time.time()

        # Clean old requests
        self.request_counts[client_ip] = [
            req_time
            for req_time in self.request_counts[client_ip]
            if now - req_time < 60
        ]

        # Check rate limit
        if len(self.request_counts[client_ip]) >= self.requests_per_minute:
            raise HTTPException(
                status_code=429,
                detail="Rate limit exceeded. Please try again in a minute.",
            )

        # Add current request
        self.request_counts[client_ip].append(now)

        return await call_next(request)

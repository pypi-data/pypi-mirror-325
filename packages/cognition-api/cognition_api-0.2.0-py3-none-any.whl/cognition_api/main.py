from cognition_api.middleware.rate_limit import RateLimitMiddleware
from cognition_api.utils.metrics import MetricsCollector
from cognition_api.utils.error_handler import (
    validation_exception_handler,
    http_exception_handler,
    general_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from cognition_api.service import create_app
from cognition_api.routes import health

REQUEST_PER_MINUTE = 1000
app = create_app()

# Add health check
app.include_router(health.router, tags=["health"])

# Add rate limiting
app.add_middleware(RateLimitMiddleware, requests_per_minute=REQUEST_PER_MINUTE)

# Add error handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

# Initialize metrics
app.state.metrics = MetricsCollector()


# Add metrics endpoint
@app.get("/metrics", tags=["monitoring"])
async def get_metrics():
    return app.state.metrics.get_metrics()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

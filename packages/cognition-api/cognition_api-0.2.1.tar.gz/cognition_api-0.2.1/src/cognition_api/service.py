from cognition_api.middleware.logging import LoggingMiddleware
from cognition_api.core.interface import BaseAgentBackend
from cognition_api.utils.task_manager import TaskManager
from contextlib import asynccontextmanager
from cognition_api.routes import openai
from typing import Dict, Any, Optional
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize components with dependency injection
    app.state.task_manager = TaskManager()
    app.state.agent_backend = app.agent_backend or DefaultAgentBackend()
    yield
    # Cleanup
    await app.state.agent_backend.cleanup()


def create_app(agent_backend: Optional[BaseAgentBackend] = None) -> FastAPI:
    """Create base FastAPI app with core configuration"""
    app = FastAPI(lifespan=lifespan)

    # Store the backend for use in lifespan
    app.agent_backend = agent_backend

    # Add core middleware
    app.add_middleware(LoggingMiddleware)

    # Include base API routes
    app.include_router(openai.router, prefix="/v1", tags=["openai"])

    return app


# Example implementations
class CrewAIBackend(BaseAgentBackend):
    """CrewAI implementation"""

    def __init__(self, crew_config: dict):
        self.crew_config = crew_config

    async def generate(self, messages: list, **kwargs) -> str:
        # Implement CrewAI specific logic
        pass

    async def run_task(self, task: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        # Implement CrewAI specific task execution
        pass


class OpenAIBackend(BaseAgentBackend):
    """OpenAI implementation"""

    def __init__(self, api_key: str):
        self.api_key = api_key

    async def generate(self, messages: list, **kwargs) -> str:
        # Implement OpenAI specific logic
        pass

    async def run_task(self, task: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        # Implement OpenAI specific task execution
        pass


class DefaultAgentBackend(BaseAgentBackend):
    """Simple echo backend for testing"""

    async def generate(self, messages: list, **kwargs) -> str:
        return f"Echo: {messages[-1]['content']}"

    async def run_task(self, task: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return {"task": task, "result": f"Echo: {inputs}"}

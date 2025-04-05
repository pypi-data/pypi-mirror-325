from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class AgentRequest(BaseModel):
    """Request model for agent tasks"""

    task: str = Field(..., description="Task identifier")
    inputs: Dict[str, Any] = Field(default_factory=dict, description="Task inputs")
    callback_url: Optional[str] = Field(
        None, description="Webhook URL for async completion"
    )
    async_execution: bool = Field(True, description="Run task asynchronously")

    class Config:
        json_schema_extra = {
            "example": {
                "task": "research",
                "inputs": {"topic": "AI agents"},
                "callback_url": "https://api.example.com/webhook",
                "async_execution": True,
            }
        }


class AgentResponse(BaseModel):
    """Response model for agent tasks"""

    task_id: str = Field(..., description="Unique task identifier")
    status: TaskStatus = Field(..., description="Current task status")
    result: Optional[Dict[str, Any]] = Field(
        None, description="Task result if completed"
    )
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Add these new models for OpenAI compatibility
class ChatMessage(BaseModel):
    role: str
    content: str


class OpenAIRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    temperature: float = 1.0
    max_tokens: Optional[int] = None
    stream: bool = False


class OpenAIResponse(BaseModel):
    id: str
    created: int
    model: str
    choices: List[Dict[str, Any]]
    usage: Optional[Dict[str, int]] = None

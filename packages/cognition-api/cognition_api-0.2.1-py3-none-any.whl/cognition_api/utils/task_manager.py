from cognition_api.models import TaskStatus, AgentResponse
from typing import Dict, Optional
from datetime import datetime
import asyncio
import uuid
import httpx


class TaskManager:
    def __init__(self):
        self.tasks: Dict[str, AgentResponse] = {}
        self._lock = asyncio.Lock()

    async def create_task(self, task: str, inputs: dict) -> str:
        """Create a new task and return its ID"""
        task_id = str(uuid.uuid4())
        task_response = AgentResponse(task_id=task_id, status=TaskStatus.PENDING)

        async with self._lock:
            self.tasks[task_id] = task_response

        return task_id

    async def update_task(
        self, task_id: str, status: TaskStatus, result: Optional[dict] = None
    ):
        """Update task status and result"""
        async with self._lock:
            if task_id not in self.tasks:
                raise KeyError(f"Task {task_id} not found")

            task = self.tasks[task_id]
            task.status = status
            task.result = result
            task.updated_at = datetime.utcnow()

    async def send_callback(self, url: str, task_response: AgentResponse):
        """Send webhook callback"""
        async with httpx.AsyncClient() as client:
            try:
                await client.post(url, json=task_response.dict())
            except Exception as e:
                print(f"Callback failed: {str(e)}")

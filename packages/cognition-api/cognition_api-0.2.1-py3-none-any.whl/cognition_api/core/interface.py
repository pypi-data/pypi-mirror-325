from typing import Dict, Any


class BaseAgentBackend:
    """Abstract base class for agent backends"""

    async def generate(self, messages: list, **kwargs) -> str:
        """Generate response from messages"""
        raise NotImplementedError

    async def run_task(self, task: str, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Run a specific task with inputs"""
        raise NotImplementedError

    async def cleanup(self):
        """Cleanup resources"""
        pass

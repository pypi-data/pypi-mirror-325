from cognition_api.models import OpenAIRequest, OpenAIResponse
from fastapi import APIRouter, HTTPException, Request
import time

router = APIRouter()


@router.post("/chat/completions", response_model=OpenAIResponse)
async def chat_completion(request: OpenAIRequest, fastapi_request: Request):
    """OpenAI-compatible chat completion endpoint"""
    try:
        # Get the configured backend from app state
        backend = fastapi_request.app.state.agent_backend

        # Execute using configured backend
        response = await backend.run_task(
            task="chat_completion",
            inputs={
                "messages": [m.dict() for m in request.messages],
                "model": request.model,
                "temperature": request.temperature,
            },
        )

        # Convert to OpenAI format
        return OpenAIResponse(
            id=response["task_id"],
            created=int(time.time()),
            model=request.model,
            choices=[
                {
                    "message": {
                        "role": "assistant",
                        "content": response["result"]["output"],
                    },
                    "finish_reason": "stop",
                }
            ],
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

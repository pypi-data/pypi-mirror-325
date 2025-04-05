import asyncio
import httpx


async def test_api():
    # Test data
    test_request = {
        "task": "test_task",
        "inputs": {"message": "Hello, Agent!", "parameters": {"key": "value"}},
    }

    async with httpx.AsyncClient() as client:
        try:
            # Make request to local API
            response = await client.post(
                "http://localhost:8000/v1/agent/run", json=test_request
            )

            # Assert successful response
            assert response.status_code == 200

            data = response.json()
            print("\nTest Results:")
            print(f"Status Code: {response.status_code}")
            print(f"Response: {data}")

            # Add more specific assertions based on your expected response
            assert "task" in data
            assert "result" in data

        except httpx.ConnectError:
            print("\nError: Could not connect to the server.")
            print("Make sure the FastAPI server is running on http://localhost:8000")
            raise


if __name__ == "__main__":
    asyncio.run(test_api())

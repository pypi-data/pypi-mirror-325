## SpecStory

## Starlette Server and SSE Implementation (14/01/2025, 13:13:05)

_**User**_

Here is how should it be made:
"""
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Route

app = Server("example-server")
sse = SseServerTransport("/messages")

async def handle_sse(scope, receive, send):
    async with sse.connect_sse(scope, receive, send) as streams:
        await app.run(streams[0], streams[1], app.create_initialization_options())

async def handle_messages(scope, receive, send):
    await sse.handle_post_message(scope, receive, send)

starlette_app = Starlette(
    routes=[
        Route("/sse", endpoint=handle_sse),
        Route("/messages", endpoint=handle_messages, methods=["POST"]),
    ]
)
"""


---

_**Assistant**_

I notice you're showing an example of how to structure the server code differently. Let me analyze the differences and propose changes to align our implementation with this pattern.

Key differences I notice:
1. Using `Starlette` directly instead of `FastAPI`
2. Simpler endpoint handlers that work directly with ASGI interface (scope, receive, send)
3. Different URL pattern ("/messages" vs "/message")
4. More direct routing setup

I'll help modify the code to match this pattern. First, let me read the server implementation to ensure we make compatible changes.

---

_**Assistant**_



---

_**Assistant**_



Now I'll modify the main.py file to match the suggested pattern while preserving our server implementation. Let me make those changes:

---

_**Assistant**_

```
import logging
from starlette.applications import Starlette
from starlette.routing import Route
from mcp.server.sse import SseServerTransport
from mcp.server import InitializationOptions

from my_mcp_server.server import app as mcp_app

logger = logging.getLogger("my_mcp_server.main")
logger.setLevel(logging.INFO)

# SSE transport setup
sse = SseServerTransport("/messages")

async def handle_sse(scope, receive, send):
    """SSE endpoint to handle server -> client streaming."""
    async with sse.connect_sse(scope, receive, send) as streams:
        await mcp_app.run(
            streams[0],
            streams[1],
            InitializationOptions(
                server_name="my_mcp_server_sse",
                server_version="0.1.0",
                capabilities=mcp_app.get_capabilities(),
            ),
        )

async def handle_messages(scope, receive, send):
    """POST endpoint for JSON-RPC messages from client -> server."""
    await sse.handle_post_message(scope, receive, send)

app = Starlette(
    routes=[
        Route("/sse", endpoint=handle_sse),
        Route("/messages", endpoint=handle_messages, methods=["POST"]),
    ]
)

def main():
    """For uvicorn-based startup"""
    import uvicorn
    uvicorn.run("my_mcp_server.main:app", host="127.0.0.1", port=8031, reload=False)

if __name__ == "__main__":
    main()
```

---

_**Assistant**_



I've refactored the main.py file to match the suggested pattern. Here are the key changes made:

1. Switched from FastAPI to Starlette directly
2. Simplified the endpoint handlers to work with ASGI interface (scope, receive, send)
3. Changed the message endpoint from "/message" to "/messages" to match the pattern
4. Removed the FastAPI-specific decorators and responses
5. Simplified the routing setup
6. Removed the root endpoint as it's not part of the core functionality

The core functionality remains the same, but the implementation is now more streamlined and follows the pattern you provided. The server will still:
1. Handle SSE connections for server->client streaming
2. Process JSON-RPC messages from client->server
3. Run on port 8031

Would you like me to make any adjustments to this implementation?

---

_**User**_

fix

---

_**Assistant**_

The error message indicates that the `handle_sse` function is missing the `receive` and `send` arguments when called. This is likely due to the way the route is set up in Starlette, which expects the endpoint function to accept a `Request` object instead of the ASGI `scope`, `receive`, and `send` directly.

To fix this, we need to adjust the endpoint functions to accept a `Request` object and then extract the necessary components from it. Let's make those changes.

---

_**Assistant**_

```
from starlette.requests import Request

async def handle_sse(request: Request):
    """SSE endpoint to handle server -> client streaming."""
    scope = request.scope
    receive = request.receive
    send = request.send
    async with sse.connect_sse(scope, receive, send) as streams:
        await mcp_app.run(
            streams[0],
            streams[1],
            InitializationOptions(
                server_name="my_mcp_server_sse",
                server_version="0.1.0",
                capabilities=mcp_app.get_capabilities(),
            ),
        )

async def handle_messages(request: Request):
    """POST endpoint for JSON-RPC messages from client -> server."""
    scope = request.scope
    receive = request.receive
    send = request.send
    await sse.handle_post_message(scope, receive, send)
```

---

_**Assistant**_

I've updated the `handle_sse` and `handle_messages` functions to accept a `Request` object and extract the `scope`, `receive`, and `send` from it. This should resolve the `TypeError` you encountered.

Please try running the server again to see if the issue is resolved. Let me know if there's anything else you'd like to adjust or if further issues arise!

---



---


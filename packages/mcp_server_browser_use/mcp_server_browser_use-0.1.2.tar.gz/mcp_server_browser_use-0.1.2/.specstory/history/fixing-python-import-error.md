## SpecStory

## Fixing Python Import Error (12/01/2025, 23:48:54)

_**User**_

fix

---

_**Assistant**_

I see the issue - there's an import error in `main.py` due to using a relative import (`.server`) when the file is being run directly as a module. Let me help fix this.

First, let me check the project structure to understand how to properly set up the imports.

---

_**Assistant**_



---

_**Assistant**_



I see the issue. The `main.py` and `server.py` are at the root level, but you're trying to use a relative import. Let me fix this by changing the relative import to an absolute import.

---

_**Assistant**_

```
import logging
from fastapi import FastAPI
from typing import Any
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route

from mcp.server.sse import SseServerTransport
from mcp.server import NotificationOptions, InitializationOptions
import mcp.types as types

from server import app as mcp_app  # Our actual MCP server instance with all handlers
// ... existing code ...
```

---

_**Assistant**_



I've changed the relative import `.server` to an absolute import `server` since both files are at the root level. The apply model also made some formatting improvements, which is fine.

Now you should be able to run the server using:

---

_**Assistant**_

```
uv run python main.py
```

---

_**Assistant**_



I see we have another import issue. Let me check the project structure more thoroughly to understand how the `browser_use` module should be organized.

---

_**Assistant**_



---

_**Assistant**_



I see the issue now. The project is set up as a Python package named `my_mcp_server`, but our files are not organized in the correct package structure. Let me help reorganize the files to match the package structure.

1. First, let's create the proper package structure:

---

_**Assistant**_

```
mkdir -p my_mcp_server
```

---

_**Assistant**_



2. Now, let's move the relevant files into the package:

---

_**Assistant**_

```
mv main.py server.py __init__.py my_mcp_server/
```

---

_**Assistant**_







3. Let's create a new entry point script at the root level:

---

_**Assistant**_

```
#!/usr/bin/env python3
"""
Entry point script for running the MCP server
"""
from my_mcp_server.main import main

if __name__ == "__main__":
    main()
```

---

_**Assistant**_







4. Now let's update the imports in the main.py file to use the correct package structure:

---

_**Assistant**_

```
import logging
from fastapi import FastAPI
from typing import Any
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route

from mcp.server.sse import SseServerTransport
from mcp.server import NotificationOptions, InitializationOptions
import mcp.types as types

from my_mcp_server.server import app as mcp_app  # Our actual MCP server instance with all handlers
// ... existing code ...
```

---

_**Assistant**_







Now you should be able to run the server using:

---

_**Assistant**_

```
uv run python run.py
```

---

_**Assistant**_







I see we still have an issue with the `browser_use` package. Let's install it first since it's listed as a dependency in `pyproject.toml`:

---

_**Assistant**_

```
uv pip install -e .
```

---

_**Assistant**_







Now let's try running the server again:

---

_**Assistant**_

```
uv run python run.py
```

---

_**Assistant**_











Let's install the `browser-use` package explicitly:

---

_**Assistant**_

```
uv pip install browser-use==0.1.8
```

---

_**Assistant**_



---

_**User**_

fix

---

_**Assistant**_

I see we have a new error - the `Request` object doesn't have a `send` attribute. This is because we're trying to access the ASGI protocol methods directly from the Request object, but we need to handle the WebSocket/SSE connection differently. Let me fix this.

---

_**Assistant**_

```
import logging
from fastapi import FastAPI
from typing import Any
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket

from mcp.server.sse import SseServerTransport
from mcp.server import NotificationOptions, InitializationOptions
import mcp.types as types

from my_mcp_server.server import app as mcp_app

logger = logging.getLogger("my_mcp_server.main")
logger.setLevel(logging.INFO)

fastapi_app = FastAPI(
    title="My MCP Server (Browser-Use)",
    description="HTTP-based SSE for MCP communication with browser automation",
    version="0.1.0",
)

# SSE transport endpoints
transport = SseServerTransport("/message")


async def sse_endpoint(websocket: WebSocket):
    """
    SSE endpoint to handle server -> client streaming.
    """
    await websocket.accept()
    async with transport.connect_sse(websocket.scope, websocket.receive, websocket.send) as streams:
        await mcp_app.run(
            streams[0],
            streams[1],
            InitializationOptions(
                server_name="my_mcp_server_sse",
                server_version="0.1.0",
                capabilities=mcp_app.get_capabilities(
                    notification_options=NotificationOptions()
                ),
            ),
        )


async def message_endpoint(request: Request):
    """
    POST endpoint for JSON-RPC messages from client -> server.
    """
    return await transport.handle_post_message(request.scope, request.receive, request._send)


routes = [
    WebSocketRoute("/sse", endpoint=sse_endpoint),
    Route("/message", endpoint=message_endpoint, methods=["POST"]),
]

for r in routes:
    fastapi_app.router.routes.append(r)


@fastapi_app.get("/")
async def root():
    return {
        "message": "Welcome to the Browser-Use MCP Server! Connect to /sse for SSE, and /message for JSON-RPC."
    }


app = fastapi_app


def main():
    """
    For uvicorn-based startup
    """
    import uvicorn

    uvicorn.run("my_mcp_server.main:app", host="127.0.0.1", port=8031, reload=False)


if __name__ == "__main__":
    main()
```

---

_**Assistant**_



I've made several important changes:

1. Changed the SSE endpoint to use WebSocket instead of regular HTTP request, since we need bi-directional communication
2. Added proper WebSocket handling with `await websocket.accept()`
3. Updated the message endpoint to use the internal `_send` method from the request object
4. Changed the route type for `/sse` to `WebSocketRoute`

Now let's try running the server again:

---

_**Assistant**_

```
uv run python run.py
```

---

_**Assistant**_



---

_**User**_

no it should be http

---

_**Assistant**_

Ah, you're right - for Server-Sent Events (SSE) we should use HTTP, not WebSocket. Let me revert back to HTTP but fix the send attribute issue:

---

_**Assistant**_

```
import logging
from fastapi import FastAPI
from typing import Any
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse
from starlette.routing import Route

from mcp.server.sse import SseServerTransport
from mcp.server import NotificationOptions, InitializationOptions
import mcp.types as types

from my_mcp_server.server import app as mcp_app

logger = logging.getLogger("my_mcp_server.main")
logger.setLevel(logging.INFO)

fastapi_app = FastAPI(
    title="My MCP Server (Browser-Use)",
    description="HTTP-based SSE for MCP communication with browser automation",
    version="0.1.0",
)

# SSE transport endpoints
transport = SseServerTransport("/message")


async def sse_endpoint(request: Request):
    """
    SSE endpoint to handle server -> client streaming.
    """
    async def event_stream():
        async with transport.connect_sse(request.scope, request.receive, None) as streams:
            await mcp_app.run(
                streams[0],
                streams[1],
                InitializationOptions(
                    server_name="my_mcp_server_sse",
                    server_version="0.1.0",
                    capabilities=mcp_app.get_capabilities(
                        notification_options=NotificationOptions()
                    ),
                ),
            )
    
    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    )


async def message_endpoint(request: Request):
    """
    POST endpoint for JSON-RPC messages from client -> server.
    """
    return await transport.handle_post_message(request.scope, request.receive, None)


routes = [
    Route("/sse", endpoint=sse_endpoint, methods=["GET"]),
    Route("/message", endpoint=message_endpoint, methods=["POST"]),
]

for r in routes:
    fastapi_app.router.routes.append(r)


@fastapi_app.get("/")
async def root():
    return {
        "message": "Welcome to the Browser-Use MCP Server! Connect to /sse for SSE, and /message for JSON-RPC."
    }


app = fastapi_app


def main():
    """
    For uvicorn-based startup
    """
    import uvicorn

    uvicorn.run("my_mcp_server.main:app", host="127.0.0.1", port=8031, reload=False)


if __name__ == "__main__":
    main()
```

---

_**Assistant**_



Key changes made:
1. Switched back to HTTP routes instead of WebSocket
2. Used `StreamingResponse` for SSE endpoint with proper headers
3. Created an `event_stream` async generator for streaming
4. Removed the `send` parameter from transport calls since we'll handle sending through the streaming response
5. Added proper SSE headers for caching and connection

Let's try running the server again:

---

_**Assistant**_

```
uv run python run.py
```

---

_**Assistant**_



---



---


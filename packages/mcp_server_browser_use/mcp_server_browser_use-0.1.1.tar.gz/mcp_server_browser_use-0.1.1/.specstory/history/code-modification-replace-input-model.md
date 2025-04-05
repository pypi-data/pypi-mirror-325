## SpecStory

## Code Modification: Replace Input Model (17/01/2025, 21:04:16)

_**User**_

remove RunBrowserAgentInput and replace input with two args

---

_**Assistant**_

I'll modify the code to replace the `RunBrowserAgentInput` Pydantic model with direct arguments in the function.

---

_**Assistant**_

```
// ... existing code ...
class RunBrowserAgentInput(BaseModel):
    task: str
    add_infos: str = ""


@app.tool("run-browser-agent")
async def run_browser_agent(task: str, add_infos: str = "") -> List[TextContent]:
    """Handle run-browser-agent tool calls."""
    global _global_agent, _global_browser, _global_browser_context, _global_agent_state

    try:
        # Clear any previous agent stop signals
        _global_agent_state.clear_stop()
// ... existing code ...
```

---

_**Assistant**_



I'll make one more edit to remove the `RunBrowserAgentInput` class since it's no longer needed:

---

_**Assistant**_

```
import os
import traceback
from typing import Any, Dict, List

from browser_use import BrowserConfig
from browser_use.browser.context import BrowserContextConfig
from fastmcp import FastMCP
from mcp.types import Resource, TextContent, Tool
from pydantic import AnyUrl, BaseModel

from mcp_server_browser_use.agent.custom_agent import CustomAgent
from mcp_server_browser_use.browser.custom_browser import CustomBrowser
from mcp_server_browser_use.controller.custom_controller import CustomController
from mcp_server_browser_use.utils import utils
from mcp_server_browser_use.utils.agent_state import AgentState

# Global references for single "running agent" approach
_global_agent = None
_global_browser = None
_global_browser_context = None
_global_agent_state = AgentState()

app = FastMCP(title="browser-automation", version="0.1.0")


@app.tool("run-browser-agent")
// ... existing code ...
```

---

_**Assistant**_



I've made the requested changes:
1. Removed the `RunBrowserAgentInput` Pydantic model
2. Modified the `run_browser_agent` function to take `task` and `add_infos` as direct arguments
3. Updated the function body to use these direct arguments instead of accessing them through the input model

The function now has a cleaner interface and can be called directly with the required arguments.

---



---


## SpecStory

## Fixing Relative Imports in Project (17/01/2025, 20:58:10)

_**User**_

@src fix all relative imports

---

_**Assistant**_

I'll help fix all relative imports in the project. First, let me check the current state of imports in the source files.

---

_**Assistant**_



---

_**Assistant**_



Let me check the project structure to ensure we make the correct absolute imports.

---

_**Assistant**_



---

_**Assistant**_



I'll now fix all relative imports to use absolute imports. I'll do this file by file:

1. First, let's fix `custom_context.py`:

---

_**Assistant**_

```
// ... existing code ...
from mcp_server_browser_use.browser.config import BrowserPersistenceConfig
// ... existing code ...
```

---

_**Assistant**_



2. Let's fix `custom_browser.py`:

---

_**Assistant**_

```
// ... existing code ...
from mcp_server_browser_use.browser.config import BrowserPersistenceConfig
from mcp_server_browser_use.browser.custom_context import CustomBrowserContext
// ... existing code ...
```

---

_**Assistant**_







3. Let's fix `server.py`:

---

_**Assistant**_

```
// ... existing code ...
from mcp_server_browser_use.agent.custom_agent import CustomAgent
from mcp_server_browser_use.browser.custom_browser import CustomBrowser
from mcp_server_browser_use.controller.custom_controller import CustomController
from mcp_server_browser_use.utils import utils
from mcp_server_browser_use.utils.agent_state import AgentState
// ... existing code ...
```

---

_**Assistant**_







4. Let's fix `custom_prompts.py`:

---

_**Assistant**_

```
// ... existing code ...
from mcp_server_browser_use.agent.custom_views import CustomAgentStepInfo
// ... existing code ...
```

---

_**Assistant**_











5. Let's fix `custom_massage_manager.py`:

---

_**Assistant**_

```
// ... existing code ...
from mcp_server_browser_use.agent.custom_prompts import CustomAgentMessagePrompt
// ... existing code ...
```

---

_**Assistant**_











6. Let's fix `custom_agent.py`:

---

_**Assistant**_

```
// ... existing code ...
from mcp_server_browser_use.utils.agent_state import AgentState
from mcp_server_browser_use.agent.custom_massage_manager import CustomMassageManager
from mcp_server_browser_use.agent.custom_views import CustomAgentOutput, CustomAgentStepInfo
// ... existing code ...
```

---

_**Assistant**_















7. Finally, let's fix `__init__.py`:

---

_**Assistant**_

```
"""MCP server for browser-use"""

from mcp_server_browser_use.server import app

__version__ = "0.1.0"
```

---

_**Assistant**_



All relative imports have been replaced with absolute imports. The changes maintain the same functionality while making the imports more explicit and less prone to issues with relative path resolution. Each import now uses the full package path starting with `mcp_server_browser_use`.

---



---


## SpecStory

## Disable Logs to Stdout (17/01/2025, 14:48:53)

_**User**_

disable any logs to stdout that is done by libraries. don't edit app.request_context.session.send_log_message(

---

_**Assistant**_

I'll help disable library logs to stdout while keeping the app's request context logging. I'll search for any logging configuration in the codebase first.

---

_**Assistant**_



---

_**Assistant**_



Let me add logging configuration to disable stdout logs from libraries while keeping our app's request context logging. I'll edit the server.py file:

---

_**Assistant**_

```
import asyncio
from typing import Any, Dict, List, Optional
from contextlib import closing
from pydantic import AnyUrl
import logging

# Disable all library logs to stdout
logging.getLogger().setLevel(logging.CRITICAL)
logging.getLogger('asyncio').setLevel(logging.CRITICAL)
logging.getLogger('browser_use').setLevel(logging.CRITICAL)
logging.getLogger('playwright').setLevel(logging.CRITICAL)
logging.getLogger('langchain').setLevel(logging.CRITICAL)
logging.getLogger('openai').setLevel(logging.CRITICAL)

import mcp.types as types
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio

# browser-use imports
// ... existing code ...
```

---

_**Assistant**_



I've added logging configuration at the top of the file that:
1. Disables root logger by setting it to CRITICAL level
2. Specifically disables logs from key libraries we use:
   - asyncio
   - browser_use
   - playwright (used by browser_use)
   - langchain
   - openai

This will prevent any library logs from going to stdout while preserving our app's request context logging which uses a separate mechanism.

---



---


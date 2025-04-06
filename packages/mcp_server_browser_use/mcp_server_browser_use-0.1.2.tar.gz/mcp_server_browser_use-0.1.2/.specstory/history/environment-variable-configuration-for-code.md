## SpecStory

## Environment Variable Configuration for Code (17/01/2025, 15:22:37)

_**User**_

here are available envs, use appropriate in code:
"""
        "OPENAI_ENDPOINT": "https://api.openai.com/v1",
        "OPENAI_API_KEY": "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",
        "ANTHROPIC_API_KEY": "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",
        "GOOGLE_API_KEY": "AIzaSyAb-Z1DuKe8CE-MBCEEBTgM0WmB2ZeVf90",
        "DEEPSEEK_ENDPOINT": "https://api.deepseek.com",
        "DEEPSEEK_API_KEY": "sk-e6d0034c6b3b486797cff7500e60ebb1",
        "ANONYMIZED_TELEMETRY": "false",
        "BROWSER_USE_LOGGING_LEVEL": "info",
        "CHROME_PATH": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "CHROME_USER_DATA": "/Users/igortarasenko/Library/Application Support/Google/Chrome/Default",
        "CHROME_DEBUGGING_PORT": "9222",
        "CHROME_DEBUGGING_HOST": "localhost",
        "CHROME_PERSISTENT_SESSION": "true",
        "RESOLUTION": "1920x1080x24",
        "RESOLUTION_WIDTH": "1920",
        "RESOLUTION_HEIGHT": "1080",
        "VNC_PASSWORD": "youvncpassword"
"""

---

_**Assistant**_

I'll help modify the code to use these environment variables. The main changes will be in the `browser_launch` and `llm_configure` tool handlers. Let me make those changes:

---

_**Assistant**_

```
import os
from typing import Any, Dict, List, Optional
from contextlib import closing
from pydantic import AnyUrl
import mcp.types as types
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio

# browser-use imports
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.agent.service import Agent
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

# Environment variables
CHROME_PATH = os.getenv("CHROME_PATH", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
CHROME_USER_DATA = os.getenv("CHROME_USER_DATA")
CHROME_DEBUGGING_PORT = int(os.getenv("CHROME_DEBUGGING_PORT", "9222"))
CHROME_DEBUGGING_HOST = os.getenv("CHROME_DEBUGGING_HOST", "localhost")
CHROME_PERSISTENT_SESSION = os.getenv("CHROME_PERSISTENT_SESSION", "true").lower() == "true"
RESOLUTION_WIDTH = int(os.getenv("RESOLUTION_WIDTH", "1920"))
RESOLUTION_HEIGHT = int(os.getenv("RESOLUTION_HEIGHT", "1080"))
OPENAI_ENDPOINT = os.getenv("OPENAI_ENDPOINT", "https://api.openai.com/v1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
// ... existing code ...

@app.call_tool()
async def call_tool_handler(
    name: str, arguments: Dict[str, Any]
) -> List[types.TextContent]:
    safe_log("info", f"Handling tool call: {name} with arguments: {arguments}")
    try:
        if name == "browser_launch":
            safe_log("info", "Launching browser with configuration")
            headless = arguments.get("headless", False)
            disable_security = arguments.get("disableSecurity", False)
            window_size = arguments.get("windowSize", {
                "width": RESOLUTION_WIDTH,
                "height": RESOLUTION_HEIGHT
            })
            chrome_path = arguments.get("chromePath", CHROME_PATH)
            persist_session = arguments.get("persistSession", CHROME_PERSISTENT_SESSION)
            load_timeouts = arguments.get("loadTimeouts", {"min": 1, "max": 10})

            safe_log(
                "debug",
                f"Browser config: headless={headless}, disable_security={disable_security}, "
                f"window_size={window_size}, chrome_path={chrome_path}, "
                f"persist_session={persist_session}, load_timeouts={load_timeouts}"
            )

            state.browser = Browser(
                config=BrowserConfig(
                    headless=headless,
                    disable_security=disable_security,
                    chrome_instance_path=chrome_path if chrome_path else None,
                    new_context_config={
                        "viewport": window_size,
                        "user_data_dir": CHROME_USER_DATA if persist_session else None,
                        "debugging_port": CHROME_DEBUGGING_PORT,
                        "debugging_host": CHROME_DEBUGGING_HOST,
                    }
                )
            )
// ... existing code ...

        elif name == "llm_configure":
            safe_log("info", "Configuring LLM")
            provider = arguments.get("provider", "openai")
            model = arguments.get("model", "gpt-3.5-turbo")
            api_key = arguments.get("apiKey", OPENAI_API_KEY)
            base_url = arguments.get("baseUrl", OPENAI_ENDPOINT)
            api_version = arguments.get("apiVersion", "")

            safe_log(
                "debug",
                f"LLM config: provider={provider}, model={model}, "
                f"base_url={base_url}, api_version={api_version}"
            )

            state.llm = ChatOpenAI(
                api_key=SecretStr(api_key),
                base_url=base_url,
                model=model,
                api_version=api_version,
            )
// ... rest of existing code ...
```

---

_**Assistant**_



I've updated the code to use the environment variables you provided. Key changes:

1. Added environment variable imports at the top
2. Set default values for Chrome configuration:
   - Chrome path
   - User data directory
   - Debugging port/host
   - Persistent session flag
   - Resolution settings
3. Updated browser launch configuration to use these values
4. Set OpenAI endpoint and API key defaults for LLM configuration

The code will now use these environment variables by default, but still allows overriding them through the tool arguments if needed.

---



---


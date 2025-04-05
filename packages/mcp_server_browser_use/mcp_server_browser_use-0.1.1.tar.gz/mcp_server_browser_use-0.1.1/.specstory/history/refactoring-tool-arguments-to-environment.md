## SpecStory

## Refactoring Tool Arguments to Environment (17/01/2025, 19:54:32)

_**User**_

refactor to move following args from tool to env:
                    "model_provider": {"type": "string"},
                    "model_name": {"type": "string"},
                    "temperature": {"type": "number"},
                    "max_steps": {"type": "integer"},
                    "use_vision": {"type": "boolean"},
                    "max_actions_per_step": {"type": "integer"},
                    "tool_call_in_content": {"type": "boolean"},

---

_**Assistant**_

I'll help you move those arguments from the tool's input schema to environment variables. I'll need to modify both the schema definition and how these values are extracted in the handler.

Let me edit the file:

---

_**Assistant**_

```
// ... existing code ...
                "properties": {
                    "task": {"type": "string"},
                    "add_infos": {"type": "string"},
                },
                "required": ["task"],
// ... existing code ...
        task = arguments.get("task", "")
        add_infos = arguments.get("add_infos", "")
        model_provider = os.getenv("MCP_MODEL_PROVIDER", "openai")
        model_name = os.getenv("MCP_MODEL_NAME", "gpt-4")
        temperature = float(os.getenv("MCP_TEMPERATURE", "0.7"))
        max_steps = int(os.getenv("MCP_MAX_STEPS", "15"))
        use_vision = os.getenv("MCP_USE_VISION", "true").lower() == "true"
        max_actions_per_step = int(os.getenv("MCP_MAX_ACTIONS_PER_STEP", "5"))
        tool_call_in_content = os.getenv("MCP_TOOL_CALL_IN_CONTENT", "true").lower() == "true"
// ... existing code ...
```

---

_**Assistant**_



I've made the following changes:
1. Removed the arguments from the tool's input schema
2. Changed all the argument extractions to use environment variables with the `MCP_` prefix
3. Added proper type conversion and default values for each environment variable

The new environment variables are:
- `MCP_MODEL_PROVIDER` (default: "openai")
- `MCP_MODEL_NAME` (default: "gpt-4")
- `MCP_TEMPERATURE` (default: "0.7")
- `MCP_MAX_STEPS` (default: "15")
- `MCP_USE_VISION` (default: "true")
- `MCP_MAX_ACTIONS_PER_STEP` (default: "5")
- `MCP_TOOL_CALL_IN_CONTENT` (default: "true")

---



---


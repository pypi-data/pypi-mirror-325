## SpecStory

## Refactoring Code to Localize Browser (17/01/2025, 21:47:01)

_**User**_

find issue:

==> /Users/igortarasenko/Library/Logs/Claude/mcp-server-browser-use.log <==
ERROR:browser_use.agent.service:❌ Result failed 1/5 times:
 Invalid model output format. Please follow the correct schema.
Details: 5 validation errors for AgentOutput
current_state.prev_action_evaluation
  Field required [type=missing, input_value={'evaluation_previous_goa...provided search terms.'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
current_state.important_contents
  Field required [type=missing, input_value={'evaluation_previous_goa...provided search terms.'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
current_state.completed_contents
  Field required [type=missing, input_value={'evaluation_previous_goa...provided search terms.'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
current_state.thought
  Field required [type=missing, input_value={'evaluation_previous_goa...provided search terms.'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
current_state.summary
  Field required [type=missing, input_value={'evaluation_previous_goa...provided search terms.'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
Error running MCP server: unhandled errors in a TaskGroup (1 sub-exception)
  + Exception Group Traceback (most recent call last):
  |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/mcp/server/stdio.py", line 83, in stdio_server
  |     yield read_stream, write_stream
  |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/fastmcp/server.py", line 422, in run_stdio_async
  |     await self._mcp_server.run(
  |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/mcp/server/lowlevel/server.py", line 424, in run
  |     async with ServerSession(
  |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/mcp/shared/session.py", line 122, in __aexit__
  |     return await self._task_group.__aexit__(exc_type, exc_val, exc_tb)
  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 767, in __aexit__
  |     raise BaseExceptionGroup(
  | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/mcp/shared/session.py", line 235, in _receive_loop
    |     notification = self._receive_notification_type.model_validate(
    |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/pydantic/main.py", line 627, in model_validate
    |     return cls.__pydantic_validator__.validate_python(
    |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    | pydantic_core._pydantic_core.ValidationError: 5 validation errors for ClientNotification
    | ProgressNotification.method
    |   Input should be 'notifications/progress' [type=literal_error, input_value='cancelled', input_type=str]
    |     For further information visit https://errors.pydantic.dev/2.10/v/literal_error
    | ProgressNotification.params.progressToken
    |   Field required [type=missing, input_value={'requestId': 18, 'reason... -2: Request timed out'}, input_type=dict]
    |     For further information visit https://errors.pydantic.dev/2.10/v/missing
    | ProgressNotification.params.progress
    |   Field required [type=missing, input_value={'requestId': 18, 'reason... -2: Request timed out'}, input_type=dict]
    |     For further information visit https://errors.pydantic.dev/2.10/v/missing
    | InitializedNotification.method
    |   Input should be 'notifications/initialized' [type=literal_error, input_value='cancelled', input_type=str]
    |     For further information visit https://errors.pydantic.dev/2.10/v/literal_error
    | RootsListChangedNotification.method
    |   Input should be 'notifications/roots/list_changed' [type=literal_error, input_value='cancelled', input_type=str]
    |     For further information visit https://errors.pydantic.dev/2.10/v/literal_error
    +------------------------------------

During handling of the above exception, another exception occurred:

  + Exception Group Traceback (most recent call last):
  |   File "/Users/igortarasenko/Projects/mcp-browser-use/src/mcp_server_browser_use/server.py", line 143, in main
  |     app.run()
  |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/fastmcp/server.py", line 128, in run
  |     asyncio.run(self.run_stdio_async())
  |   File "/opt/homebrew/Cellar/python@3.11/3.11.11/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/runners.py", line 190, in run
  |     return runner.run(main)
  |            ^^^^^^^^^^^^^^^^
  |   File "/opt/homebrew/Cellar/python@3.11/3.11.11/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/runners.py", line 118, in run
  |     return self._loop.run_until_complete(task)
  |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |   File "/opt/homebrew/Cellar/python@3.11/3.11.11/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
  |     return future.result()
  |            ^^^^^^^^^^^^^^^
  |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/fastmcp/server.py", line 421, in run_stdio_async
  |     async with stdio_server() as (read_stream, write_stream):
  |   File "/opt/homebrew/Cellar/python@3.11/3.11.11/Frameworks/Python.framework/Versions/3.11/lib/python3.11/contextlib.py", line 231, in __aexit__
  |     await self.gen.athrow(typ, value, traceback)
  |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/mcp/server/stdio.py", line 80, in stdio_server
  |     async with anyio.create_task_group() as tg:
  |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 767, in __aexit__
  |     raise BaseExceptionGroup(
  | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception)
  +-+---------------- 1 ----------------
    | Traceback (most recent call last):
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/anyio/streams/memory.py", line 242, in send
    |     self.send_nowait(item)
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/anyio/streams/memory.py", line 225, in send_nowait
    |     raise WouldBlock
    | anyio.WouldBlock
    |
    | During handling of the above exception, another exception occurred:
    |
    | Traceback (most recent call last):
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/mcp/server/lowlevel/server.py", line 466, in run
    |     await message.respond(response)
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/mcp/shared/session.py", line 58, in respond
    |     await self._session._send_response(
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/mcp/shared/session.py", line 205, in _send_response
    |     await self._write_stream.send(JSONRPCMessage(jsonrpc_response))
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/anyio/streams/memory.py", line 248, in send
    |     await send_event.wait()
    |   File "/opt/homebrew/Cellar/python@3.11/3.11.11/Frameworks/Python.framework/Versions/3.11/lib/python3.11/asyncio/locks.py", line 213, in wait
    |     await fut
    | asyncio.exceptions.CancelledError: Cancelled by cancel scope 10ccfa810
    |
    | During handling of the above exception, another exception occurred:
    |
    | Exception Group Traceback (most recent call last):
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/mcp/server/stdio.py", line 83, in stdio_server
    |     yield read_stream, write_stream
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/fastmcp/server.py", line 422, in run_stdio_async
    |     await self._mcp_server.run(
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/mcp/server/lowlevel/server.py", line 424, in run
    |     async with ServerSession(
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/mcp/shared/session.py", line 122, in __aexit__
    |     return await self._task_group.__aexit__(exc_type, exc_val, exc_tb)
    |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/anyio/_backends/_asyncio.py", line 767, in __aexit__
    |     raise BaseExceptionGroup(
    | ExceptionGroup: unhandled errors in a TaskGroup (1 sub-exception)
    +-+---------------- 1 ----------------
      | Traceback (most recent call last):
      |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/mcp/shared/session.py", line 235, in _receive_loop
      |     notification = self._receive_notification_type.model_validate(
      |                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      |   File "/Users/igortarasenko/Projects/mcp-browser-use/.venv/lib/python3.11/site-packages/pydantic/main.py", line 627, in model_validate
      |     return cls.__pydantic_validator__.validate_python(
      |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      | pydantic_core._pydantic_core.ValidationError: 5 validation errors for ClientNotification
      | ProgressNotification.method
      |   Input should be 'notifications/progress' [type=literal_error, input_value='cancelled', input_type=str]
      |     For further information visit https://errors.pydantic.dev/2.10/v/literal_error
      | ProgressNotification.params.progressToken
      |   Field required [type=missing, input_value={'requestId': 18, 'reason... -2: Request timed out'}, input_type=dict]
      |     For further information visit https://errors.pydantic.dev/2.10/v/missing
      | ProgressNotification.params.progress
      |   Field required [type=missing, input_value={'requestId': 18, 'reason... -2: Request timed out'}, input_type=dict]
      |     For further information visit https://errors.pydantic.dev/2.10/v/missing
      | InitializedNotification.method
      |   Input should be 'notifications/initialized' [type=literal_error, input_value='cancelled', input_type=str]
      |     For further information visit https://errors.pydantic.dev/2.10/v/literal_error
      | RootsListChangedNotification.method
      |   Input should be 'notifications/roots/list_changed' [type=literal_error, input_value='cancelled', input_type=str]
      |     For further information visit https://errors.pydantic.dev/2.10/v/literal_error
      +------------------------------------


---

_**Assistant**_

Let me check the code and error logs to identify the issue.

The error shows validation failures in the agent output format. The key issue is that required fields are missing in the agent's output state. Let me search for the relevant code.

---

_**Assistant**_



---

_**Assistant**_



Let me check the custom agent implementation:

---

_**Assistant**_



---

_**Assistant**_



Let me check the custom views implementation:

---

_**Assistant**_



---

_**Assistant**_



The issue appears to be in the agent output validation. The error shows that required fields are missing in the agent's output state. Looking at the code:

1. The `CustomAgentBrain` model requires these fields:
   - prev_action_evaluation
   - important_contents 
   - completed_contents
   - thought
   - summary

2. The error shows that these fields are missing in the output, suggesting the LLM response isn't properly formatted.

The issue is likely in the LLM response parsing in `get_next_action()` method. When the structured output fails, the fallback JSON parsing isn't properly validating the required fields.

Here's what's happening:

1. The LLM response doesn't include all required fields in the `current_state` object
2. The validation fails because these fields are required by the `CustomAgentBrain` model
3. The error propagates up through the MCP server

To fix this, you need to:

1. Check the LLM prompt to ensure it's instructed to include all required fields
2. Add validation in the fallback JSON parsing
3. Or make the fields optional in the `CustomAgentBrain` model if they're not strictly required

Let me check the prompt:

---

_**Assistant**_



---

_**Assistant**_



The issue is in the LLM response handling. Looking at the code:

1. The prompt correctly specifies all required fields in the response format
2. However, in `get_next_action()`, when the structured output fails, the fallback JSON parsing isn't properly handling the response format

Here's the fix needed in `get_next_action()` in `custom_agent.py`:

---

_**Assistant**_

```
```python
// ... existing code ...
            # If something goes wrong, try to invoke the LLM again without structured output,
            # and Manually parse the response. Temporarily solution for DeepSeek
            ret = self.llm.invoke(input_messages)
            if isinstance(ret.content, list):
                content = ret.content[0].replace("```json", "").replace("```", "")
            else:
                content = ret.content.replace("```json", "").replace("```", "")
                
            try:
                parsed_json = json.loads(content)
                # Ensure all required fields are present
                required_fields = ["prev_action_evaluation", "important_contents", "completed_contents", "thought", "summary"]
                current_state = parsed_json.get("current_state", {})
                for field in required_fields:
                    if field not in current_state:
                        current_state[field] = ""  # Provide empty string as default
                parsed_json["current_state"] = current_state
                parsed: AgentOutput = self.AgentOutput(**parsed_json)
            except json.JSONDecodeError:
                raise ValueError(f"Could not parse response as JSON: {content}")
            except Exception as e:
                raise ValueError(f"Could not parse response: {str(e)}\nContent: {content}")
                
            if parsed is None:
                raise ValueError(f"Could not parse response.")
// ... existing code ...
```
```

---

_**Assistant**_



This fix:

1. Adds proper error handling for JSON parsing
2. Ensures all required fields are present in the `current_state` object
3. Provides empty strings as defaults for missing fields
4. Gives more detailed error messages when parsing fails

The changes should resolve the validation errors you're seeing. The agent will now properly handle cases where the LLM response is missing some of the required fields by providing empty string defaults, while still maintaining the required structure of the `CustomAgentBrain` model.

Try running the agent again - it should now handle the LLM responses properly without validation errors.

---



---


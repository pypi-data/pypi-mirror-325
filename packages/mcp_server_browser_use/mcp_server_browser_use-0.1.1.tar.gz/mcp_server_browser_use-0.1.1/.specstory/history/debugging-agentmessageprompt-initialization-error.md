## SpecStory

## Debugging AgentMessagePrompt Initialization Error (12/01/2025, 23:48:54)

_**User**_

diff --git a/README.md b/README.md
index 7f010dc..03e9ff4 100644
--- a/README.md
+++ b/README.md
@@ -2,77 +2,72 @@
 
 <br/>
 
-
 # browser-use MCP server
 [![Documentation](https://img.shields.io/badge/Documentation-📕-blue)](https://docs.browser-use.com)
 [![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
 
-MCP server for browser-use - a powerful browser automation system that enables AI agents to interact with web browsers through natural language.
+> **Project Note**: This MCP server implementation builds upon the [browser-use/web-ui](https://github.com/browser-use/web-ui) foundation. Core browser automation logic and configuration patterns are adapted from the original project.
 
-## Features
-
-- 🤖 **AI-Driven Browser Control**: Natural language interface for browser automation
-- 🔍 **Smart Navigation**: Intelligent webpage analysis and interaction
-- 📸 **Visual Understanding**: Vision-based element detection and interaction
-- 🔄 **State Management**: Persistent browser sessions and context management
-- 🛠️ **Extensible**: Custom browser automation capabilities
-- 🤝 **MCP Integration**: Seamless integration with Model Context Protocol
+AI-driven browser automation server implementing the Model Context Protocol (MCP) for natural language browser control.
 
 <a href="https://glama.ai/mcp/servers/dz6dy5hw59"><img width="380" height="200" src="https://glama.ai/mcp/servers/dz6dy5hw59/badge" alt="Browser-Use Server MCP server" /></a>
 
-## Components
+## Features
 
-### Resources
+- 🧠 **MCP Integration** - Full protocol implementation for AI agent communication
+- 🌐 **Browser Automation** - Page navigation, form filling, and element interaction
+- 👁️ **Visual Understanding** - Screenshot analysis and vision-based interactions
+- 🔄 **State Persistence** - Maintain browser sessions between tasks
+- 🔌 **Multi-LLM Support** - OpenAI, Anthropic, Azure, DeepSeek integration
 
-The server implements a browser automation system with:
-- Integration with browser-use library for advanced browser control
-- Custom browser automation capabilities
-- Agent-based interaction system with vision capabilities
-- Persistent state management
-- Customizable model settings
+## Quick Start
 
-### Requirements
+### Prerequisites
 
 - Python 3.11 or higher
 - uv (fast Python package installer)
 - Chrome/Chromium browser
 
-### Quick Start
+### Installation
 
 #### Claude Desktop
 
 On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
 On Windows: `%APPDATA%/Claude/claude_desktop_config.json`
 
-<details>
-  <summary>Development Configuration</summary>
-
 ```json
 "mcpServers": {
-    "mcp_server_browser_use": {
+    "browser-use": {
       "command": "uvx",
       "args": [
         "mcp-server-browser-use",
       ],
       "env": {
+        "OPENROUTER_API_KEY": "",
+        "OPENROUTER_ENDPOINT": "https://openrouter.ai/api/v1",
         "OPENAI_ENDPOINT": "https://api.openai.com/v1",
         "OPENAI_API_KEY": "",
+        "ANTHROPIC_ENDPOINT": "https://api.anthropic.com",
         "ANTHROPIC_API_KEY": "",
         "GOOGLE_API_KEY": "",
         "AZURE_OPENAI_ENDPOINT": "",
         "AZURE_OPENAI_API_KEY": "",
         "DEEPSEEK_ENDPOINT": "https://api.deepseek.com",
         "DEEPSEEK_API_KEY": "",
-        # Set to false to disable anonymized telemetry
+        "MISTRAL_API_KEY": "",
+        "MISTRAL_ENDPOINT": "https://api.mistral.ai/v1",
+        "OLLAMA_ENDPOINT": "http://localhost:11434",
         "ANONYMIZED_TELEMETRY": "true",
-        # Chrome settings
+        "BROWSER_USE_LOGGING_LEVEL": "info",
         "CHROME_PATH": "",
         "CHROME_USER_DATA": "",
         "CHROME_DEBUGGING_PORT": "9222",
         "CHROME_DEBUGGING_HOST": "localhost",
-        # Set to true to keep browser open between AI tasks
         "CHROME_PERSISTENT_SESSION": "false",
-        # Model settings
+        "RESOLUTION": "1920x1080x24",
+        "RESOLUTION_WIDTH": "1920",
+        "RESOLUTION_HEIGHT": "1080",
+        "VNC_PASSWORD": "youvncpassword",
         "MCP_MODEL_PROVIDER": "anthropic",
         "MCP_MODEL_NAME": "claude-3-5-sonnet-20241022",
         "MCP_TEMPERATURE": "0.3",
@@ -83,80 +78,65 @@ On Windows: `%APPDATA%/Claude/claude_desktop_config.json`
     }
 }
 ```
-</details>
 
-### Environment Variables
+### Local Development
 
-Key environment variables:
-
-```bash
-# API Keys
-OPENAI_API_KEY=your_openai_key
-ANTHROPIC_API_KEY=your_anthropic_key
-
-# Chrome Configuration
-CHROME_PATH=/path/to/chrome  # Optional: Path to Chrome executable
-CHROME_USER_DATA=/path/to/user/data  # Optional: Chrome user data directory
-CHROME_DEBUGGING_PORT=9222  # Default: 9222
-CHROME_DEBUGGING_HOST=localhost  # Default: localhost
-CHROME_PERSISTENT_SESSION=false  # Keep browser open between tasks
-
-# Model Settings
-MCP_MODEL_PROVIDER=anthropic  # Options: anthropic, openai, azure, deepseek
-MCP_MODEL_NAME=claude-3-5-sonnet-20241022
-MCP_TEMPERATURE=0.3
-MCP_MAX_STEPS=30
-MCP_USE_VISION=true
-MCP_MAX_ACTIONS_PER_STEP=5
+```json
+"browser-use": {
+  "command": "uv",
+  "args": [
+    "--directory",
+    "/path/to/mcp-browser-use",
+    "run",
+    "mcp-server-browser-use"
+  ],
+  "env": {
+    ...
+  }
+}
 ```
 
 ## Development
 
-### Setup
-
-1. Clone the repository:
-```bash
-git clone https://github.com/saik0s/mcp-browser-use.git
-cd mcp-browser-use
-```
-
-2. Create and activate virtual environment:
-```bash
-python -m venv .venv
-source .venv/bin/activate  # On Windows: .venv\Scripts\activate
-```
-
-3. Install dependencies:
 ```bash
+# Install dev dependencies
 uv sync
-```
 
-### Debugging
+# Run with debugger
+npx @modelcontextprotocol/inspector uv --directory . run mcp-server-browser-use
+```
 
-For debugging, use the [MCP Inspector](https://github.com/modelcontextprotocol/inspector):
+## Troubleshooting
 
-```bash
-npx @modelcontextprotocol/inspector uv --directory /path/to/project run mcp-server-browser-use
-```
+-   **Browser Conflicts**: Close all Chrome instances before starting.
+-   **API Errors**: Verify API keys in environment variables match your LLM provider.
+-   **Vision Support**: Ensure `MCP_USE_VISION=true` for screenshot analysis.
 
-The Inspector will display a URL for the debugging interface.
+## Provider Configuration
 
-## Browser Actions
+The server supports multiple LLM providers through environment variables. Here are the available options for `MCP_MODEL_PROVIDER`:
 
-The server supports various browser actions through natural language:
+| Provider | Value | Required Env Variables |
+|----------|--------|----------------------|
+| Anthropic | `anthropic` | `ANTHROPIC_API_KEY`<br>`ANTHROPIC_ENDPOINT` (optional) |
+| OpenAI | `openai` | `OPENAI_API_KEY`<br>`OPENAI_ENDPOINT` (optional) |
+| Azure OpenAI | `azure_openai` | `AZURE_OPENAI_API_KEY`<br>`AZURE_OPENAI_ENDPOINT` |
+| DeepSeek | `deepseek` | `DEEPSEEK_API_KEY`<br>`DEEPSEEK_ENDPOINT` (optional) |
+| Gemini | `gemini` | `GOOGLE_API_KEY` |
+| Mistral | `mistral` | `MISTRAL_API_KEY`<br>`MISTRAL_ENDPOINT` (optional) |
+| Ollama | `ollama` | `OLLAMA_ENDPOINT` (optional, defaults to localhost:11434) |
+| OpenRouter | `openrouter` | `OPENROUTER_API_KEY`<br>`OPENROUTER_ENDPOINT` (optional) |
 
-- Navigation: Go to URLs, back/forward, refresh
-- Interaction: Click, type, scroll, hover
-- Forms: Fill forms, submit, select options
-- State: Get page content, take screenshots
-- Tabs: Create, close, switch between tabs
-- Vision: Find elements by visual appearance
-- Cookies & Storage: Manage browser state
+### Notes:
+- For endpoints marked as optional, default values will be used if not specified
+- Temperature can be configured using `MCP_TEMPERATURE` (default: 0.3)
+- Model can be specified using `MCP_MODEL_NAME`
+- For Ollama models, additional context settings like `num_ctx` and `num_predict` are configurable
 
-## Contributing
+## Credits
 
-Contributions are welcome! Please feel free to submit a Pull Request.
+This project extends the [browser-use/web-ui](https://github.com/browser-use/web-ui) under MIT License. Special thanks to the original authors for their browser automation framework.
 
 ## License
 
-This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
+MIT - See [LICENSE](LICENSE) for details.
diff --git a/pyproject.toml b/pyproject.toml
index cfd3809..6be3fc2 100644
--- a/pyproject.toml
+++ b/pyproject.toml
@@ -17,7 +17,6 @@ classifiers = [
 
 dependencies = [
     "fastmcp>=0.4.1",
-    "browser-use==0.1.19",
     "langchain>=0.3.14",
     "langchain-openai>=0.2.14",
     "pydantic>=2.10.5",
@@ -28,6 +27,9 @@ dependencies = [
     "pyperclip>=1.9.0",
     "langchain-ollama>=0.2.2",
     "instructor>=1.7.2",
+    "browser-use==0.1.29",
+    "json-repair>=0.35.0",
+    "langchain-mistralai>=0.2.6",
 ]
 
 [build-system]
diff --git a/src/mcp_server_browser_use/agent/__init__.py b/src/mcp_server_browser_use/agent/__init__.py
index 93fbe7f..e69de29 100644
--- a/src/mcp_server_browser_use/agent/__init__.py
+++ b/src/mcp_server_browser_use/agent/__init__.py
@@ -1,6 +0,0 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/1
-# @Author  : wenshao
-# @Email   : wenshaoguo1026@gmail.com
-# @Project : browser-use-webui
-# @FileName: __init__.py.py
diff --git a/src/mcp_server_browser_use/agent/custom_agent.py b/src/mcp_server_browser_use/agent/custom_agent.py
index 04c1751..cb76626 100644
--- a/src/mcp_server_browser_use/agent/custom_agent.py
+++ b/src/mcp_server_browser_use/agent/custom_agent.py
@@ -1,28 +1,22 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/2
-# @Author  : wenshao
-# @ProjectName: browser-use-webui
-# @FileName: custom_agent.py
-
 import json
 import logging
 import pdb
 import traceback
-from typing import Optional, Type
+from typing import Optional, Type, List, Dict, Any, Callable
 from PIL import Image, ImageDraw, ImageFont
 import os
 import base64
 import io
-
-from browser_use.agent.prompts import SystemPrompt
+import platform
+from browser_use.agent.prompts import SystemPrompt, AgentMessagePrompt
 from browser_use.agent.service import Agent
 from browser_use.agent.views import (
     ActionResult,
+    ActionModel,
     AgentHistoryList,
     AgentOutput,
     AgentHistory,
 )
-from browser_use.agent.message_manager.views import MessageHistory, ManagedMessage
 from browser_use.browser.browser import Browser
 from browser_use.browser.context import BrowserContext
 from browser_use.browser.views import BrowserStateHistory
@@ -30,28 +24,23 @@ from browser_use.controller.service import Controller
 from browser_use.telemetry.views import (
     AgentEndTelemetryEvent,
     AgentRunTelemetryEvent,
-    AgentStepErrorTelemetryEvent,
+    AgentStepTelemetryEvent,
 )
 from browser_use.utils import time_execution_async
 from langchain_core.language_models.chat_models import BaseChatModel
 from langchain_core.messages import (
     BaseMessage,
 )
-from langchain_openai import ChatOpenAI
-from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
-from langchain_openai.chat_models.base import _convert_message_to_dict
+from json_repair import repair_json
 from mcp_server_browser_use.utils.agent_state import AgentState
-from mcp_server_browser_use.agent.custom_massage_manager import CustomMassageManager
-from mcp_server_browser_use.agent.custom_views import (
-    CustomAgentOutput,
-    CustomAgentStepInfo,
-)
+
+from .custom_massage_manager import CustomMassageManager
+from .custom_views import CustomAgentOutput, CustomAgentStepInfo
 
 logger = logging.getLogger(__name__)
 
 
 class CustomAgent(Agent):
-
     def __init__(
         self,
         task: str,
@@ -65,7 +54,8 @@ class CustomAgent(Agent):
         max_failures: int = 5,
         retry_delay: int = 10,
         system_prompt_class: Type[SystemPrompt] = SystemPrompt,
-        max_input_tokens: int = 13000,
+        agent_prompt_class: Type[AgentMessagePrompt] = AgentMessagePrompt,
+        max_input_tokens: int = 128000,
         validate_output: bool = False,
         include_attributes: list[str] = [
             "title",
@@ -83,6 +73,13 @@ class CustomAgent(Agent):
         max_actions_per_step: int = 10,
         tool_call_in_content: bool = True,
         agent_state: AgentState = None,
+        initial_actions: Optional[List[Dict[str, Dict[str, Any]]]] = None,
+        # Cloud Callbacks
+        register_new_step_callback: (
+            Callable[["BrowserState", "AgentOutput", int], None] | None
+        ) = None,
+        register_done_callback: Callable[["AgentHistoryList"], None] | None = None,
+        tool_calling_method: Optional[str] = "auto",
     ):
         super().__init__(
             task=task,
@@ -101,19 +98,38 @@ class CustomAgent(Agent):
             max_error_length=max_error_length,
             max_actions_per_step=max_actions_per_step,
             tool_call_in_content=tool_call_in_content,
+            initial_actions=initial_actions,
+            register_new_step_callback=register_new_step_callback,
+            register_done_callback=register_done_callback,
+            tool_calling_method=tool_calling_method,
         )
+        if self.model_name in ["deepseek-reasoner"] or "deepseek-r1" in self.model_name:
+            # deepseek-reasoner does not support function calling
+            self.use_deepseek_r1 = True
+            # deepseek-reasoner only support 64000 context
+            self.max_input_tokens = 64000
+        else:
+            self.use_deepseek_r1 = False
+
+        # record last actions
+        self._last_actions = None
+        # record extract content
+        self.extracted_content = ""
+        # custom new info
         self.add_infos = add_infos
+        # agent_state for Stop
         self.agent_state = agent_state
+        self.agent_prompt_class = agent_prompt_class
         self.message_manager = CustomMassageManager(
             llm=self.llm,
             task=self.task,
             action_descriptions=self.controller.registry.get_prompt_description(),
             system_prompt_class=self.system_prompt_class,
+            agent_prompt_class=agent_prompt_class,
             max_input_tokens=self.max_input_tokens,
             include_attributes=self.include_attributes,
             max_error_length=self.max_error_length,
             max_actions_per_step=self.max_actions_per_step,
-            tool_call_in_content=tool_call_in_content,
         )
 
     def _setup_action_models(self) -> None:
@@ -134,7 +150,8 @@ class CustomAgent(Agent):
 
         logger.info(f"{emoji} Eval: {response.current_state.prev_action_evaluation}")
         logger.info(f"🧠 New Memory: {response.current_state.important_contents}")
-        logger.info(f"⏳ Task Progress: {response.current_state.completed_contents}")
+        logger.info(f"⏳ Task Progress: \n{response.current_state.task_progress}")
+        logger.info(f"📋 Future Plans: \n{response.current_state.future_plans}")
         logger.info(f"🤔 Thought: {response.current_state.thought}")
         logger.info(f"🎯 Summary: {response.current_state.summary}")
         for i, action in enumerate(response.action):
@@ -160,193 +177,293 @@ class CustomAgent(Agent):
         ):
             step_info.memory += important_contents + "\n"
 
-        completed_contents = model_output.current_state.completed_contents
-        if completed_contents and "None" not in completed_contents:
-            step_info.task_progress = completed_contents
+        task_progress = model_output.current_state.task_progress
+        if task_progress and "None" not in task_progress:
+            step_info.task_progress = task_progress
+
+        future_plans = model_output.current_state.future_plans
+        if future_plans and "None" not in future_plans:
+            step_info.future_plans = future_plans
 
     @time_execution_async("--get_next_action")
     async def get_next_action(self, input_messages: list[BaseMessage]) -> AgentOutput:
         """Get next action from LLM based on current state"""
-        logger.info("Getting next action from LLM")
-        logger.debug(f"Input messages: {input_messages}")
-
-        try:
-            if isinstance(self.llm, ChatOpenAI):
-                try:
-                    logger.info("Using OpenAI chat model")
-                    import instructor
-
-                    client = instructor.from_openai(self.llm.root_async_client)
-                    logger.debug(f"Using model: {self.llm.model_name}")
-                    messages = [
-                        _convert_message_to_dict(message) for message in input_messages
-                    ]
-                    parsed = await client.chat.completions.create(
-                        messages=messages,
-                        model=self.llm.model_name,
-                        response_model=self.AgentOutput,
-                    )
-                    logger.debug(f"Raw OpenAI response: {parsed}")
-                except Exception as e:
-                    logger.error(f"Error getting structured output: {str(e)}")
-                    logger.info(f"Using default structured output")
-                    structured_llm = self.llm.with_structured_output(
-                        self.AgentOutput, include_raw=True
-                    )
-                    response: dict[str, Any] = await structured_llm.ainvoke(input_messages)  # type: ignore
-                    logger.debug(f"Raw LLM response: {response}")
-                    parsed: AgentOutput = response["parsed"]
-            else:
-                logger.info(f"Using non-OpenAI model: {type(self.llm).__name__}")
-                structured_llm = self.llm.with_structured_output(
-                    self.AgentOutput, include_raw=True
-                )
-                response: dict[str, Any] = await structured_llm.ainvoke(input_messages)  # type: ignore
-                logger.debug(f"Raw LLM response: {response}")
-                parsed: AgentOutput = response["parsed"]
-
-            # cut the number of actions to max_actions_per_step
-            original_action_count = len(parsed.action)
-            parsed.action = parsed.action[: self.max_actions_per_step]
-            if original_action_count > self.max_actions_per_step:
-                logger.warning(
-                    f"Truncated actions from {original_action_count} to {self.max_actions_per_step}"
-                )
-
-            self._log_response(parsed)
-            self.n_steps += 1
-            logger.info(f"Successfully got next action. Step count: {self.n_steps}")
-
-            return parsed
-        except Exception as e:
-            logger.warning(f"Error getting structured output: {str(e)}")
-            logger.info("Attempting fallback to manual parsing")
-
-            try:
-                ret = self.llm.invoke(input_messages)
-                logger.debug(f"Raw fallback response: {ret}")
-
-                if isinstance(ret.content, list):
-                    logger.debug("Parsing list content")
-                    parsed_json = json.loads(
-                        ret.content[0].replace("```json", "").replace("```", "")
-                    )
-                else:
-                    logger.debug("Parsing string content")
-                    parsed_json = json.loads(
-                        ret.content.replace("```json", "").replace("```", "")
-                    )
-
-                parsed: AgentOutput = self.AgentOutput(**parsed_json)
-                if parsed is None:
-                    raise ValueError(f"Could not parse response.")
-
-                # cut the number of actions to max_actions_per_step
-                original_action_count = len(parsed.action)
-                parsed.action = parsed.action[: self.max_actions_per_step]
-                if original_action_count > self.max_actions_per_step:
-                    logger.warning(
-                        f"Truncated actions from {original_action_count} to {self.max_actions_per_step}"
-                    )
-
-                self._log_response(parsed)
-                self.n_steps += 1
-                logger.info(
-                    f"Successfully got next action via fallback. Step count: {self.n_steps}"
-                )
-
-                return parsed
-            except Exception as parse_error:
-                logger.error(f"Fallback parsing failed: {str(parse_error)}")
-                raise
-
-    def summarize_messages(self):
-        """Summarize message history if it exceeds 5 messages."""
-        stored_messages = self.message_manager.get_messages()
-        message_count = len(stored_messages)
-
-        if message_count <= 5:
-            logger.debug("Message count <= 5, skipping summarization")
-            return False
-
-        logger.info(f"Summarizing {message_count} messages")
-        try:
-            summarization_prompt = ChatPromptTemplate.from_messages(
-                [
-                    MessagesPlaceholder(variable_name="chat_history"),
-                    (
-                        "user",
-                        "Distill the above chat messages into a single summary message. Include as many specific details as you can.",
-                    ),
-                ]
-            )
-            summarization_chain = summarization_prompt | self.llm
-
-            summary_message = summarization_chain.invoke(
-                {"chat_history": stored_messages}
-            )
-            logger.debug(f"Generated summary: {summary_message}")
-
-            self.message_manager.history = MessageHistory(
-                messages=[ManagedMessage(message=summary_message)]
-            )
-
-            return True
-
-        except Exception as e:
-            logger.error(f"Error during message summarization: {str(e)}")
-            logger.debug(f"Full traceback: {traceback.format_exc()}")
-            raise
+        messages_to_process = (
+            self.message_manager.merge_successive_human_messages(input_messages)
+            if self.use_deepseek_r1
+            else input_messages
+        )
+
+        ai_message = self.llm.invoke(messages_to_process)
+        self.message_manager._add_message_with_tokens(ai_message)
+
+        if self.use_deepseek_r1:
+            logger.info("🤯 Start Deep Thinking: ")
+            logger.info(ai_message.reasoning_content)
+            logger.info("🤯 End Deep Thinking")
+
+        if isinstance(ai_message.content, list):
+            ai_content = ai_message.content[0]
+        else:
+            ai_content = ai_message.content
+
+        ai_content = ai_content.replace("```json", "").replace("```", "")
+        ai_content = repair_json(ai_content)
+        parsed_json = json.loads(ai_content)
+        parsed: AgentOutput = self.AgentOutput(**parsed_json)
+
+        if parsed is None:
+            logger.debug(ai_message.content)
+            raise ValueError("Could not parse response.")
+
+        # Limit actions to maximum allowed per step
+        parsed.action = parsed.action[: self.max_actions_per_step]
+        self._log_response(parsed)
+        self.n_steps += 1
+
+        return parsed
 
     @time_execution_async("--step")
     async def step(self, step_info: Optional[CustomAgentStepInfo] = None) -> None:
         """Execute one step of the task"""
         logger.info(f"\n📍 Step {self.n_steps}")
-        logger.info(f"History token count: {self.message_manager.history.total_tokens}")
-        # self.summarize_messages()
         state = None
         model_output = None
         result: list[ActionResult] = []
 
         try:
             state = await self.browser_context.get_state(use_vision=self.use_vision)
-            self.message_manager.add_state_message(state, self._last_result, step_info)
+            self.message_manager.add_state_message(
+                state, self._last_actions, self._last_result, step_info
+            )
             input_messages = self.message_manager.get_messages()
-            model_output = await self.get_next_action(input_messages)
-            self.update_step_info(model_output, step_info)
-            logger.info(f"🧠 All Memory: {step_info.memory}")
-            self._save_conversation(input_messages, model_output)
-            self.message_manager._remove_last_state_message()  # we dont want the whole state in the chat history
-            self.message_manager.add_model_output(model_output)
+            try:
+                model_output = await self.get_next_action(input_messages)
+                if self.register_new_step_callback:
+                    self.register_new_step_callback(state, model_output, self.n_steps)
+                self.update_step_info(model_output, step_info)
+                logger.info(f"🧠 All Memory: \n{step_info.memory}")
+                self._save_conversation(input_messages, model_output)
+                if self.model_name != "deepseek-reasoner":
+                    # remove prev message
+                    self.message_manager._remove_state_message_by_index(-1)
+            except Exception as e:
+                # model call failed, remove last state message from history
+                self.message_manager._remove_state_message_by_index(-1)
+                raise e
 
+            actions: list[ActionModel] = model_output.action
             result: list[ActionResult] = await self.controller.multi_act(
-                model_output.action, self.browser_context
+                actions, self.browser_context
             )
+            if len(result) != len(actions):
+                # I think something changes, such information should let LLM know
+                for ri in range(len(result), len(actions)):
+                    result.append(
+                        ActionResult(
+                            extracted_content=None,
+                            include_in_memory=True,
+                            error=f"{actions[ri].model_dump_json(exclude_unset=True)} is Failed to execute. \
+                                                    Something new appeared after action {actions[len(result) - 1].model_dump_json(exclude_unset=True)}",
+                            is_done=False,
+                        )
+                    )
+            if len(actions) == 0:
+                # TODO: fix no action case
+                result = [
+                    ActionResult(
+                        is_done=True,
+                        extracted_content=step_info.memory,
+                        include_in_memory=True,
+                    )
+                ]
+            for ret_ in result:
+                if "Extracted page" in ret_.extracted_content:
+                    # record every extracted page
+                    self.extracted_content += ret_.extracted_content
             self._last_result = result
-
+            self._last_actions = actions
             if len(result) > 0 and result[-1].is_done:
+                if not self.extracted_content:
+                    self.extracted_content = step_info.memory
+                result[-1].extracted_content = self.extracted_content
                 logger.info(f"📄 Result: {result[-1].extracted_content}")
 
             self.consecutive_failures = 0
 
         except Exception as e:
-            result = self._handle_step_error(e)
+            result = await self._handle_step_error(e)
             self._last_result = result
 
         finally:
+            actions = (
+                [a.model_dump(exclude_unset=True) for a in model_output.action]
+                if model_output
+                else []
+            )
+            self.telemetry.capture(
+                AgentStepTelemetryEvent(
+                    agent_id=self.agent_id,
+                    step=self.n_steps,
+                    actions=actions,
+                    consecutive_failures=self.consecutive_failures,
+                    step_error=(
+                        [r.error for r in result if r.error]
+                        if result
+                        else ["No result"]
+                    ),
+                )
+            )
             if not result:
                 return
-            for r in result:
-                if r.error:
-                    self.telemetry.capture(
-                        AgentStepErrorTelemetryEvent(
-                            agent_id=self.agent_id,
-                            error=r.error,
-                        )
-                    )
+
             if state:
                 self._make_history_item(model_output, state, result)
 
+    async def run(self, max_steps: int = 100) -> AgentHistoryList:
+        """Execute the task with maximum number of steps"""
+        try:
+            self._log_agent_run()
+
+            # Execute initial actions if provided
+            if self.initial_actions:
+                result = await self.controller.multi_act(
+                    self.initial_actions,
+                    self.browser_context,
+                    check_for_new_elements=False,
+                )
+                self._last_result = result
+
+            step_info = CustomAgentStepInfo(
+                task=self.task,
+                add_infos=self.add_infos,
+                step_number=1,
+                max_steps=max_steps,
+                memory="",
+                task_progress="",
+                future_plans="",
+            )
+
+            for step in range(max_steps):
+                # 1) Check if stop requested
+                if self.agent_state and self.agent_state.is_stop_requested():
+                    logger.info("🛑 Stop requested by user")
+                    self._create_stop_history_item()
+                    break
+
+                # 2) Store last valid state before step
+                if self.browser_context and self.agent_state:
+                    state = await self.browser_context.get_state(
+                        use_vision=self.use_vision
+                    )
+                    self.agent_state.set_last_valid_state(state)
+
+                if self._too_many_failures():
+                    break
+
+                # 3) Do the step
+                await self.step(step_info)
+
+                if self.history.is_done():
+                    if (
+                        self.validate_output and step < max_steps - 1
+                    ):  # if last step, we dont need to validate
+                        if not await self._validate_output():
+                            continue
+
+                    logger.info("✅ Task completed successfully")
+                    break
+            else:
+                logger.info("❌ Failed to complete task in maximum steps")
+                if not self.extracted_content:
+                    self.history.history[-1].result[
+                        -1
+                    ].extracted_content = step_info.memory
+                else:
+                    self.history.history[-1].result[
+                        -1
+                    ].extracted_content = self.extracted_content
+
+            return self.history
+
+        finally:
+            self.telemetry.capture(
+                AgentEndTelemetryEvent(
+                    agent_id=self.agent_id,
+                    success=self.history.is_done(),
+                    steps=self.n_steps,
+                    max_steps_reached=self.n_steps >= max_steps,
+                    errors=self.history.errors(),
+                )
+            )
+
+            if not self.injected_browser_context:
+                await self.browser_context.close()
+
+            if not self.injected_browser and self.browser:
+                await self.browser.close()
+
+            if self.generate_gif:
+                output_path: str = "agent_history.gif"
+                if isinstance(self.generate_gif, str):
+                    output_path = self.generate_gif
+
+                self.create_history_gif(output_path=output_path)
+
+    def _create_stop_history_item(self):
+        """Create a history item for when the agent is stopped."""
+        try:
+            # Attempt to retrieve the last valid state from agent_state
+            state = None
+            if self.agent_state:
+                last_state = self.agent_state.get_last_valid_state()
+                if last_state:
+                    # Convert to BrowserStateHistory
+                    state = BrowserStateHistory(
+                        url=getattr(last_state, "url", ""),
+                        title=getattr(last_state, "title", ""),
+                        tabs=getattr(last_state, "tabs", []),
+                        interacted_element=[None],
+                        screenshot=getattr(last_state, "screenshot", None),
+                    )
+                else:
+                    state = self._create_empty_state()
+            else:
+                state = self._create_empty_state()
+
+            # Create a final item in the agent history indicating done
+            stop_history = AgentHistory(
+                model_output=None,
+                state=state,
+                result=[ActionResult(extracted_content=None, error=None, is_done=True)],
+            )
+            self.history.history.append(stop_history)
+
+        except Exception as e:
+            logger.error(f"Error creating stop history item: {e}")
+            # Create empty state as fallback
+            state = self._create_empty_state()
+            stop_history = AgentHistory(
+                model_output=None,
+                state=state,
+                result=[ActionResult(extracted_content=None, error=None, is_done=True)],
+            )
+            self.history.history.append(stop_history)
+
+    def _convert_to_browser_state_history(self, browser_state):
+        return BrowserStateHistory(
+            url=getattr(browser_state, "url", ""),
+            title=getattr(browser_state, "title", ""),
+            tabs=getattr(browser_state, "tabs", []),
+            interacted_element=[None],
+            screenshot=getattr(browser_state, "screenshot", None),
+        )
+
+    def _create_empty_state(self):
+        return BrowserStateHistory(
+            url="", title="", tabs=[], interacted_element=[None], screenshot=None
+        )
+
     def create_history_gif(
         self,
         output_path: str = "agent_history.gif",
@@ -379,8 +496,6 @@ class CustomAgent(Agent):
 
             for font_name in font_options:
                 try:
-                    import platform
-
                     if platform.system() == "Windows":
                         # Need to specify the abs font path on Windows
                         font_name = os.path.join(
@@ -464,130 +579,3 @@ class CustomAgent(Agent):
             logger.info(f"Created GIF at {output_path}")
         else:
             logger.warning("No images found in history to create GIF")
-
-    async def run(self, max_steps: int = 100) -> AgentHistoryList:
-        """Execute the task with maximum number of steps"""
-        try:
-            logger.info(f"🚀 Starting task: {self.task}")
-
-            self.telemetry.capture(
-                AgentRunTelemetryEvent(
-                    agent_id=self.agent_id,
-                    task=self.task,
-                )
-            )
-
-            step_info = CustomAgentStepInfo(
-                task=self.task,
-                add_infos=self.add_infos,
-                step_number=1,
-                max_steps=max_steps,
-                memory="",
-                task_progress="",
-            )
-
-            for step in range(max_steps):
-                # 1) Check if stop requested
-                if self.agent_state and self.agent_state.is_stop_requested():
-                    logger.info("🛑 Stop requested by user")
-                    self._create_stop_history_item()
-                    break
-
-                # 2) Store last valid state before step
-                if self.browser_context and self.agent_state:
-                    state = await self.browser_context.get_state(
-                        use_vision=self.use_vision
-                    )
-                    self.agent_state.set_last_valid_state(state)
-
-                if self._too_many_failures():
-                    break
-
-                # 3) Do the step
-                await self.step(step_info)
-
-                if self.history.is_done():
-                    if (
-                        self.validate_output and step < max_steps - 1
-                    ):  # if last step, we dont need to validate
-                        if not await self._validate_output():
-                            continue
-
-                    logger.info("✅ Task completed successfully")
-                    break
-            else:
-                logger.info("❌ Failed to complete task in maximum steps")
-
-            return self.history
-
-        finally:
-            self.telemetry.capture(
-                AgentEndTelemetryEvent(
-                    agent_id=self.agent_id,
-                    task=self.task,
-                    success=self.history.is_done(),
-                    steps=len(self.history.history),
-                )
-            )
-            if not self.injected_browser_context:
-                await self.browser_context.close()
-
-            if not self.injected_browser and self.browser:
-                await self.browser.close()
-
-            if self.generate_gif:
-                self.create_history_gif()
-
-    def _create_stop_history_item(self):
-        """Create a history item for when the agent is stopped."""
-        try:
-            # Attempt to retrieve the last valid state from agent_state
-            state = None
-            if self.agent_state:
-                last_state = self.agent_state.get_last_valid_state()
-                if last_state:
-                    # Convert to BrowserStateHistory
-                    state = BrowserStateHistory(
-                        url=getattr(last_state, "url", ""),
-                        title=getattr(last_state, "title", ""),
-                        tabs=getattr(last_state, "tabs", []),
-                        interacted_element=[None],
-                        screenshot=getattr(last_state, "screenshot", None),
-                    )
-                else:
-                    state = self._create_empty_state()
-            else:
-                state = self._create_empty_state()
-
-            # Create a final item in the agent history indicating done
-            stop_history = AgentHistory(
-                model_output=None,
-                state=state,
-                result=[ActionResult(extracted_content=None, error=None, is_done=True)],
-            )
-            self.history.history.append(stop_history)
-
-        except Exception as e:
-            logger.error(f"Error creating stop history item: {e}")
-            # Create empty state as fallback
-            state = self._create_empty_state()
-            stop_history = AgentHistory(
-                model_output=None,
-                state=state,
-                result=[ActionResult(extracted_content=None, error=None, is_done=True)],
-            )
-            self.history.history.append(stop_history)
-
-    def _convert_to_browser_state_history(self, browser_state):
-        return BrowserStateHistory(
-            url=getattr(browser_state, "url", ""),
-            title=getattr(browser_state, "title", ""),
-            tabs=getattr(browser_state, "tabs", []),
-            interacted_element=[None],
-            screenshot=getattr(browser_state, "screenshot", None),
-        )
-
-    def _create_empty_state(self):
-        return BrowserStateHistory(
-            url="", title="", tabs=[], interacted_element=[None], screenshot=None
-        )
diff --git a/src/mcp_server_browser_use/agent/custom_massage_manager.py b/src/mcp_server_browser_use/agent/custom_massage_manager.py
index 3bd941c..f39c999 100644
--- a/src/mcp_server_browser_use/agent/custom_massage_manager.py
+++ b/src/mcp_server_browser_use/agent/custom_massage_manager.py
@@ -1,9 +1,3 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/2
-# @Author  : wenshao
-# @ProjectName: browser-use-webui
-# @FileName: custom_massage_manager.py
-
 from __future__ import annotations
 
 import logging
@@ -11,16 +5,21 @@ from typing import List, Optional, Type
 
 from browser_use.agent.message_manager.service import MessageManager
 from browser_use.agent.message_manager.views import MessageHistory
-from browser_use.agent.prompts import SystemPrompt
-from browser_use.agent.views import ActionResult, AgentStepInfo
+from browser_use.agent.prompts import SystemPrompt, AgentMessagePrompt
+from browser_use.agent.views import ActionResult, AgentStepInfo, ActionModel
 from browser_use.browser.views import BrowserState
 from langchain_core.language_models import BaseChatModel
+from langchain_anthropic import ChatAnthropic
+from langchain_core.language_models import BaseChatModel
 from langchain_core.messages import (
-    HumanMessage,
-    AIMessage
+	AIMessage,
+	BaseMessage,
+	HumanMessage,
+    ToolMessage
 )
-
-from mcp_server_browser_use.agent.custom_prompts import CustomAgentMessagePrompt
+from langchain_openai import ChatOpenAI
+from ..utils.llm import DeepSeekR1ChatOpenAI
+from .custom_prompts import CustomAgentMessagePrompt
 
 logger = logging.getLogger(__name__)
 
@@ -32,13 +31,14 @@ class CustomMassageManager(MessageManager):
             task: str,
             action_descriptions: str,
             system_prompt_class: Type[SystemPrompt],
+            agent_prompt_class: Type[AgentMessagePrompt],
             max_input_tokens: int = 128000,
-            estimated_tokens_per_character: int = 3,
+            estimated_characters_per_token: int = 3,
             image_tokens: int = 800,
             include_attributes: list[str] = [],
             max_error_length: int = 400,
             max_actions_per_step: int = 10,
-            tool_call_in_content: bool = False,
+            message_context: Optional[str] = None
     ):
         super().__init__(
             llm=llm,
@@ -46,76 +46,72 @@ class CustomMassageManager(MessageManager):
             action_descriptions=action_descriptions,
             system_prompt_class=system_prompt_class,
             max_input_tokens=max_input_tokens,
-            estimated_tokens_per_character=estimated_tokens_per_character,
+            estimated_characters_per_token=estimated_characters_per_token,
             image_tokens=image_tokens,
             include_attributes=include_attributes,
             max_error_length=max_error_length,
             max_actions_per_step=max_actions_per_step,
-            tool_call_in_content=tool_call_in_content,
+            message_context=message_context
         )
-
+        self.agent_prompt_class = agent_prompt_class
         # Custom: Move Task info to state_message
         self.history = MessageHistory()
         self._add_message_with_tokens(self.system_prompt)
-        tool_calls = [
-            {
-                'name': 'CustomAgentOutput',
-                'args': {
-                    'current_state': {
-                        'prev_action_evaluation': 'Unknown - No previous actions to evaluate.',
-                        'important_contents': '',
-                        'completed_contents': '',
-                        'thought': 'Now Google is open. Need to type OpenAI to search.',
-                        'summary': 'Type OpenAI to search.',
-                    },
-                    'action': [],
-                },
-                'id': '',
-                'type': 'tool_call',
-            }
-        ]
-        if self.tool_call_in_content:
-            # openai throws error if tool_calls are not responded -> move to content
-            example_tool_call = AIMessage(
-                content=f'{tool_calls}',
-                tool_calls=[],
-            )
-        else:
-            example_tool_call = AIMessage(
-                content=f'',
-                tool_calls=tool_calls,
-            )
-
-        self._add_message_with_tokens(example_tool_call)
+        
+        if self.message_context:
+            context_message = HumanMessage(content=self.message_context)
+            self._add_message_with_tokens(context_message)
 
+    def cut_messages(self):
+        """Get current message list, potentially trimmed to max tokens"""
+        diff = self.history.total_tokens - self.max_input_tokens
+        min_message_len = 2 if self.message_context is not None else 1
+        
+        while diff > 0 and len(self.history.messages) > min_message_len:
+            self.history.remove_message(min_message_len) # alway remove the oldest message
+            diff = self.history.total_tokens - self.max_input_tokens
+        
     def add_state_message(
             self,
             state: BrowserState,
+            actions: Optional[List[ActionModel]] = None,
             result: Optional[List[ActionResult]] = None,
             step_info: Optional[AgentStepInfo] = None,
     ) -> None:
         """Add browser state as human message"""
-
-        # if keep in memory, add to directly to history and add state without result
-        if result:
-            for r in result:
-                if r.include_in_memory:
-                    if r.extracted_content:
-                        msg = HumanMessage(content=str(r.extracted_content))
-                        self._add_message_with_tokens(msg)
-                    if r.error:
-                        msg = HumanMessage(
-                            content=str(r.error)[-self.max_error_length:]
-                        )
-                        self._add_message_with_tokens(msg)
-                    result = None  # if result in history, we dont want to add it again
-
         # otherwise add state message and result to next message (which will not stay in memory)
-        state_message = CustomAgentMessagePrompt(
+        state_message = self.agent_prompt_class(
             state,
+            actions,
             result,
             include_attributes=self.include_attributes,
             max_error_length=self.max_error_length,
             step_info=step_info,
         ).get_user_message()
         self._add_message_with_tokens(state_message)
+    
+    def _count_text_tokens(self, text: str) -> int:
+        if isinstance(self.llm, (ChatOpenAI, ChatAnthropic, DeepSeekR1ChatOpenAI)):
+            try:
+                tokens = self.llm.get_num_tokens(text)
+            except Exception:
+                tokens = (
+					len(text) // self.estimated_characters_per_token
+				)  # Rough estimate if no tokenizer available
+        else:
+            tokens = (
+				len(text) // self.estimated_characters_per_token
+			)  # Rough estimate if no tokenizer available
+        return tokens
+
+    def _remove_state_message_by_index(self, remove_ind=-1) -> None:
+        """Remove last state message from history"""
+        i = len(self.history.messages) - 1
+        remove_cnt = 0
+        while i >= 0:
+            if isinstance(self.history.messages[i].message, HumanMessage): 
+                remove_cnt += 1
+            if remove_cnt == abs(remove_ind):
+                self.history.remove_message(i)
+                break
+            i -= 1
\ No newline at end of file
diff --git a/src/mcp_server_browser_use/agent/custom_prompts.py b/src/mcp_server_browser_use/agent/custom_prompts.py
index 4877b2a..fcb0721 100644
--- a/src/mcp_server_browser_use/agent/custom_prompts.py
+++ b/src/mcp_server_browser_use/agent/custom_prompts.py
@@ -1,17 +1,13 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/2
-# @Author  : wenshao
-# @ProjectName: browser-use-webui
-# @FileName: custom_prompts.py
-
+import pdb
 from typing import List, Optional
 
-from browser_use.agent.prompts import SystemPrompt
-from browser_use.agent.views import ActionResult
+from browser_use.agent.prompts import SystemPrompt, AgentMessagePrompt
+from browser_use.agent.views import ActionResult, ActionModel
 from browser_use.browser.views import BrowserState
 from langchain_core.messages import HumanMessage, SystemMessage
+from datetime import datetime
 
-from mcp_server_browser_use.agent.custom_views import CustomAgentStepInfo
+from .custom_views import CustomAgentStepInfo
 
 
 class CustomSystemPrompt(SystemPrompt):
@@ -19,27 +15,23 @@ class CustomSystemPrompt(SystemPrompt):
         """
         Returns the important rules for the agent.
         """
-        text = """
+        text = r"""
     1. RESPONSE FORMAT: You must ALWAYS respond with valid JSON in this exact format:
        {
          "current_state": {
            "prev_action_evaluation": "Success|Failed|Unknown - Analyze the current elements and the image to check if the previous goals/actions are successful like intended by the task. Ignore the action result. The website is the ground truth. Also mention if something unexpected happened like new suggestions in an input field. Shortly state why/why not. Note that the result you output must be consistent with the reasoning you output afterwards. If you consider it to be 'Failed,' you should reflect on this during your thought.",
-           "important_contents": "Output important contents closely related to user\'s instruction or task on the current page. If there is, please output the contents. If not, please output empty string ''.",
-           "completed_contents": "Update the input Task Progress. Completed contents is a general summary of the current contents that have been completed. Just summarize the contents that have been actually completed based on the current page and the history operations. Please list each completed item individually, such as: 1. Input username. 2. Input Password. 3. Click confirm button",
-           "thought": "Think about the requirements that have been completed in previous operations and the requirements that need to be completed in the next one operation. If the output of prev_action_evaluation is 'Failed', please reflect and output your reflection here. If you think you have entered the wrong page, consider to go back to the previous page in next action.",
+           "important_contents": "Output important contents closely related to user\'s instruction on the current page. If there is, please output the contents. If not, please output empty string ''.",
+           "task_progress": "Task Progress is a general summary of the current contents that have been completed. Just summarize the contents that have been actually completed based on the content at current step and the history operations. Please list each completed item individually, such as: 1. Input username. 2. Input Password. 3. Click confirm button. Please return string type not a list.",
+           "future_plans": "Based on the user's request and the current state, outline the remaining steps needed to complete the task. This should be a concise list of actions yet to be performed, such as: 1. Select a date. 2. Choose a specific time slot. 3. Confirm booking. Please return string type not a list.",
+           "thought": "Think about the requirements that have been completed in previous operations and the requirements that need to be completed in the next one operation. If your output of prev_action_evaluation is 'Failed', please reflect and output your reflection here.",
            "summary": "Please generate a brief natural language description for the operation in next actions based on your Thought."
          },
          "action": [
-           {
-             "action_name": {
-               // action-specific parameters
-             }
-           },
-           // ... more actions in sequence
+           * actions in sequences, please refer to **Common action sequences**. Each output action MUST be formated as: \{action_name\: action_params\}* 
          ]
        }
 
-    2. ACTIONS: You can specify multiple actions to be executed in sequence.
+    2. ACTIONS: You can specify multiple actions to be executed in sequence. 
 
        Common action sequences:
        - Form filling: [
@@ -48,7 +40,6 @@ class CustomSystemPrompt(SystemPrompt):
            {"click_element": {"index": 3}}
          ]
        - Navigation and extraction: [
-           {"open_new_tab": {}},
            {"go_to_url": {"url": "https://example.com"}},
            {"extract_page_content": {}}
          ]
@@ -66,10 +57,11 @@ class CustomSystemPrompt(SystemPrompt):
        - Use scroll to find elements you are looking for
 
     5. TASK COMPLETION:
-       - If you think all the requirements of user\'s instruction have been completed and no further operation is required, output the done action to terminate the operation process.
+       - If you think all the requirements of user\'s instruction have been completed and no further operation is required, output the **Done** action to terminate the operation process.
        - Don't hallucinate actions.
        - If the task requires specific information - make sure to include everything in the done function. This is what the user will see.
        - If you are running out of steps (current step), think about speeding it up, and ALWAYS use the done action as the last action.
+       - Note that you must verify if you've truly fulfilled the user's request by examining the actual page content, not just by looking at the actions you output but also whether the action is executed successfully. Pay particular attention when errors occur during action execution.
 
     6. VISUAL CONTEXT:
        - When an image is provided, use it to understand the page layout
@@ -83,13 +75,13 @@ class CustomSystemPrompt(SystemPrompt):
        - If you fill an input field and your action sequence is interrupted, most often a list with suggestions poped up under the field and you need to first select the right element from the suggestion list.
 
     8. ACTION SEQUENCING:
-       - Actions are executed in the order they appear in the list
+       - Actions are executed in the order they appear in the list 
        - Each action should logically follow from the previous one
        - If the page changes after an action, the sequence is interrupted and you get the new state.
        - If content only disappears the sequence continues.
        - Only provide the action sequence until you think the page will change.
        - Try to be efficient, e.g. fill forms at once, or chain actions where nothing changes on the page like saving, extracting, checkboxes...
-       - only use multiple actions if it makes sense.
+       - only use multiple actions if it makes sense. 
     """
         text += f"   - use maximum {self.max_actions_per_step} actions per sequence"
         return text
@@ -100,10 +92,9 @@ class CustomSystemPrompt(SystemPrompt):
     1. Task: The user\'s instructions you need to complete.
     2. Hints(Optional): Some hints to help you complete the user\'s instructions.
     3. Memory: Important contents are recorded during historical operations for use in subsequent operations.
-    4. Task Progress: Up to the current page, the content you have completed can be understood as the progress of the task.
-    5. Current URL: The webpage you're currently on
-    6. Available Tabs: List of open browser tabs
-    7. Interactive Elements: List in the format:
+    4. Current URL: The webpage you're currently on
+    5. Available Tabs: List of open browser tabs
+    6. Interactive Elements: List in the format:
        index[:]<element_type>element_text</element_type>
        - index: Numeric identifier for interaction
        - element_type: HTML element type (button, input, etc.)
@@ -126,14 +117,10 @@ class CustomSystemPrompt(SystemPrompt):
         Returns:
             str: Formatted system prompt
         """
-        time_str = self.current_date.strftime("%Y-%m-%d %H:%M")
-
         AGENT_PROMPT = f"""You are a precise browser automation agent that interacts with websites through structured commands. Your role is to:
     1. Analyze the provided webpage elements and structure
     2. Plan a sequence of actions to accomplish the given task
-    3. Respond with valid JSON containing your action sequence and state assessment
-
-    Current date and time: {time_str}
+    3. Your final result MUST be a valid JSON as the **RESPONSE FORMAT** described, containing your action sequence and state assessment, No need extra content to expalin. 
 
     {self.input_format()}
 
@@ -146,47 +133,83 @@ class CustomSystemPrompt(SystemPrompt):
         return SystemMessage(content=AGENT_PROMPT)
 
 
-class CustomAgentMessagePrompt:
+class CustomAgentMessagePrompt(AgentMessagePrompt):
     def __init__(
             self,
             state: BrowserState,
+            actions: Optional[List[ActionModel]] = None,
             result: Optional[List[ActionResult]] = None,
             include_attributes: list[str] = [],
             max_error_length: int = 400,
             step_info: Optional[CustomAgentStepInfo] = None,
     ):
-        self.state = state
-        self.result = result
-        self.max_error_length = max_error_length
-        self.include_attributes = include_attributes
-        self.step_info = step_info
+        super(CustomAgentMessagePrompt, self).__init__(state=state, 
+                                                       result=result, 
+                                                       include_attributes=include_attributes, 
+                                                       max_error_length=max_error_length, 
+                                                       step_info=step_info
+                                                       )
+        self.actions = actions
 
     def get_user_message(self) -> HumanMessage:
+        if self.step_info:
+            step_info_description = f'Current step: {self.step_info.step_number}/{self.step_info.max_steps}\n'
+        else:
+            step_info_description = ''
+            
+        time_str = datetime.now().strftime("%Y-%m-%d %H:%M")
+        step_info_description += "Current date and time: {time_str}"
+
+        elements_text = self.state.element_tree.clickable_elements_to_string(include_attributes=self.include_attributes)
+
+        has_content_above = (self.state.pixels_above or 0) > 0
+        has_content_below = (self.state.pixels_below or 0) > 0
+
+        if elements_text != '':
+            if has_content_above:
+                elements_text = (
+                    f'... {self.state.pixels_above} pixels above - scroll or extract content to see more ...\n{elements_text}'
+                )
+            else:
+                elements_text = f'[Start of page]\n{elements_text}'
+            if has_content_below:
+                elements_text = (
+                    f'{elements_text}\n... {self.state.pixels_below} pixels below - scroll or extract content to see more ...'
+                )
+            else:
+                elements_text = f'{elements_text}\n[End of page]'
+        else:
+            elements_text = 'empty page'
+   
         state_description = f"""
-    1. Task: {self.step_info.task}
-    2. Hints(Optional):
-    {self.step_info.add_infos}
-    3. Memory:
-    {self.step_info.memory}
-    4. Task Progress:
-    {self.step_info.task_progress}
-    5. Current url: {self.state.url}
-    6. Available tabs:
-    {self.state.tabs}
-    7. Interactive elements:
-    {self.state.element_tree.clickable_elements_to_string(include_attributes=self.include_attributes)}
-            """
+{step_info_description}
+1. Task: {self.step_info.task}. 
+2. Hints(Optional): 
+{self.step_info.add_infos}
+3. Memory: 
+{self.step_info.memory}
+4. Current url: {self.state.url}
+5. Available tabs:
+{self.state.tabs}
+6. Interactive elements:
+{elements_text}
+        """
 
-        if self.result:
+        if self.actions and self.result:
+            state_description += "\n **Previous Actions** \n"
+            state_description += f'Previous step: {self.step_info.step_number-1}/{self.step_info.max_steps} \n'
             for i, result in enumerate(self.result):
-                if result.extracted_content:
-                    state_description += f"\nResult of action {i + 1}/{len(self.result)}: {result.extracted_content}"
-                if result.error:
-                    # only use last 300 characters of error
-                    error = result.error[-self.max_error_length:]
-                    state_description += (
-                        f"\nError of action {i + 1}/{len(self.result)}: ...{error}"
-                    )
+                action = self.actions[i]
+                state_description += f"Previous action {i + 1}/{len(self.result)}: {action.model_dump_json(exclude_unset=True)}\n"
+                if result.include_in_memory:
+                    if result.extracted_content:
+                        state_description += f"Result of previous action {i + 1}/{len(self.result)}: {result.extracted_content}\n"
+                    if result.error:
+                        # only use last 300 characters of error
+                        error = result.error[-self.max_error_length:]
+                        state_description += (
+                            f"Error of previous action {i + 1}/{len(self.result)}: ...{error}\n"
+                        )
 
         if self.state.screenshot:
             # Format message for vision model
@@ -202,4 +225,4 @@ class CustomAgentMessagePrompt:
                 ]
             )
 
-        return HumanMessage(content=state_description)
+        return HumanMessage(content=state_description)
\ No newline at end of file
diff --git a/src/mcp_server_browser_use/agent/custom_views.py b/src/mcp_server_browser_use/agent/custom_views.py
index 7bf46c0..d0dfb06 100644
--- a/src/mcp_server_browser_use/agent/custom_views.py
+++ b/src/mcp_server_browser_use/agent/custom_views.py
@@ -1,9 +1,3 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/2
-# @Author  : wenshao
-# @ProjectName: browser-use-webui
-# @FileName: custom_views.py
-
 from dataclasses import dataclass
 from typing import Type
 
@@ -20,6 +14,7 @@ class CustomAgentStepInfo:
     add_infos: str
     memory: str
     task_progress: str
+    future_plans: str
 
 
 class CustomAgentBrain(BaseModel):
@@ -27,7 +22,8 @@ class CustomAgentBrain(BaseModel):
 
     prev_action_evaluation: str
     important_contents: str
-    completed_contents: str
+    task_progress: str
+    future_plans: str
     thought: str
     summary: str
 
@@ -49,7 +45,7 @@ class CustomAgentOutput(AgentOutput):
     ) -> Type["CustomAgentOutput"]:
         """Extend actions with custom actions"""
         return create_model(
-            "AgentOutput",
+            "CustomAgentOutput",
             __base__=CustomAgentOutput,
             action=(
                 list[custom_actions],
diff --git a/src/mcp_server_browser_use/browser/__init__.py b/src/mcp_server_browser_use/browser/__init__.py
index 93fbe7f..e69de29 100644
--- a/src/mcp_server_browser_use/browser/__init__.py
+++ b/src/mcp_server_browser_use/browser/__init__.py
@@ -1,6 +0,0 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/1
-# @Author  : wenshao
-# @Email   : wenshaoguo1026@gmail.com
-# @Project : browser-use-webui
-# @FileName: __init__.py.py
diff --git a/src/mcp_server_browser_use/browser/config.py b/src/mcp_server_browser_use/browser/config.py
deleted file mode 100644
index 32329c4..0000000
--- a/src/mcp_server_browser_use/browser/config.py
+++ /dev/null
@@ -1,30 +0,0 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/6
-# @Author  : wenshao
-# @ProjectName: browser-use-webui
-# @FileName: config.py
-
-import os
-from dataclasses import dataclass
-from typing import Optional
-
-
-@dataclass
-class BrowserPersistenceConfig:
-    """Configuration for browser persistence"""
-
-    persistent_session: bool = False
-    user_data_dir: Optional[str] = None
-    debugging_port: Optional[int] = None
-    debugging_host: Optional[str] = None
-
-    @classmethod
-    def from_env(cls) -> "BrowserPersistenceConfig":
-        """Create config from environment variables"""
-        return cls(
-            persistent_session=os.getenv("CHROME_PERSISTENT_SESSION", "").lower()
-            == "true",
-            user_data_dir=os.getenv("CHROME_USER_DATA"),
-            debugging_port=int(os.getenv("CHROME_DEBUGGING_PORT", "9222")),
-            debugging_host=os.getenv("CHROME_DEBUGGING_HOST", "localhost"),
-        )
\ No newline at end of file
diff --git a/src/mcp_server_browser_use/browser/custom_browser.py b/src/mcp_server_browser_use/browser/custom_browser.py
index 19bcb65..661470e 100644
--- a/src/mcp_server_browser_use/browser/custom_browser.py
+++ b/src/mcp_server_browser_use/browser/custom_browser.py
@@ -1,26 +1,20 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/2
-# @Author  : wenshao
-# @ProjectName: browser-use-webui
-# @FileName: browser.py
-
 import asyncio
+import pdb
 
 from playwright.async_api import Browser as PlaywrightBrowser
 from playwright.async_api import (
-	BrowserContext as PlaywrightBrowserContext,
+    BrowserContext as PlaywrightBrowserContext,
 )
 from playwright.async_api import (
-	Playwright,
-	async_playwright,
+    Playwright,
+    async_playwright,
 )
 from browser_use.browser.browser import Browser
 from browser_use.browser.context import BrowserContext, BrowserContextConfig
 from playwright.async_api import BrowserContext as PlaywrightBrowserContext
 import logging
 
-from mcp_server_browser_use.browser.config import BrowserPersistenceConfig
-from mcp_server_browser_use.browser.custom_context import CustomBrowserContext
+from .custom_context import CustomBrowserContext
 
 logger = logging.getLogger(__name__)
 
@@ -31,96 +25,57 @@ class CustomBrowser(Browser):
         config: BrowserContextConfig = BrowserContextConfig()
     ) -> CustomBrowserContext:
         return CustomBrowserContext(config=config, browser=self)
-
-    async def _setup_browser(self, playwright: Playwright) -> PlaywrightBrowser:
+    
+    async def _setup_browser_with_instance(self, playwright: Playwright) -> PlaywrightBrowser:
         """Sets up and returns a Playwright Browser instance with anti-detection measures."""
-        if self.config.wss_url:
-            browser = await playwright.chromium.connect(self.config.wss_url)
-            return browser
-        elif self.config.chrome_instance_path:
-            import subprocess
+        if not self.config.chrome_instance_path:
+            raise ValueError('Chrome instance path is required')
+        import subprocess
 
-            import requests
+        import requests
 
+        try:
+            # Check if browser is already running
+            response = requests.get('http://localhost:9222/json/version', timeout=2)
+            if response.status_code == 200:
+                logger.info('Reusing existing Chrome instance')
+                browser = await playwright.chromium.connect_over_cdp(
+                    endpoint_url='http://localhost:9222',
+                    timeout=20000,  # 20 second timeout for connection
+                )
+                return browser
+        except requests.ConnectionError:
+            logger.debug('No existing Chrome instance found, starting a new one')
+
+        # Start a new Chrome instance
+        subprocess.Popen(
+            [
+                self.config.chrome_instance_path,
+                '--remote-debugging-port=9222',
+            ] + self.config.extra_chromium_args,
+            stdout=subprocess.DEVNULL,
+            stderr=subprocess.DEVNULL,
+        )
+  
+        # try to connect first in case the browser have not started
+        for _ in range(10):
             try:
-                # Check if browser is already running
                 response = requests.get('http://localhost:9222/json/version', timeout=2)
                 if response.status_code == 200:
-                    logger.info('Reusing existing Chrome instance')
-                    browser = await playwright.chromium.connect_over_cdp(
-                        endpoint_url='http://localhost:9222',
-                        timeout=20000,  # 20 second timeout for connection
-                    )
-                    return browser
+                    break
             except requests.ConnectionError:
-                logger.debug('No existing Chrome instance found, starting a new one')
+                pass
+            await asyncio.sleep(1)
 
-            # Start a new Chrome instance
-            subprocess.Popen(
-                [
-                    self.config.chrome_instance_path,
-                    '--remote-debugging-port=9222',
-                ],
-                stdout=subprocess.DEVNULL,
-                stderr=subprocess.DEVNULL,
+        # Attempt to connect again after starting a new instance
+        try:
+            browser = await playwright.chromium.connect_over_cdp(
+                endpoint_url='http://localhost:9222',
+                timeout=20000,  # 20 second timeout for connection
             )
-
-            # Attempt to connect again after starting a new instance
-            for _ in range(10):
-                try:
-                    response = requests.get('http://localhost:9222/json/version', timeout=2)
-                    if response.status_code == 200:
-                        break
-                except requests.ConnectionError:
-                    pass
-                await asyncio.sleep(1)
-
-            try:
-                browser = await playwright.chromium.connect_over_cdp(
-                    endpoint_url='http://localhost:9222',
-                    timeout=20000,  # 20 second timeout for connection
-                )
-                return browser
-            except Exception as e:
-                logger.error(f'Failed to start a new Chrome instance.: {str(e)}')
-                raise RuntimeError(
-                    ' To start chrome in Debug mode, you need to close all existing Chrome instances and try again otherwise we can not connect to the instance.'
-                )
-
-        else:
-            try:
-                disable_security_args = []
-                if self.config.disable_security:
-                    disable_security_args = [
-                        '--disable-web-security',
-                        '--disable-site-isolation-trials',
-                        '--disable-features=IsolateOrigins,site-per-process',
-                    ]
-
-                browser = await playwright.chromium.launch(
-                    headless=self.config.headless,
-                    args=[
-                             '--no-sandbox',
-                             '--disable-blink-features=AutomationControlled',
-                             '--disable-infobars',
-                             '--disable-background-timer-throttling',
-                             '--disable-popup-blocking',
-                             '--disable-backgrounding-occluded-windows',
-                             '--disable-renderer-backgrounding',
-                             '--disable-window-activation',
-                             '--disable-focus-on-load',
-                             '--no-first-run',
-                             '--no-default-browser-check',
-                             '--no-startup-window',
-                             '--window-position=0,0',
-                             # '--window-size=1280,1000',
-                         ]
-                         + disable_security_args
-                         + self.config.extra_chromium_args,
-                    proxy=self.config.proxy,
-                )
-
-                return browser
-            except Exception as e:
-                logger.error(f'Failed to initialize Playwright browser: {str(e)}')
-                raise
+            return browser
+        except Exception as e:
+            logger.error(f'Failed to start a new Chrome instance.: {str(e)}')
+            raise RuntimeError(
+                ' To start chrome in Debug mode, you need to close all existing Chrome instances and try again otherwise we can not connect to the instance.'
+            )
\ No newline at end of file
diff --git a/src/mcp_server_browser_use/browser/custom_context.py b/src/mcp_server_browser_use/browser/custom_context.py
index 5f25f17..c293174 100644
--- a/src/mcp_server_browser_use/browser/custom_context.py
+++ b/src/mcp_server_browser_use/browser/custom_context.py
@@ -1,10 +1,3 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/1
-# @Author  : wenshao
-# @Email   : wenshaoguo1026@gmail.com
-# @Project : browser-use-webui
-# @FileName: context.py
-
 import json
 import logging
 import os
@@ -14,8 +7,6 @@ from browser_use.browser.context import BrowserContext, BrowserContextConfig
 from playwright.async_api import Browser as PlaywrightBrowser
 from playwright.async_api import BrowserContext as PlaywrightBrowserContext
 
-from mcp_server_browser_use.browser.config import BrowserPersistenceConfig
-
 logger = logging.getLogger(__name__)
 
 
@@ -25,73 +16,4 @@ class CustomBrowserContext(BrowserContext):
         browser: "Browser",
         config: BrowserContextConfig = BrowserContextConfig()
     ):
-        super(CustomBrowserContext, self).__init__(browser=browser, config=config)
-
-    async def _create_context(self, browser: PlaywrightBrowser) -> PlaywrightBrowserContext:
-        """Creates a new browser context with anti-detection measures and loads cookies if available."""
-        # If we have a context, return it directly
-
-        # Check if we should use existing context for persistence
-        if self.browser.config.chrome_instance_path and len(browser.contexts) > 0:
-            # Connect to existing Chrome instance instead of creating new one
-            context = browser.contexts[0]
-        else:
-            # Original code for creating new context
-            context = await browser.new_context(
-                viewport=self.config.browser_window_size,
-                no_viewport=False,
-                user_agent=(
-                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
-                    "(KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
-                ),
-                java_script_enabled=True,
-                bypass_csp=self.config.disable_security,
-                ignore_https_errors=self.config.disable_security,
-                record_video_dir=self.config.save_recording_path,
-                record_video_size=self.config.browser_window_size,
-            )
-
-        if self.config.trace_path:
-            await context.tracing.start(screenshots=True, snapshots=True, sources=True)
-
-        # Load cookies if they exist
-        if self.config.cookies_file and os.path.exists(self.config.cookies_file):
-            with open(self.config.cookies_file, "r") as f:
-                cookies = json.load(f)
-                logger.info(
-                    f"Loaded {len(cookies)} cookies from {self.config.cookies_file}"
-                )
-                await context.add_cookies(cookies)
-
-        # Expose anti-detection scripts
-        await context.add_init_script(
-            """
-            // Webdriver property
-            Object.defineProperty(navigator, 'webdriver', {
-                get: () => undefined
-            });
-
-            // Languages
-            Object.defineProperty(navigator, 'languages', {
-                get: () => ['en-US', 'en']
-            });
-
-            // Plugins
-            Object.defineProperty(navigator, 'plugins', {
-                get: () => [1, 2, 3, 4, 5]
-            });
-
-            // Chrome runtime
-            window.chrome = { runtime: {} };
-
-            // Permissions
-            const originalQuery = window.navigator.permissions.query;
-            window.navigator.permissions.query = (parameters) => (
-                parameters.name === 'notifications' ?
-                    Promise.resolve({ state: Notification.permission }) :
-                    originalQuery(parameters)
-            );
-            """
-        )
-
-        return context
+        super(CustomBrowserContext, self).__init__(browser=browser, config=config)
\ No newline at end of file
diff --git a/src/mcp_server_browser_use/controller/__init__.py b/src/mcp_server_browser_use/controller/__init__.py
index b2eb1b3..e69de29 100644
--- a/src/mcp_server_browser_use/controller/__init__.py
+++ b/src/mcp_server_browser_use/controller/__init__.py
@@ -1,5 +0,0 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/2
-# @Author  : wenshao
-# @ProjectName: browser-use-webui
-# @FileName: __init__.py.py
diff --git a/src/mcp_server_browser_use/controller/custom_controller.py b/src/mcp_server_browser_use/controller/custom_controller.py
index 6e57dd4..a042eb1 100644
--- a/src/mcp_server_browser_use/controller/custom_controller.py
+++ b/src/mcp_server_browser_use/controller/custom_controller.py
@@ -1,18 +1,34 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/2
-# @Author  : wenshao
-# @ProjectName: browser-use-webui
-# @FileName: custom_action.py
+import pdb
 
 import pyperclip
+from typing import Optional, Type
+from pydantic import BaseModel
 from browser_use.agent.views import ActionResult
 from browser_use.browser.context import BrowserContext
-from browser_use.controller.service import Controller
+from browser_use.controller.service import Controller, DoneAction
+from main_content_extractor import MainContentExtractor
+from browser_use.controller.views import (
+    ClickElementAction,
+    DoneAction,
+    ExtractPageContentAction,
+    GoToUrlAction,
+    InputTextAction,
+    OpenTabAction,
+    ScrollAction,
+    SearchGoogleAction,
+    SendKeysAction,
+    SwitchTabAction,
+)
+import logging
+
+logger = logging.getLogger(__name__)
 
 
 class CustomController(Controller):
-    def __init__(self):
-        super().__init__()
+    def __init__(self, exclude_actions: list[str] = [],
+                 output_model: Optional[Type[BaseModel]] = None
+                 ):
+        super().__init__(exclude_actions=exclude_actions, output_model=output_model)
         self._register_custom_actions()
 
     def _register_custom_actions(self):
@@ -31,3 +47,25 @@ class CustomController(Controller):
             await page.keyboard.type(text)
 
             return ActionResult(extracted_content=text)
+
+        @self.registry.action(
+            'Extract page content to get the pure text or markdown with links if include_links is set to true',
+            param_model=ExtractPageContentAction,
+            requires_browser=True,
+        )
+        async def extract_content(params: ExtractPageContentAction, browser: BrowserContext):
+            page = await browser.get_current_page()
+            # use jina reader
+            url = page.url
+            jina_url = f"https://r.jina.ai/{url}"
+            await page.goto(jina_url)
+            output_format = 'markdown' if params.include_links else 'text'
+            content = MainContentExtractor.extract(  # type: ignore
+                html=await page.content(),
+                output_format=output_format,
+            )
+            # go back to org url
+            await page.go_back()
+            msg = f'📄  Extracted page content as {output_format}\n: {content}\n'
+            logger.info(msg)
+            return ActionResult(extracted_content=msg)
diff --git a/src/mcp_server_browser_use/server.py b/src/mcp_server_browser_use/server.py
index f761d97..cc891c5 100644
--- a/src/mcp_server_browser_use/server.py
+++ b/src/mcp_server_browser_use/server.py
@@ -2,7 +2,7 @@ import asyncio
 import os
 import sys
 import traceback
-from typing import List
+from typing import List, Optional
 
 import logging
 
@@ -28,6 +28,32 @@ _global_agent_state = AgentState()
 app = FastMCP("mcp_server_browser_use")
 
 
+def get_env_bool(key: str, default: bool = False) -> bool:
+    """Get boolean value from environment variable."""
+    return os.getenv(key, str(default)).lower() in ("true", "1", "yes")
+
+
+def get_browser_config() -> BrowserConfig:
+    """Get browser configuration from environment variables."""
+    return BrowserConfig(
+        headless=get_env_bool("BROWSER_HEADLESS", False),
+        disable_security=get_env_bool("BROWSER_DISABLE_SECURITY", False),
+        chrome_instance_path=os.getenv("CHROME_PATH") or None,
+        extra_chromium_args=os.getenv("BROWSER_EXTRA_ARGS", "").split(),
+        wss_url=os.getenv("BROWSER_WSS_URL"),
+        proxy=os.getenv("BROWSER_PROXY"),
+    )
+
+
+def get_context_config() -> BrowserContextConfig:
+    """Get browser context configuration from environment variables."""
+    return BrowserContextConfig(
+        trace_path=os.getenv("BROWSER_TRACE_PATH"),
+        save_recording_path=os.getenv("BROWSER_RECORDING_PATH"),
+        no_viewport=get_env_bool("BROWSER_NO_VIEWPORT", False),
+    )
+
+
 async def _safe_cleanup():
     """Safely clean up browser resources"""
     global _global_browser, _global_agent_state, _global_browser_context, _global_agent
@@ -72,40 +98,25 @@ async def run_browser_agent(task: str, add_infos: str = "") -> str:
         _global_agent_state.clear_stop()
 
         # Get environment variables with defaults
-        model_provider = os.getenv("MCP_MODEL_PROVIDER", "openai")
-        model_name = os.getenv("MCP_MODEL_NAME", "gpt-4o")
+        model_provider = os.getenv("MCP_MODEL_PROVIDER", "anthropic")
+        model_name = os.getenv("MCP_MODEL_NAME", "claude-3-5-sonnet-20241022")
         temperature = float(os.getenv("MCP_TEMPERATURE", "0.7"))
         max_steps = int(os.getenv("MCP_MAX_STEPS", "100"))
-        use_vision = os.getenv("MCP_USE_VISION", "true").lower() == "true"
+        use_vision = get_env_bool("MCP_USE_VISION", True)
         max_actions_per_step = int(os.getenv("MCP_MAX_ACTIONS_PER_STEP", "5"))
-        tool_call_in_content = (
-            os.getenv("MCP_TOOL_CALL_IN_CONTENT", "true").lower() == "true"
-        )
+        tool_call_in_content = get_env_bool("MCP_TOOL_CALL_IN_CONTENT", True)
 
         # Prepare LLM
         llm = utils.get_llm_model(
             provider=model_provider, model_name=model_name, temperature=temperature
         )
 
-        chrome_path = os.getenv("CHROME_PATH", "") or None
-
-        # Create or reuse browser
+        # Create or reuse browser with improved configuration
         if not _global_browser:
-            _global_browser = CustomBrowser(
-                config=BrowserConfig(
-                    headless=False,
-                    disable_security=False,
-                    chrome_instance_path=chrome_path,
-                    extra_chromium_args=[],
-                    wss_url=None,
-                    proxy=None,
-                )
-            )
+            _global_browser = CustomBrowser(config=get_browser_config())
         if not _global_browser_context:
             _global_browser_context = await _global_browser.new_context(
-                config=BrowserContextConfig(
-                    trace_path=None, save_recording_path=None, no_viewport=False
-                )
+                config=get_context_config()
             )
 
         # Create controller and agent
@@ -123,16 +134,23 @@ async def run_browser_agent(task: str, add_infos: str = "") -> str:
             agent_state=_global_agent_state,
         )
 
-        # Run agent
-        history = await _global_agent.run(max_steps=max_steps)
-        final_result = (
-            history.final_result() or f"No final result. Possibly incomplete. {history}"
-        )
-
-        return final_result
+        # Run agent with improved error handling
+        try:
+            history = await _global_agent.run(max_steps=max_steps)
+            final_result = (
+                history.final_result()
+                or f"No final result. Possibly incomplete. {history}"
+            )
+            return final_result
+        except asyncio.CancelledError:
+            return "Task was cancelled"
+        except Exception as e:
+            logging.error(f"Agent run error: {str(e)}\n{traceback.format_exc()}")
+            return f"Error during task execution: {str(e)}"
 
     except Exception as e:
-        raise ValueError(f"run-browser-agent error: {str(e)}\n{traceback.format_exc()}")
+        logging.error(f"run-browser-agent error: {str(e)}\n{traceback.format_exc()}")
+        raise ValueError(f"run-browser-agent error: {str(e)}")
 
     finally:
         await _safe_cleanup()
diff --git a/src/mcp_server_browser_use/utils/__init__.py b/src/mcp_server_browser_use/utils/__init__.py
index 93fbe7f..e69de29 100644
--- a/src/mcp_server_browser_use/utils/__init__.py
+++ b/src/mcp_server_browser_use/utils/__init__.py
@@ -1,6 +0,0 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/1
-# @Author  : wenshao
-# @Email   : wenshaoguo1026@gmail.com
-# @Project : browser-use-webui
-# @FileName: __init__.py.py
diff --git a/src/mcp_server_browser_use/utils/deep_research.py b/src/mcp_server_browser_use/utils/deep_research.py
new file mode 100644
index 0000000..ddee059
--- /dev/null
+++ b/src/mcp_server_browser_use/utils/deep_research.py
@@ -0,0 +1,282 @@
+import pdb
+
+from dotenv import load_dotenv
+
+load_dotenv()
+import asyncio
+import os
+import sys
+import logging
+from pprint import pprint
+from uuid import uuid4
+from mcp_server_browser_use.utils import utils
+from mcp_server_browser_use.agent.custom_agent import CustomAgent
+import json
+from browser_use.agent.service import Agent
+from browser_use.browser.browser import BrowserConfig, Browser
+from langchain.schema import SystemMessage, HumanMessage
+from json_repair import repair_json
+from mcp_server_browser_use.agent.custom_prompts import (
+    CustomSystemPrompt,
+    CustomAgentMessagePrompt,
+)
+from mcp_server_browser_use.controller.custom_controller import CustomController
+
+logger = logging.getLogger(__name__)
+
+
+async def deep_research(task, llm, **kwargs):
+    task_id = str(uuid4())
+    save_dir = kwargs.get("save_dir", os.path.join(f"./tmp/deep_research/{task_id}"))
+    logger.info(f"Save Deep Research at: {save_dir}")
+    os.makedirs(save_dir, exist_ok=True)
+
+    # max qyery num per iteration
+    max_query_num = kwargs.get("max_query_num", 3)
+    search_system_prompt = f"""
+    You are a **Deep Researcher**, an AI agent specializing in in-depth information gathering and research using a web browser with **automated execution capabilities**. Your expertise lies in formulating comprehensive research plans and executing them meticulously to fulfill complex user requests. You will analyze user instructions, devise a detailed research plan, and determine the necessary search queries to gather the required information.
+
+    **Your Task:**
+
+    Given a user's research topic, you will:
+
+    1. **Develop a Research Plan:** Outline the key aspects and subtopics that need to be investigated to thoroughly address the user's request. This plan should be a high-level overview of the research direction.
+    2. **Generate Search Queries:** Based on your research plan, generate a list of specific search queries to be executed in a web browser. These queries should be designed to efficiently gather relevant information for each aspect of your plan.
+
+    **Output Format:**
+
+    Your output will be a JSON object with the following structure:
+
+    ```json
+    {{
+    "plan": "A concise, high-level research plan outlining the key areas to investigate.",
+      "queries": [
+        "search query 1",
+        "search query 2",
+        //... up to a maximum of {max_query_num} search queries
+      ]
+    }}
+    ```
+
+    **Important:**
+
+    *   Limit your output to a **maximum of {max_query_num}** search queries.
+    *   Make the search queries to help the automated agent find the needed information. Consider what keywords are most likely to lead to useful results.
+    *   If you have gathered for all the information you want and no further search queries are required, output queries with an empty list: `[]`
+    *   Make sure output search queries are different from the history queries.
+
+    **Inputs:**
+
+    1.  **User Instruction:** The original instruction given by the user.
+    2.  **Previous Queries:** History Queries.
+    3.  **Previous Search Results:** Textual data gathered from prior search queries. If there are no previous search results this string will be empty.
+    """
+    search_messages = [SystemMessage(content=search_system_prompt)]
+
+    record_system_prompt = """
+    You are an expert information recorder. Your role is to process user instructions, current search results, and previously recorded information to extract, summarize, and record new, useful information that helps fulfill the user's request. Your output will be a JSON formatted list, where each element represents a piece of extracted information and follows the structure: `{"url": "source_url", "title": "source_title", "summary_content": "concise_summary", "thinking": "reasoning"}`.
+
+**Important Considerations:**
+
+1. **Minimize Information Loss:** While concise, prioritize retaining important details and nuances from the sources. Aim for a summary that captures the essence of the information without over-simplification. **Crucially, ensure to preserve key data and figures within the `summary_content`. This is essential for later stages, such as generating tables and reports.**
+
+2. **Avoid Redundancy:** Do not record information that is already present in the Previous Recorded Information. Check for semantic similarity, not just exact matches. However, if the same information is expressed differently in a new source and this variation adds valuable context or clarity, it should be included.
+
+3. **Source Information:** Extract and include the source title and URL for each piece of information summarized. This is crucial for verification and context. **The Current Search Results are provided in a specific format, where each item starts with "Title:", followed by the title, then "URL Source:", followed by the URL, and finally "Markdown Content:", followed by the content. Please extract the title and URL from this structure.** If a piece of information cannot be attributed to a specific source from the provided search results, use `"url": "unknown"` and `"title": "unknown"`.
+
+4. **Thinking and Report Structure:**  For each extracted piece of information, add a `"thinking"` key. This field should contain your assessment of how this information could be used in a report, which section it might belong to (e.g., introduction, background, analysis, conclusion, specific subtopics), and any other relevant thoughts about its significance or connection to other information.
+
+**Output Format:**
+
+Provide your output as a JSON formatted list. Each item in the list must adhere to the following format:
+
+```json
+[
+  {
+    "url": "source_url_1",
+    "title": "source_title_1",
+    "summary_content": "Concise summary of content. Remember to include key data and figures here.",
+    "thinking": "This could be used in the introduction to set the context. It also relates to the section on the history of the topic."
+  },
+  // ... more entries
+  {
+    "url": "unknown",
+    "title": "unknown",
+    "summary_content": "concise_summary_of_content_without_clear_source",
+    "thinking": "This might be useful background information, but I need to verify its accuracy. Could be used in the methodology section to explain how data was collected."
+  }
+]
+```
+
+**Inputs:**
+
+1. **User Instruction:** The original instruction given by the user. This helps you determine what kind of information will be useful and how to structure your thinking.
+2. **Previous Recorded Information:** Textual data gathered and recorded from previous searches and processing, represented as a single text string.
+3. **Current Search Results:** Textual data gathered from the most recent search query.
+    """
+    record_messages = [SystemMessage(content=record_system_prompt)]
+
+    browser = Browser(
+        config=BrowserConfig(
+            disable_security=True,
+            headless=kwargs.get(
+                "headless", False
+            ),  # Set to False to see browser actions
+        )
+    )
+    controller = CustomController()
+
+    search_iteration = 0
+    max_search_iterations = kwargs.get(
+        "max_search_iterations", 10
+    )  # Limit search iterations to prevent infinite loop
+    use_vision = kwargs.get("use_vision", False)
+
+    history_query = []
+    history_infos = []
+    try:
+        while search_iteration < max_search_iterations:
+            search_iteration += 1
+            logger.info(f"Start {search_iteration}th Search...")
+            history_query_ = json.dumps(history_query, indent=4)
+            history_infos_ = json.dumps(history_infos, indent=4)
+            query_prompt = f"This is search {search_iteration} of {max_search_iterations} maximum searches allowed.\n User Instruction:{task} \n Previous Queries:\n {history_query_} \n Previous Search Results:\n {history_infos_}\n"
+            search_messages.append(HumanMessage(content=query_prompt))
+            ai_query_msg = llm.invoke(search_messages[:1] + search_messages[1:][-1:])
+            search_messages.append(ai_query_msg)
+            if hasattr(ai_query_msg, "reasoning_content"):
+                logger.info("🤯 Start Search Deep Thinking: ")
+                logger.info(ai_query_msg.reasoning_content)
+                logger.info("🤯 End Search Deep Thinking")
+            ai_query_content = ai_query_msg.content.replace("```json", "").replace(
+                "```", ""
+            )
+            ai_query_content = repair_json(ai_query_content)
+            ai_query_content = json.loads(ai_query_content)
+            query_plan = ai_query_content["plan"]
+            logger.info(f"Current Iteration {search_iteration} Planing:")
+            logger.info(query_plan)
+            query_tasks = ai_query_content["queries"]
+            if not query_tasks:
+                break
+            else:
+                history_query.extend(query_tasks)
+                logger.info("Query tasks:")
+                logger.info(query_tasks)
+
+            # 2. Perform Web Search and Auto exec
+            # Paralle BU agents
+            add_infos = (
+                "1. Please click on the most relevant link to get information and go deeper, instead of just staying on the search page. \n"
+                "2. When opening a PDF file, please remember to extract the content using extract_content instead of simply opening it for the user to view."
+            )
+            agents = [
+                CustomAgent(
+                    task=task,
+                    llm=llm,
+                    add_infos=add_infos,
+                    browser=browser,
+                    use_vision=use_vision,
+                    system_prompt_class=CustomSystemPrompt,
+                    agent_prompt_class=CustomAgentMessagePrompt,
+                    max_actions_per_step=5,
+                    controller=controller,
+                )
+                for task in query_tasks
+            ]
+            query_results = await asyncio.gather(
+                *[agent.run(max_steps=kwargs.get("max_steps", 10)) for agent in agents]
+            )
+
+            # 3. Summarize Search Result
+            query_result_dir = os.path.join(save_dir, "query_results")
+            os.makedirs(query_result_dir, exist_ok=True)
+            for i in range(len(query_tasks)):
+                query_result = query_results[i].final_result()
+                querr_save_path = os.path.join(
+                    query_result_dir, f"{search_iteration}-{i}.md"
+                )
+                logger.info(f"save query: {query_tasks[i]} at {querr_save_path}")
+                with open(querr_save_path, "w", encoding="utf-8") as fw:
+                    fw.write(f"Query: {query_tasks[i]}\n")
+                    fw.write(query_result)
+                history_infos_ = json.dumps(history_infos, indent=4)
+                record_prompt = f"User Instruction:{task}. \nPrevious Recorded Information:\n {json.dumps(history_infos_)} \n Current Search Results: {query_result}\n "
+                record_messages.append(HumanMessage(content=record_prompt))
+                ai_record_msg = llm.invoke(record_messages[:1] + record_messages[-1:])
+                record_messages.append(ai_record_msg)
+                if hasattr(ai_record_msg, "reasoning_content"):
+                    logger.info("🤯 Start Record Deep Thinking: ")
+                    logger.info(ai_record_msg.reasoning_content)
+                    logger.info("🤯 End Record Deep Thinking")
+                record_content = ai_record_msg.content
+                record_content = repair_json(record_content)
+                new_record_infos = json.loads(record_content)
+                history_infos.extend(new_record_infos)
+
+        logger.info("\nFinish Searching, Start Generating Report...")
+
+        # 5. Report Generation in Markdown (or JSON if you prefer)
+        writer_system_prompt = """
+        You are a **Deep Researcher** and a professional report writer tasked with creating polished, high-quality reports that fully meet the user's needs, based on the user's instructions and the relevant information provided. You will write the report using Markdown format, ensuring it is both informative and visually appealing.
+
+**Specific Instructions:**
+
+*   **Structure for Impact:** The report must have a clear, logical, and impactful structure. Begin with a compelling introduction that immediately grabs the reader's attention. Develop well-structured body paragraphs that flow smoothly and logically, and conclude with a concise and memorable conclusion that summarizes key takeaways and leaves a lasting impression.
+*   **Engaging and Vivid Language:** Employ precise, vivid, and descriptive language to make the report captivating and enjoyable to read. Use stylistic techniques to enhance engagement. Tailor your tone, vocabulary, and writing style to perfectly suit the subject matter and the intended audience to maximize impact and readability.
+*   **Accuracy, Credibility, and Citations:** Ensure that all information presented is meticulously accurate, rigorously truthful, and robustly supported by the available data. **Cite sources exclusively using bracketed sequential numbers within the text (e.g., [1], [2], etc.). If no references are used, omit citations entirely.** These numbers must correspond to a numbered list of references at the end of the report.
+*   **Publication-Ready Formatting:** Adhere strictly to Markdown formatting for excellent readability and a clean, highly professional visual appearance. Pay close attention to formatting details like headings, lists, emphasis, and spacing to optimize the visual presentation and reader experience. The report should be ready for immediate publication upon completion, requiring minimal to no further editing for style or format.
+*   **Conciseness and Clarity (Unless Specified Otherwise):** When the user does not provide a specific length, prioritize concise and to-the-point writing, maximizing information density while maintaining clarity.
+*   **Data-Driven Comparisons with Tables:**  **When appropriate and beneficial for enhancing clarity and impact, present data comparisons in well-structured Markdown tables. This is especially encouraged when dealing with numerical data or when a visual comparison can significantly improve the reader's understanding.**
+*   **Length Adherence:** When the user specifies a length constraint, meticulously stay within reasonable bounds of that specification, ensuring the content is appropriately scaled without sacrificing quality or completeness.
+*   **Comprehensive Instruction Following:** Pay meticulous attention to all details and nuances provided in the user instructions. Strive to fulfill every aspect of the user's request with the highest degree of accuracy and attention to detail, creating a report that not only meets but exceeds expectations for quality and professionalism.
+*   **Reference List Formatting:** The reference list at the end must be formatted as follows:
+    `[1] Title (URL, if available)`
+    **Each reference must be separated by a blank line to ensure proper spacing.** For example:
+
+    ```
+    [1] Title 1 (URL1, if available)
+
+    [2] Title 2 (URL2, if available)
+    ```
+    **Furthermore, ensure that the reference list is free of duplicates. Each unique source should be listed only once, regardless of how many times it is cited in the text.**
+*   **ABSOLUTE FINAL OUTPUT RESTRICTION:**  **Your output must contain ONLY the finished, publication-ready Markdown report. Do not include ANY extraneous text, phrases, preambles, meta-commentary, or markdown code indicators (e.g., "```markdown```"). The report should begin directly with the title and introductory paragraph, and end directly after the conclusion and the reference list (if applicable).**  **Your response will be deemed a failure if this instruction is not followed precisely.**
+
+**Inputs:**
+
+1. **User Instruction:** The original instruction given by the user. This helps you determine what kind of information will be useful and how to structure your thinking.
+2. **Search Information:** Information gathered from the search queries.
+        """
+
+        history_infos_ = json.dumps(history_infos, indent=4)
+        record_json_path = os.path.join(save_dir, "record_infos.json")
+        logger.info(f"save All recorded information at {record_json_path}")
+        with open(record_json_path, "w") as fw:
+            json.dump(history_infos, fw, indent=4)
+        report_prompt = (
+            f"User Instruction:{task} \n Search Information:\n {history_infos_}"
+        )
+        report_messages = [
+            SystemMessage(content=writer_system_prompt),
+            HumanMessage(content=report_prompt),
+        ]  # New context for report generation
+        ai_report_msg = llm.invoke(report_messages)
+        if hasattr(ai_report_msg, "reasoning_content"):
+            logger.info("🤯 Start Report Deep Thinking: ")
+            logger.info(ai_report_msg.reasoning_content)
+            logger.info("🤯 End Report Deep Thinking")
+        report_content = ai_report_msg.content
+
+        report_file_path = os.path.join(save_dir, "final_report.md")
+        with open(report_file_path, "w", encoding="utf-8") as f:
+            f.write(report_content)
+        logger.info(f"Save Report at: {report_file_path}")
+        return report_content, report_file_path
+
+    except Exception as e:
+        logger.error(f"Deep research Error: {e}")
+        return "", None
+    finally:
+        if browser:
+            await browser.close()
+            logger.info("Browser closed.")
diff --git a/src/mcp_server_browser_use/utils/llm.py b/src/mcp_server_browser_use/utils/llm.py
new file mode 100644
index 0000000..646bd0c
--- /dev/null
+++ b/src/mcp_server_browser_use/utils/llm.py
@@ -0,0 +1,134 @@
+from openai import OpenAI
+import pdb
+from langchain_openai import ChatOpenAI
+from langchain_core.globals import get_llm_cache
+from langchain_core.language_models.base import (
+    BaseLanguageModel,
+    LangSmithParams,
+    LanguageModelInput,
+)
+from langchain_core.load import dumpd, dumps
+from langchain_core.messages import (
+    AIMessage,
+    SystemMessage,
+    AnyMessage,
+    BaseMessage,
+    BaseMessageChunk,
+    HumanMessage,
+    convert_to_messages,
+    message_chunk_to_message,
+)
+from langchain_core.outputs import (
+    ChatGeneration,
+    ChatGenerationChunk,
+    ChatResult,
+    LLMResult,
+    RunInfo,
+)
+from langchain_ollama import ChatOllama
+from langchain_core.output_parsers.base import OutputParserLike
+from langchain_core.runnables import Runnable, RunnableConfig
+from langchain_core.tools import BaseTool
+
+from typing import (
+    TYPE_CHECKING,
+    Any,
+    Callable,
+    Literal,
+    Optional,
+    Union,
+    cast,
+)
+
+class DeepSeekR1ChatOpenAI(ChatOpenAI):
+
+    def __init__(self, *args: Any, **kwargs: Any) -> None:
+        super().__init__(*args, **kwargs)
+        self.client = OpenAI(
+            base_url=kwargs.get("base_url"), api_key=kwargs.get("api_key")
+        )
+
+    async def ainvoke(
+        self,
+        input: LanguageModelInput,
+        config: Optional[RunnableConfig] = None,
+        *,
+        stop: Optional[list[str]] = None,
+        **kwargs: Any,
+    ) -> AIMessage:
+        message_history = []
+        for input_ in input:
+            if isinstance(input_, SystemMessage):
+                message_history.append({"role": "system", "content": input_.content})
+            elif isinstance(input_, AIMessage):
+                message_history.append({"role": "assistant", "content": input_.content})
+            else:
+                message_history.append({"role": "user", "content": input_.content})
+
+        response = self.client.chat.completions.create(
+            model=self.model_name, messages=message_history
+        )
+
+        reasoning_content = response.choices[0].message.reasoning_content
+        content = response.choices[0].message.content
+        return AIMessage(content=content, reasoning_content=reasoning_content)
+
+    def invoke(
+        self,
+        input: LanguageModelInput,
+        config: Optional[RunnableConfig] = None,
+        *,
+        stop: Optional[list[str]] = None,
+        **kwargs: Any,
+    ) -> AIMessage:
+        message_history = []
+        for input_ in input:
+            if isinstance(input_, SystemMessage):
+                message_history.append({"role": "system", "content": input_.content})
+            elif isinstance(input_, AIMessage):
+                message_history.append({"role": "assistant", "content": input_.content})
+            else:
+                message_history.append({"role": "user", "content": input_.content})
+
+        response = self.client.chat.completions.create(
+            model=self.model_name,
+            messages=message_history
+        )
+
+        reasoning_content = response.choices[0].message.reasoning_content
+        content = response.choices[0].message.content
+        return AIMessage(content=content, reasoning_content=reasoning_content)
+
+class DeepSeekR1ChatOllama(ChatOllama):
+
+    async def ainvoke(
+        self,
+        input: LanguageModelInput,
+        config: Optional[RunnableConfig] = None,
+        *,
+        stop: Optional[list[str]] = None,
+        **kwargs: Any,
+    ) -> AIMessage:
+        org_ai_message = await super().ainvoke(input=input)
+        org_content = org_ai_message.content
+        reasoning_content = org_content.split("</think>")[0].replace("<think>", "")
+        content = org_content.split("</think>")[1]
+        if "**JSON Response:**" in content:
+            content = content.split("**JSON Response:**")[-1]
+        return AIMessage(content=content, reasoning_content=reasoning_content)
+
+    def invoke(
+        self,
+        input: LanguageModelInput,
+        config: Optional[RunnableConfig] = None,
+        *,
+        stop: Optional[list[str]] = None,
+        **kwargs: Any,
+    ) -> AIMessage:
+        org_ai_message = super().invoke(input=input)
+        org_content = org_ai_message.content
+        reasoning_content = org_content.split("</think>")[0].replace("<think>", "")
+        content = org_content.split("</think>")[1]
+        if "**JSON Response:**" in content:
+            content = content.split("**JSON Response:**")[-1]
+        return AIMessage(content=content, reasoning_content=reasoning_content)
diff --git a/src/mcp_server_browser_use/utils/utils.py b/src/mcp_server_browser_use/utils/utils.py
index 8ea6ce0..15772c8 100644
--- a/src/mcp_server_browser_use/utils/utils.py
+++ b/src/mcp_server_browser_use/utils/utils.py
@@ -1,20 +1,17 @@
-# -*- coding: utf-8 -*-
-# @Time    : 2025/1/1
-# @Author  : wenshao
-# @Email   : wenshaoguo1026@gmail.com
-# @Project : browser-use-webui
-# @FileName: utils.py
 import base64
 import os
 import time
 from pathlib import Path
 from typing import Dict, Optional
+import requests
 
 from langchain_anthropic import ChatAnthropic
+from langchain_mistralai import ChatMistralAI
 from langchain_google_genai import ChatGoogleGenerativeAI
 from langchain_ollama import ChatOllama
 from langchain_openai import AzureChatOpenAI, ChatOpenAI
 
+from .llm import DeepSeekR1ChatOpenAI, DeepSeekR1ChatOllama
 
 def get_llm_model(provider: str, **kwargs):
     """
@@ -23,34 +20,49 @@ def get_llm_model(provider: str, **kwargs):
     :param kwargs:
     :return:
     """
+    if provider not in ["ollama"]:
+        env_var = (
+            "GOOGLE_API_KEY" if provider == "gemini" else f"{provider.upper()}_API_KEY"
+        )
+        api_key = kwargs.get("api_key", "") or os.getenv(env_var, "")
+        if not api_key:
+            raise ValueError(f"API key for {provider} is not set")
+        kwargs["api_key"] = api_key
+
     if provider == "anthropic":
         if not kwargs.get("base_url", ""):
             base_url = "https://api.anthropic.com"
         else:
             base_url = kwargs.get("base_url")
 
-        if not kwargs.get("api_key", ""):
-            api_key = os.getenv("ANTHROPIC_API_KEY", "")
-        else:
-            api_key = kwargs.get("api_key")
-
         return ChatAnthropic(
             model_name=kwargs.get("model_name", "claude-3-5-sonnet-20240620"),
             temperature=kwargs.get("temperature", 0.0),
             base_url=base_url,
             api_key=api_key,
         )
+    elif provider == "mistral":
+        if not kwargs.get("base_url", ""):
+            base_url = os.getenv("MISTRAL_ENDPOINT", "https://api.mistral.ai/v1")
+        else:
+            base_url = kwargs.get("base_url")
+        if not kwargs.get("api_key", ""):
+            api_key = os.getenv("MISTRAL_API_KEY", "")
+        else:
+            api_key = kwargs.get("api_key")
+
+        return ChatMistralAI(
+            model=kwargs.get("model_name", "mistral-large-latest"),
+            temperature=kwargs.get("temperature", 0.0),
+            base_url=base_url,
+            api_key=api_key,
+        )
     elif provider == "openai":
         if not kwargs.get("base_url", ""):
             base_url = os.getenv("OPENAI_ENDPOINT", "https://api.openai.com/v1")
         else:
             base_url = kwargs.get("base_url")
 
-        if not kwargs.get("api_key", ""):
-            api_key = os.getenv("OPENAI_API_KEY", "")
-        else:
-            api_key = kwargs.get("api_key")
-
         return ChatOpenAI(
             model=kwargs.get("model_name", "gpt-4o"),
             temperature=kwargs.get("temperature", 0.0),
@@ -63,43 +75,52 @@ def get_llm_model(provider: str, **kwargs):
         else:
             base_url = kwargs.get("base_url")
 
-        if not kwargs.get("api_key", ""):
-            api_key = os.getenv("DEEPSEEK_API_KEY", "")
+        if kwargs.get("model_name", "deepseek-chat") == "deepseek-reasoner":
+            return DeepSeekR1ChatOpenAI(
+                model=kwargs.get("model_name", "deepseek-reasoner"),
+                temperature=kwargs.get("temperature", 0.0),
+                base_url=base_url,
+                api_key=api_key,
+            )
         else:
-            api_key = kwargs.get("api_key")
-
-        return ChatOpenAI(
-            model=kwargs.get("model_name", "deepseek-chat"),
-            temperature=kwargs.get("temperature", 0.0),
-            base_url=base_url,
-            api_key=api_key,
-        )
+            return ChatOpenAI(
+                model=kwargs.get("model_name", "deepseek-chat"),
+                temperature=kwargs.get("temperature", 0.0),
+                base_url=base_url,
+                api_key=api_key,
+            )
     elif provider == "gemini":
-        if not kwargs.get("api_key", ""):
-            api_key = os.getenv("GOOGLE_API_KEY", "")
-        else:
-            api_key = kwargs.get("api_key")
         return ChatGoogleGenerativeAI(
             model=kwargs.get("model_name", "gemini-2.0-flash-exp"),
             temperature=kwargs.get("temperature", 0.0),
             google_api_key=api_key,
         )
     elif provider == "ollama":
-        return ChatOllama(
-            model=kwargs.get("model_name", "qwen2.5:7b"),
-            temperature=kwargs.get("temperature", 0.0),
-            num_ctx=128000,
-            base_url=kwargs.get("base_url", "http://localhost:11434"),
-        )
+        if not kwargs.get("base_url", ""):
+            base_url = os.getenv("OLLAMA_ENDPOINT", "http://localhost:11434")
+        else:
+            base_url = kwargs.get("base_url")
+
+        if "deepseek-r1" in kwargs.get("model_name", "qwen2.5:7b"):
+            return DeepSeekR1ChatOllama(
+                model=kwargs.get("model_name", "deepseek-r1:14b"),
+                temperature=kwargs.get("temperature", 0.0),
+                num_ctx=kwargs.get("num_ctx", 32000),
+                base_url=base_url,
+            )
+        else:
+            return ChatOllama(
+                model=kwargs.get("model_name", "qwen2.5:7b"),
+                temperature=kwargs.get("temperature", 0.0),
+                num_ctx=kwargs.get("num_ctx", 32000),
+                num_predict=kwargs.get("num_predict", 1024),
+                base_url=base_url,
+            )
     elif provider == "azure_openai":
         if not kwargs.get("base_url", ""):
             base_url = os.getenv("AZURE_OPENAI_ENDPOINT", "")
         else:
             base_url = kwargs.get("base_url")
-        if not kwargs.get("api_key", ""):
-            api_key = os.getenv("AZURE_OPENAI_API_KEY", "")
-        else:
-            api_key = kwargs.get("api_key")
         return AzureChatOpenAI(
             model=kwargs.get("model_name", "gpt-4o"),
             temperature=kwargs.get("temperature", 0.0),
@@ -107,27 +128,31 @@ def get_llm_model(provider: str, **kwargs):
             azure_endpoint=base_url,
             api_key=api_key,
         )
+    elif provider == "openrouter":
+        if not kwargs.get("base_url", ""):
+            base_url = os.getenv("OPENROUTER_ENDPOINT", "")
+        else:
+            base_url = kwargs.get("base_url")
+
+        model_name = kwargs.get("model_name", "openai/o3-mini")
+        if "r1" in model_name or "aion" in model_name:
+            return DeepSeekR1ChatOpenAI(
+                model=model_name,
+                temperature=kwargs.get("temperature", 0.0),
+                base_url=base_url,
+                api_key=api_key,
+            )
+        else:
+            return ChatOpenAI(
+                model=model_name,
+                temperature=kwargs.get("temperature", 0.0),
+                base_url=base_url,
+                api_key=api_key,
+            )
     else:
         raise ValueError(f"Unsupported provider: {provider}")
 
 
-# Predefined model names for common providers
-model_names = {
-    "anthropic": ["claude-3-5-sonnet-20240620", "claude-3-opus-20240229"],
-    "openai": ["gpt-4o", "gpt-4", "gpt-3.5-turbo"],
-    "deepseek": ["deepseek-chat"],
-    "gemini": [
-        "gemini-2.0-flash-exp",
-        "gemini-2.0-flash-thinking-exp",
-        "gemini-1.5-flash-latest",
-        "gemini-1.5-flash-8b-latest",
-        "gemini-2.0-flash-thinking-exp-1219",
-    ],
-    "ollama": ["qwen2.5:7b", "llama2:7b"],
-    "azure_openai": ["gpt-4o", "gpt-4", "gpt-3.5-turbo"],
-}
-
-
 def encode_image(img_path):
     if not img_path:
         return None
diff --git a/uv.lock b/uv.lock
index eb80b89..13bc52e 100644
--- a/uv.lock
+++ b/uv.lock
@@ -18,7 +18,7 @@ wheels = [
 
 [[package]]
 name = "aiohttp"
-version = "3.11.11"
+version = "3.11.12"
 source = { registry = "https://pypi.org/simple" }
 dependencies = [
     { name = "aiohappyeyeballs" },
@@ -29,53 +29,56 @@ dependencies = [
     { name = "propcache" },
     { name = "yarl" },
 ]



why does it give error " AgentMessagePrompt.__init__() got multiple values for argument 'include_attributes'"

---

_**Assistant**_

<think>
Okay, let's try to figure out why the error "AgentMessagePrompt.__init__() got multiple values for argument 'include_attributes'" is happening. 

First, I'll look at the code where the CustomMassageManager is initialized. The user mentioned that the error occurs here. The __init__ method of CustomMassageManager probably inherits from a parent class, maybe MessageManager. I need to check if the parent class's __init__ method has parameters that are being passed multiple times.

Looking at the CustomMassageManager's __init__ method, the parameters include 'llm', 'task', 'action_descriptions', 'system_prompt_class', 'agent_prompt_class', 'max_input_tokens', 'include_attributes', 'max_error_length', 'max_actions_per_step'. When initializing the parent class (MessageManager), does it expect any of these parameters? If the parent class's __init__ has a parameter named 'include_attributes', and the child class is passing it again when calling super().__init__, that would cause a conflict.

Wait, in the code provided, the CustomMassageManager's __init__ calls super().__init__ with some arguments. Let me check that. The super().__init__ might be passing include_attributes as a keyword argument, but if the parent class's __init__ doesn't expect that parameter, or if it's already being passed in another way, that could cause the error.

Looking at the code snippet for CustomMassageManager's __init__:

def __init__(self, ..., include_attributes, ...):
    super().__init__(
        llm=llm,
        action_descriptions=action_descriptions,
        system_prompt_class=system_prompt_class,
        max_input_tokens=max_input_tokens,
        include_attributes=include_attributes,
        max_error_length=max_error_length,
        max_actions_per_step=max_actions_per_step,
    )

If the parent class (MessageManager) doesn't have an 'include_attributes' parameter in its __init__ method, then passing include_attributes=include_attributes here would be invalid. Alternatively, if the parent class does have include_attributes, but the child class is also receiving it as a parameter and passing it to super, but there's a mismatch in how it's handled.

Wait, maybe the parent class's __init__ doesn't have include_attributes as a parameter, but the child class is passing it, leading to a TypeError. Or perhaps the parent class's __init__ was updated, and the child class is now passing an extra parameter that's not expected.

Another possibility is that the AgentMessagePrompt class (which is part of the system_prompt_class or agent_prompt_class) has an __init__ method that includes 'include_attributes' as a parameter, and when creating an instance, it's being passed multiple times. For example, if the AgentMessagePrompt's __init__ is defined with include_attributes as a positional argument, but the code is passing it both positionally and as a keyword argument.

Looking at the code where AgentMessagePrompt is used, perhaps in the message_manager, when creating the prompt, the include_attributes is being passed twice. For instance, if the parent class's method already includes include_attributes, and the child class adds it again.

Alternatively, in the CustomMassageManager's add_state_message method, when creating the AgentMessagePrompt, maybe the parameters are being passed incorrectly. For example, if the code does something like AgentMessagePrompt(state, ..., include_attributes=self.include_attributes), but the __init__ of AgentMessagePrompt already has include_attributes as a positional argument, leading to a duplicate.

Wait, the error message says the __init__ of AgentMessagePrompt received multiple values for 'include_attributes'. That suggests that in the AgentMessagePrompt's __init__ method, 'include_attributes' is defined as a positional parameter, but the code is passing it both positionally and as a keyword argument.

Looking at the code where AgentMessagePrompt is initialized, perhaps in the add_state_message method, the code is passing include_attributes as a keyword argument, but it's already being set by another parameter. For example:

class AgentMessagePrompt:
    def __init__(self, state, result, include_attributes, ...):
        ...

Then, when creating an instance, if the code does:

AgentMessagePrompt(state, result, include_attributes=True, ...)

But if 'include_attributes' is already the third positional parameter, and the code also passes it as a keyword argument, that would cause the error.

Alternatively, the parent class of AgentMessagePrompt might have an 'include_attributes' parameter, and the child class is overriding __init__ and accidentally passing it twice.

Another angle: the CustomMassageManager's parent class (MessageManager) might have an 'include_attributes' parameter in its __init__, and when the child class calls super().__init__, it's passing include_attributes as a keyword argument, but the parent class's __init__ is expecting it as a positional argument, or vice versa, leading to a conflict.

Wait, looking at the code for the CustomMassageManager's __init__:

super().__init__(
    llm=llm,
    action_descriptions=action_descriptions,
    system_prompt_class=system_prompt_class,
    max_input_tokens=max_input_tokens,
    include_attributes=include_attributes,
    max_error_length=max_error_length,
    max_actions_per_step=max_actions_per_step,
)

If the parent class's __init__ doesn't have 'include_attributes' as a parameter, then this would cause an error. But the error message is about AgentMessagePrompt's __init__, not the MessageManager's. So perhaps the issue is elsewhere.

Wait, the error occurs when initializing the CustomMassageManager, which in turn initializes the MessageManager (parent), which might be creating an instance of AgentMessagePrompt. If the MessageManager's __init__ passes 'include_attributes' to the AgentMessagePrompt's __init__, but the way it's passed causes a duplication.

Alternatively, the AgentMessagePrompt's __init__ is being called with 'include_attributes' both as a positional and keyword argument. For example, if the __init__ is defined as:

def __init__(self, include_attributes, ...):

But when creating an instance, the code does:

AgentMessagePrompt(include_attributes=True, ..., include_attributes=False)

That would obviously cause an error. But more likely, the code is passing 'include_attributes' in both the positional arguments and keyword arguments.

Looking at the code in the CustomMassageManager's add_state_message method, where it creates the AgentMessagePrompt:

self.add_message(
    AgentMessagePrompt(
        state=state,
        prev_actions=prev_actions,
        result=result,
        step_info=step_info,
        include_attributes=self.include_attributes,
    )
)

If the AgentMessagePrompt's __init__ method has 'include_attributes' as a positional parameter, but the code is passing it as a keyword argument, while also having another positional argument that maps to 'include_attributes', that would cause the error.

For example, if the __init__ is defined as:

class AgentMessagePrompt:
    def __init__(self, include_attributes, state, prev_actions, result, step_info):
        ...

But the code is passing state, prev_actions, etc., as keyword arguments, and include_attributes as a keyword argument, but the first positional parameter is 'include_attributes', then the code would be passing 'include_attributes' twice: once positionally (since the first argument is state, which would be assigned to include_attributes) and once as a keyword.

That would definitely cause the "multiple values" error.

So the root cause is that the AgentMessagePrompt's __init__ method has 'include_attributes' as a parameter, but when creating an instance, the code is passing it both positionally (by mistake) and as a keyword argument.

Looking at how the AgentMessagePrompt is initialized in the code:

AgentMessagePrompt(
    state=state,
    prev_actions=prev_actions,
    result=result,
    step_info=step_info,
    include_attributes=self.include_attributes,
)

If the __init__ method's parameters are ordered as (self, state, prev_actions, result, step_info, include_attributes), then passing them as keyword arguments is fine. But if the __init__ method's first parameter after self is 'include_attributes', then passing state=state would be a keyword argument, but the first positional parameter is 'include_attributes', leading to a conflict.

Wait, no. In Python, when you instantiate a class, you can't pass positional arguments after keyword arguments. But if the __init__ is defined as:

def __init__(self, include_attributes, state, prev_actions, ...):

And the code does:

AgentMessagePrompt(state=state, prev_actions=..., include_attributes=...)

Then 'state' is being passed as a keyword argument, but the first parameter is 'include_attributes', which hasn't been provided positionally. That would result in a missing required positional argument error. 

But the error the user is getting is about multiple values for 'include_attributes', which suggests that 'include_attributes' is being assigned both positionally and via keyword.

So perhaps in the AgentMessagePrompt's __init__, 'include_attributes' is a positional parameter, but the code is also passing it as a keyword argument. For example, if the __init__ is defined as:

class AgentMessagePrompt:
    def __init__(self, include_attributes, state, ...):
        ...

And the code creates an instance like:

AgentMessagePrompt(state=state, include_attributes=True)

Then, since 'include_attributes' is the first positional parameter, but the code is passing 'state' as a keyword argument, the first positional argument is missing. That would cause an error, but not the multiple values error.

Alternatively, if the code has a parent class where 'include_attributes' is already a parameter, and the child class is adding it again.

Alternatively, the issue is in the parent class's __init__ method. For example, the MessageManager's __init__ might have a parameter 'include_attributes', and when the CustomMassageManager is initialized, it's passing include_attributes to the parent's __init__, but the parent's __init__ is also receiving it from another source.

Wait, looking back at the code for the CustomMassageManager's __init__:

def __init__(
    self,
    llm,
    task,
    action_descriptions,
    system_prompt_class,
    agent_prompt_class,
    max_input_tokens,
    include_attributes,
    max_error_length,
    max_actions_per_step,
):
    super().__init__(
        llm=llm,
        action_descriptions=action_descriptions,
        system_prompt_class=system_prompt_class,
        max_input_tokens=max_input_tokens,
        include_attributes=include_attributes,
        max_error_length=max_error_length,
        max_actions_per_step=max_actions_per_step,
    )
    self.agent_prompt_class = agent_prompt_class
    ...

If the parent class (MessageManager) does not have 'include_attributes' as a parameter in its __init__, then passing include_attributes=include_attributes would cause a TypeError. But the error the user is encountering is about AgentMessagePrompt, not the MessageManager.

Hmm. Maybe the parent class (MessageManager) does have 'include_attributes' in its __init__, and when the CustomMassageManager is initialized, it's passing that parameter to the parent, but when the MessageManager creates an AgentMessagePrompt instance, it's passing include_attributes both via the parent's __init__ and somewhere else.

Alternatively, the AgentMessagePrompt is part of the system_prompt_class or agent_prompt_class, and when initializing those classes, the code is passing include_attributes multiple times.

Wait, in the code, the CustomMassageManager's __init__ sets self.agent_prompt_class = agent_prompt_class. Then, when adding a message, it uses self.agent_prompt_class to create an instance. If the agent_prompt_class's __init__ method has 'include_attributes' as a parameter, and when creating the instance, the code is passing it both via the parent's __init__ and explicitly, that could cause the error.

Looking at the code where AgentMessagePrompt is created in the CustomMassageManager's add_state_message method:

self.add_message(
    AgentMessagePrompt(
        state=state,
        prev_actions=prev_actions,
        result=result,
        step_info=step_info,
        include_attributes=self.include_attributes,
    )
)

If the AgentMessagePrompt's __init__ method is defined as:

class AgentMessagePrompt:
    def __init__(self, state, prev_actions, result, step_info, include_attributes):
        ...

Then this would be correct. But if the __init__ method has 'include_attributes' as a positional argument before others, or if it's also being passed via *args or **kwargs, that could cause a conflict.

Alternatively, the parent class of AgentMessagePrompt (if any) has an 'include_attributes' parameter, and the child class is inadvertently passing it twice.

Another possibility is that the AgentMessagePrompt is a subclass of a class that already has 'include_attributes' as an attribute, and the __init__ method is overriding it incorrectly.

Alternatively, the code was refactored, and 'include_attributes' was added both as a positional and keyword argument in the __init__ call.

Given the error message, the most likely scenario is that when initializing the AgentMessagePrompt, the code is passing 'include_attributes' both as a positional argument and as a keyword argument, leading to the conflict.

For example, if the __init__ is defined as:

class AgentMessagePrompt:
    def __init__(self, include_attributes, state, prev_actions, result, step_info):
        ...

But the code is calling it as:

AgentMessagePrompt(
    state=state,
    prev_actions=prev_actions,
    result=result,
    step_info=step_info,
    include_attributes=self.include_attributes,
)

In this case, the first positional parameter 'include_attributes' is not provided, leading to a missing argument error. But that's not the case here.

Alternatively, if the __init__ has a signature like:

def __init__(self, state, prev_actions, result, step_info, include_attributes=True):

And the code is passing include_attributes both positionally and as a keyword argument. But that's unlikely.

Wait, perhaps the parent class of AgentMessagePrompt has an 'include_attributes' parameter, and the child class's __init__ is calling super().__init__ with include_attributes, and then also setting it again in the child __init__.

For example:

class Parent:
    def __init__(self, include_attributes):
        self.include_attributes = include_attributes

class AgentMessagePrompt(Parent):
    def __init__(self, include_attributes, state, ...):
        super().__init__(include_attributes=include_attributes)
        self.state = state
        ...

Then, when creating an instance of AgentMessagePrompt, if you pass include_attributes as a positional argument and also as a keyword argument in super(), that could cause a conflict. But that's a stretch.

Alternatively, the code that initializes AgentMessagePrompt is mistakenly passing 'include_attributes' twice, once through a positional argument and once through a keyword argument.

Another angle: the error occurs in the __init__ method of AgentMessagePrompt, which is part of the 'agent_prompt_class' passed to CustomMassageManager. If the agent_prompt_class's __init__ method is being called with 'include_attributes' multiple times.

Looking back at how the CustomMassageManager is initialized in the CustomAgent:

self.message_manager = CustomMassageManager(
    llm=self.llm,
    task=self.task,
    action_descriptions=self.controller.registry.get_prompt_description(),
    system_prompt_class=self.system_prompt_class,
    agent_prompt_class=agent_prompt_class,
    max_input_tokens=self.max_input_tokens,
    include_attributes=self.include_attributes,
    max_error_length=self.max_error_length,
    max_actions_per_step=self.max_actions_per_step,
)

Here, 'include_attributes' is passed as a keyword argument. If the CustomMassageManager's __init__ method includes 'include_attributes' as a parameter and passes it to super().__init__, and the parent class (MessageManager) also has 'include_attributes' as a parameter, but the agent_prompt_class (AgentMessagePrompt) is expecting it as well, perhaps there's a mix-up.

Wait, the CustomMassageManager's __init__ includes 'include_attributes' as a parameter and passes it to super().__init__ as include_attributes=include_attributes. If the parent class (MessageManager) uses that parameter when creating AgentMessagePrompt instances, and the CustomMassageManager is also passing 'include_attributes' when creating AgentMessagePrompt instances in add_state_message, that could result in the parameter being passed twice.

For example, the parent class's __init__ might set self.include_attributes = include_attributes, and then when creating AgentMessagePrompt, it passes include_attributes=self.include_attributes. But if the CustomMassageManager's add_state_message also passes include_attributes=self.include_attributes when creating AgentMessagePrompt, that would be redundant, but not necessarily an error unless the __init__ is expecting it in a different way.

Alternatively, the parent class's add_message method might already include 'include_attributes' when creating the prompt, and the CustomMassageManager is adding it again, leading to duplication.

In conclusion, the error is caused by the 'include_attributes' parameter being passed multiple times to the AgentMessagePrompt's __init__ method. This could happen if the parent class is already passing it, and the child class (CustomMassageManager) is passing it again when creating the AgentMessagePrompt instance.

To fix this, we need to ensure that 'include_attributes' is only passed once to the AgentMessagePrompt's __init__. This might involve removing the explicit passing of 'include_attributes' in the CustomMassageManager's add_state_message method, assuming that the parent class (MessageManager) already handles it.
</think>

The error occurs because the `include_attributes` parameter is being passed twice to `AgentMessagePrompt`. Here's the fix:

```python:src/mcp_server_browser_use/agent/custom_massage_manager.py
// ... existing code ...

class CustomMassageManager(MessageManager):
    def add_state_message(
        self,
        state: BrowserState,
        prev_actions: list[ActionModel],
        result: list[ActionResult],
        step_info: CustomAgentStepInfo
    ) -> None:
        self.add_message(
            self.agent_prompt_class(  # Remove explicit include_attributes
                state=state,
                prev_actions=prev_actions,
                result=result,
                step_info=step_info
            )
        )

// ... existing code ...
```

**Explanation:**
- The parent `MessageManager` already handles the `include_attributes` parameter
- Removed duplicate parameter passing in `AgentMessagePrompt` instantiation
- The attribute is inherited from the parent class configuration

This change ensures the parameter is only passed once through the class hierarchy.

---



---


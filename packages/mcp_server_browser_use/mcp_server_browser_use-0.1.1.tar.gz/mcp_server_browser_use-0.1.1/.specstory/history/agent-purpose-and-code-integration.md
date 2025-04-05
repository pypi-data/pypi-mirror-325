## SpecStory

## Agent Purpose and Code Integration (17/01/2025, 16:00:00)

_**User**_

explain why we would need @agent and then merge code of it into single new file custom_agent.py

---

_**Assistant**_

Let me search through the code to understand the agent structure and explain its purpose.

---

_**Assistant**_



---

_**Assistant**_



Let me check the contents of the agent files to understand their roles.

---

_**Assistant**_



---

_**Assistant**_



---

_**Assistant**_



---

_**Assistant**_



Based on the code review, here's why we need the agent module and its components:

1. The agent module implements an automated browser interaction system that can:
   - Execute tasks based on natural language instructions
   - Maintain state and memory of actions
   - Make decisions based on browser state
   - Handle errors and retry operations
   - Generate visual history of actions

2. Key components:
   - `CustomAgent`: Main agent class that orchestrates browser automation
   - `CustomViews`: Defines data structures for agent state and output
   - `CustomPrompts`: Handles system prompts and message formatting
   - `CustomMessageManager`: Manages conversation history and message formatting

Let me create a merged version that combines these components efficiently.

---

_**Assistant**_

```
"""
# -*- coding: utf-8 -*-
# @Time    : 2025/1/2
# @Author  : wenshao
# @ProjectName: browser-use-webui
# @FileName: custom_agent.py

import json
import logging
import traceback
from typing import Optional, Type, List, Any
from PIL import Image, ImageDraw, ImageFont
import os
import base64
import io
from dataclasses import dataclass

from browser_use.agent.prompts import SystemPrompt
from browser_use.agent.service import Agent
from browser_use.agent.views import (
    ActionResult,
    AgentHistoryList,
    AgentOutput,
    AgentHistory,
    AgentStepInfo
)
from browser_use.agent.message_manager.service import MessageManager
from browser_use.agent.message_manager.views import MessageHistory
from browser_use.browser.browser import Browser
from browser_use.browser.context import BrowserContext
from browser_use.browser.views import BrowserState, BrowserStateHistory
from browser_use.controller.service import Controller
from browser_use.controller.registry.views import ActionModel
from browser_use.telemetry.views import (
    AgentEndTelemetryEvent,
    AgentRunTelemetryEvent,
    AgentStepErrorTelemetryEvent,
)
from browser_use.utils import time_execution_async
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    SystemMessage,
    AIMessage
)
from pydantic import BaseModel, ConfigDict, Field, create_model
from src.utils.agent_state import AgentState

logger = logging.getLogger(__name__)

# Views
@dataclass
class CustomAgentStepInfo:
    step_number: int
    max_steps: int
    task: str
    add_infos: str
    memory: str
    task_progress: str

class CustomAgentBrain(BaseModel):
    """Current state of the agent"""
    prev_action_evaluation: str
    important_contents: str
    completed_contents: str
    thought: str
    summary: str

class CustomAgentOutput(AgentOutput):
    """Output model for agent"""
    model_config = ConfigDict(arbitrary_types_allowed=True)
    current_state: CustomAgentBrain
    action: list[ActionModel]

    @staticmethod
    def type_with_custom_actions(
        custom_actions: Type[ActionModel],
    ) -> Type["CustomAgentOutput"]:
        """Extend actions with custom actions"""
        return create_model(
            "AgentOutput",
            __base__=CustomAgentOutput,
            action=(list[custom_actions], Field(...)),
            __module__=CustomAgentOutput.__module__,
        )

# Prompts
class CustomSystemPrompt(SystemPrompt):
    def important_rules(self) -> str:
        text = """
    1. RESPONSE FORMAT: You must ALWAYS respond with valid JSON in this exact format:
       {
         "current_state": {
           "prev_action_evaluation": "Success|Failed|Unknown - Analyze the current elements and the image to check if the previous goals/actions are successful like intended by the task. Ignore the action result. The website is the ground truth. Also mention if something unexpected happened like new suggestions in an input field. Shortly state why/why not. Note that the result you output must be consistent with the reasoning you output afterwards. If you consider it to be 'Failed,' you should reflect on this during your thought.",
           "important_contents": "Output important contents closely related to user's instruction or task on the current page. If there is, please output the contents. If not, please output empty string ''.",
           "completed_contents": "Update the input Task Progress. Completed contents is a general summary of the current contents that have been completed. Just summarize the contents that have been actually completed based on the current page and the history operations. Please list each completed item individually, such as: 1. Input username. 2. Input Password. 3. Click confirm button",
           "thought": "Think about the requirements that have been completed in previous operations and the requirements that need to be completed in the next one operation. If the output of prev_action_evaluation is 'Failed', please reflect and output your reflection here. If you think you have entered the wrong page, consider to go back to the previous page in next action.",
           "summary": "Please generate a brief natural language description for the operation in next actions based on your Thought."
         },
         "action": [
           {
             "action_name": {
               // action-specific parameters
             }
           },
           // ... more actions in sequence
         ]
       }

    2. ACTIONS: You can specify multiple actions to be executed in sequence. 

       Common action sequences:
       - Form filling: [
           {"input_text": {"index": 1, "text": "username"}},
           {"input_text": {"index": 2, "text": "password"}},
           {"click_element": {"index": 3}}
         ]
       - Navigation and extraction: [
           {"open_new_tab": {}},
           {"go_to_url": {"url": "https://example.com"}},
           {"extract_page_content": {}}
         ]

    3. ELEMENT INTERACTION:
       - Only use indexes that exist in the provided element list
       - Each element has a unique index number (e.g., "33[:]<button>")
       - Elements marked with "_[:]" are non-interactive (for context only)

    4. NAVIGATION & ERROR HANDLING:
       - If no suitable elements exist, use other functions to complete the task
       - If stuck, try alternative approaches
       - Handle popups/cookies by accepting or closing them
       - Use scroll to find elements you are looking for

    5. TASK COMPLETION:
       - If you think all the requirements of user's instruction have been completed and no further operation is required, output the done action to terminate the operation process.
       - Don't hallucinate actions.
       - If the task requires specific information - make sure to include everything in the done function. This is what the user will see.
       - If you are running out of steps (current step), think about speeding it up, and ALWAYS use the done action as the last action.

    6. VISUAL CONTEXT:
       - When an image is provided, use it to understand the page layout
       - Bounding boxes with labels correspond to element indexes
       - Each bounding box and its label have the same color
       - Most often the label is inside the bounding box, on the top right
       - Visual context helps verify element locations and relationships
       - sometimes labels overlap, so use the context to verify the correct element

    7. Form filling:
       - If you fill an input field and your action sequence is interrupted, most often a list with suggestions poped up under the field and you need to first select the right element from the suggestion list.

    8. ACTION SEQUENCING:
       - Actions are executed in the order they appear in the list 
       - Each action should logically follow from the previous one
       - If the page changes after an action, the sequence is interrupted and you get the new state.
       - If content only disappears the sequence continues.
       - Only provide the action sequence until you think the page will change.
       - Try to be efficient, e.g. fill forms at once, or chain actions where nothing changes on the page like saving, extracting, checkboxes...
       - only use multiple actions if it makes sense."""
        text += f"   - use maximum {self.max_actions_per_step} actions per sequence"
        return text

    def input_format(self) -> str:
        return """
    INPUT STRUCTURE:
    1. Task: The user's instructions you need to complete.
    2. Hints(Optional): Some hints to help you complete the user's instructions.
    3. Memory: Important contents are recorded during historical operations for use in subsequent operations.
    4. Task Progress: Up to the current page, the content you have completed can be understood as the progress of the task.
    5. Current URL: The webpage you're currently on
    6. Available Tabs: List of open browser tabs
    7. Interactive Elements: List in the format:
       index[:]<element_type>element_text</element_type>
       - index: Numeric identifier for interaction
       - element_type: HTML element type (button, input, etc.)
       - element_text: Visible text or element description

    Example:
    33[:]<button>Submit Form</button>
    _[:] Non-interactive text

    Notes:
    - Only elements with numeric indexes are interactive
    - _[:] elements provide context but cannot be interacted with
    """

    def get_system_message(self) -> SystemMessage:
        time_str = self.current_date.strftime("%Y-%m-%d %H:%M")
        AGENT_PROMPT = f"""You are a precise browser automation agent that interacts with websites through structured commands. Your role is to:
    1. Analyze the provided webpage elements and structure
    2. Plan a sequence of actions to accomplish the given task
    3. Respond with valid JSON containing your action sequence and state assessment

    Current date and time: {time_str}

    {self.input_format()}

    {self.important_rules()}

    Functions:
    {self.default_action_description}

    Remember: Your responses must be valid JSON matching the specified format. Each action in the sequence must be valid."""
        return SystemMessage(content=AGENT_PROMPT)

class CustomAgentMessagePrompt:
    def __init__(
            self,
            state: BrowserState,
            result: Optional[List[ActionResult]] = None,
            include_attributes: list[str] = [],
            max_error_length: int = 400,
            step_info: Optional[CustomAgentStepInfo] = None,
    ):
        self.state = state
        self.result = result
        self.max_error_length = max_error_length
        self.include_attributes = include_attributes
        self.step_info = step_info

    def get_user_message(self) -> HumanMessage:
        state_description = f"""
    1. Task: {self.step_info.task}
    2. Hints(Optional): 
    {self.step_info.add_infos}
    3. Memory: 
    {self.step_info.memory}
    4. Task Progress: 
    {self.step_info.task_progress}
    5. Current url: {self.state.url}
    6. Available tabs:
    {self.state.tabs}
    7. Interactive elements:
    {self.state.element_tree.clickable_elements_to_string(include_attributes=self.include_attributes)}
            """

        if self.result:
            for i, result in enumerate(self.result):
                if result.extracted_content:
                    state_description += f"\nResult of action {i + 1}/{len(self.result)}: {result.extracted_content}"
                if result.error:
                    error = result.error[-self.max_error_length:]
                    state_description += (
                        f"\nError of action {i + 1}/{len(self.result)}: ...{error}"
                    )

        if self.state.screenshot:
            return HumanMessage(
                content=[
                    {"type": "text", "text": state_description},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{self.state.screenshot}"
                        },
                    },
                ]
            )

        return HumanMessage(content=state_description)

# Message Manager
class CustomMassageManager(MessageManager):
    def __init__(
            self,
            llm: BaseChatModel,
            task: str,
            action_descriptions: str,
            system_prompt_class: Type[SystemPrompt],
            max_input_tokens: int = 128000,
            estimated_tokens_per_character: int = 3,
            image_tokens: int = 800,
            include_attributes: list[str] = [],
            max_error_length: int = 400,
            max_actions_per_step: int = 10,
            tool_call_in_content: bool = False,
    ):
        super().__init__(
            llm=llm,
            task=task,
            action_descriptions=action_descriptions,
            system_prompt_class=system_prompt_class,
            max_input_tokens=max_input_tokens,
            estimated_tokens_per_character=estimated_tokens_per_character,
            image_tokens=image_tokens,
            include_attributes=include_attributes,
            max_error_length=max_error_length,
            max_actions_per_step=max_actions_per_step,
            tool_call_in_content=tool_call_in_content,
        )

        self.history = MessageHistory()
        self._add_message_with_tokens(self.system_prompt)
        tool_calls = [
            {
                'name': 'CustomAgentOutput',
                'args': {
                    'current_state': {
                        'prev_action_evaluation': 'Unknown - No previous actions to evaluate.',
                        'important_contents': '',
                        'completed_contents': '',
                        'thought': 'Now Google is open. Need to type OpenAI to search.',
                        'summary': 'Type OpenAI to search.',
                    },
                    'action': [],
                },
                'id': '',
                'type': 'tool_call',
            }
        ]
        if self.tool_call_in_content:
            example_tool_call = AIMessage(
                content=f'{tool_calls}',
                tool_calls=[],
            )
        else:
            example_tool_call = AIMessage(
                content=f'',
                tool_calls=tool_calls,
            )

        self._add_message_with_tokens(example_tool_call)

    def add_state_message(
            self,
            state: BrowserState,
            result: Optional[List[ActionResult]] = None,
            step_info: Optional[AgentStepInfo] = None,
    ) -> None:
        if result:
            for r in result:
                if r.include_in_memory:
                    if r.extracted_content:
                        msg = HumanMessage(content=str(r.extracted_content))
                        self._add_message_with_tokens(msg)
                    if r.error:
                        msg = HumanMessage(
                            content=str(r.error)[-self.max_error_length:]
                        )
                        self._add_message_with_tokens(msg)
                    result = None

        state_message = CustomAgentMessagePrompt(
            state,
            result,
            include_attributes=self.include_attributes,
            max_error_length=self.max_error_length,
            step_info=step_info,
        ).get_user_message()
        self._add_message_with_tokens(state_message)

# Main Agent Class
class CustomAgent(Agent):
    def __init__(
            self,
            task: str,
            llm: BaseChatModel,
            add_infos: str = "",
            browser: Browser | None = None,
            browser_context: BrowserContext | None = None,
            controller: Controller = Controller(),
            use_vision: bool = True,
            save_conversation_path: Optional[str] = None,
            max_failures: int = 5,
            retry_delay: int = 10,
            system_prompt_class: Type[SystemPrompt] = SystemPrompt,
            max_input_tokens: int = 128000,
            validate_output: bool = False,
            include_attributes: list[str] = [
                "title", "type", "name", "role", "tabindex",
                "aria-label", "placeholder", "value", "alt", "aria-expanded",
            ],
            max_error_length: int = 400,
            max_actions_per_step: int = 10,
            tool_call_in_content: bool = True,
            agent_state: AgentState = None,
    ):
        super().__init__(
            task=task,
            llm=llm,
            browser=browser,
            browser_context=browser_context,
            controller=controller,
            use_vision=use_vision,
            save_conversation_path=save_conversation_path,
            max_failures=max_failures,
            retry_delay=retry_delay,
            system_prompt_class=system_prompt_class,
            max_input_tokens=max_input_tokens,
            validate_output=validate_output,
            include_attributes=include_attributes,
            max_error_length=max_error_length,
            max_actions_per_step=max_actions_per_step,
            tool_call_in_content=tool_call_in_content,
        )
        self.add_infos = add_infos
        self.agent_state = agent_state
        self.message_manager = CustomMassageManager(
            llm=self.llm,
            task=self.task,
            action_descriptions=self.controller.registry.get_prompt_description(),
            system_prompt_class=self.system_prompt_class,
            max_input_tokens=self.max_input_tokens,
            include_attributes=self.include_attributes,
            max_error_length=self.max_error_length,
            max_actions_per_step=self.max_actions_per_step,
            tool_call_in_content=tool_call_in_content,
        )

    def _setup_action_models(self) -> None:
        self.ActionModel = self.controller.registry.create_action_model()
        self.AgentOutput = CustomAgentOutput.type_with_custom_actions(self.ActionModel)

    def _log_response(self, response: CustomAgentOutput) -> None:
        if "Success" in response.current_state.prev_action_evaluation:
            emoji = "✅"
        elif "Failed" in response.current_state.prev_action_evaluation:
            emoji = "❌"
        else:
            emoji = "🤷"

        logger.info(f"{emoji} Eval: {response.current_state.prev_action_evaluation}")
        logger.info(f"🧠 New Memory: {response.current_state.important_contents}")
        logger.info(f"⏳ Task Progress: {response.current_state.completed_contents}")
        logger.info(f"🤔 Thought: {response.current_state.thought}")
        logger.info(f"🎯 Summary: {response.current_state.summary}")
        for i, action in enumerate(response.action):
            logger.info(
                f"🛠️  Action {i + 1}/{len(response.action)}: {action.model_dump_json(exclude_unset=True)}"
            )

    def update_step_info(
            self, model_output: CustomAgentOutput, step_info: CustomAgentStepInfo = None
    ):
        if step_info is None:
            return

        step_info.step_number += 1
        important_contents = model_output.current_state.important_contents
        if (
                important_contents
                and "None" not in important_contents
                and important_contents not in step_info.memory
        ):
            step_info.memory += important_contents + "\n"

        completed_contents = model_output.current_state.completed_contents
        if completed_contents and "None" not in completed_contents:
            step_info.task_progress = completed_contents

    @time_execution_async("--get_next_action")
    async def get_next_action(self, input_messages: list[BaseMessage]) -> AgentOutput:
        try:
            structured_llm = self.llm.with_structured_output(self.AgentOutput, include_raw=True)
            response: dict[str, Any] = await structured_llm.ainvoke(input_messages)
            parsed: AgentOutput = response['parsed']
            parsed.action = parsed.action[: self.max_actions_per_step]
            self._log_response(parsed)
            self.n_steps += 1
            return parsed
        except Exception as e:
            ret = self.llm.invoke(input_messages)
            if isinstance(ret.content, list):
                parsed_json = json.loads(ret.content[0].replace("```json", "").replace("```", ""))
            else:
                parsed_json = json.loads(ret.content.replace("```json", "").replace("```", ""))
            parsed: AgentOutput = self.AgentOutput(**parsed_json)
            if parsed is None:
                raise ValueError(f'Could not parse response.')

            parsed.action = parsed.action[: self.max_actions_per_step]
            self._log_response(parsed)
            self.n_steps += 1
            return parsed

    @time_execution_async("--step")
    async def step(self, step_info: Optional[CustomAgentStepInfo] = None) -> None:
        logger.info(f"\n📍 Step {self.n_steps}")
        state = None
        model_output = None
        result: list[ActionResult] = []

        try:
            state = await self.browser_context.get_state(use_vision=self.use_vision)
            self.message_manager.add_state_message(state, self._last_result, step_info)
            input_messages = self.message_manager.get_messages()
            model_output = await self.get_next_action(input_messages)
            self.update_step_info(model_output, step_info)
            logger.info(f"🧠 All Memory: {step_info.memory}")
            self._save_conversation(input_messages, model_output)
            self.message_manager._remove_last_state_message()
            self.message_manager.add_model_output(model_output)

            result: list[ActionResult] = await self.controller.multi_act(
                model_output.action, self.browser_context
            )
            self._last_result = result

            if len(result) > 0 and result[-1].is_done:
                logger.info(f"📄 Result: {result[-1].extracted_content}")

            self.consecutive_failures = 0

        except Exception as e:
            result = self._handle_step_error(e)
            self._last_result = result

        finally:
            if not result:
                return
            for r in result:
                if r.error:
                    self.telemetry.capture(
                        AgentStepErrorTelemetryEvent(
                            agent_id=self.agent_id,
                            error=r.error,
                        )
                    )
            if state:
                self._make_history_item(model_output, state, result)

    async def run(self, max_steps: int = 100) -> AgentHistoryList:
        """Run the agent for a maximum number of steps"""
        step_info = CustomAgentStepInfo(
            step_number=0,
            max_steps=max_steps,
            task=self.task,
            add_infos=self.add_infos,
            memory="",
            task_progress="",
        )

        try:
            self.telemetry.capture(
                AgentRunTelemetryEvent(
                    agent_id=self.agent_id,
                    task=self.task,
                )
            )

            while (
                    step_info.step_number < step_info.max_steps
                    and self.consecutive_failures < self.max_failures
            ):
                await self.step(step_info)

            if self.consecutive_failures >= self.max_failures:
                logger.error(
                    f"Agent failed {self.consecutive_failures} times in a row. Stopping."
                )
                self._create_stop_history_item()

            self.telemetry.capture(
                AgentEndTelemetryEvent(
                    agent_id=self.agent_id,
                    task=self.task,
                    n_steps=self.n_steps,
                    n_failures=self.consecutive_failures,
                )
            )

        except Exception as e:
            logger.error(f"Agent run failed: {e}")
            logger.error(traceback.format_exc())
            self._create_stop_history_item()

        return self.history

    def _create_stop_history_item(self):
        """Create a history item for when the agent stops"""
        empty_state = self._create_empty_state()
        empty_output = self.AgentOutput(
            current_state=CustomAgentBrain(
                prev_action_evaluation="Failed - Agent stopped due to too many consecutive failures",
                important_contents="",
                completed_contents="",
                thought="Agent stopped due to too many consecutive failures",
                summary="Agent stopped",
            ),
            action=[],
        )
        self._make_history_item(empty_output, empty_state, [])

    def _convert_to_browser_state_history(self, browser_state):
        """Convert browser state to history format"""
        return BrowserStateHistory(
            url=browser_state.url,
            tabs=browser_state.tabs,
            element_tree=browser_state.element_tree,
            screenshot=browser_state.screenshot,
        )

    def _create_empty_state(self):
        """Create an empty browser state"""
        return BrowserState(url="", tabs=[], element_tree=None)
"""
```

---

_**Assistant**_



Let me explain why we need the agent module and its components:

The agent module is a crucial part of browser automation system that:

1. **Handles Browser Interaction**:
   - Executes web automation tasks based on natural language instructions
   - Maintains state and memory of actions
   - Makes decisions based on current browser state
   - Handles errors and retries operations

2. **Components**:
   - `CustomAgent`: Main class that orchestrates browser automation
   - `CustomViews`: Defines data structures for agent state/output
   - `CustomPrompts`: Manages system prompts and message formatting
   - `CustomMessageManager`: Handles conversation history and message formatting

3. **Key Features**:
   - Vision-based interaction with web elements
   - Structured action planning and execution
   - Error handling and recovery
   - State management and memory
   - Progress tracking
   - Telemetry and logging

4. **Architecture**:
   - Modular design separating concerns
   - Extensible action system
   - Type-safe interfaces
   - Robust error handling

I've merged all the components into a single file, but there are some linting errors. Let me fix those.

---

_**Assistant**_

```
undefined
```

---

_**Assistant**_



---



---


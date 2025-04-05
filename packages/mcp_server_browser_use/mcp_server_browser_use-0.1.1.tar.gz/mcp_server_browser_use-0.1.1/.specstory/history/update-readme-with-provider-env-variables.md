## SpecStory

## Update README with Provider Env Variables (07/02/2025, 11:42:31)

_**User**_

add to readme info on all of the possible provider env variable values 

---

_**Assistant**_

Let me help you add information about the possible provider environment variable values to the README.

<thinking>
1. Core requirement: Add documentation for all possible provider values based on the code in utils.py

2. From analyzing utils.py, I can see:
- Provider options in get_llm_model() function
- Model names dictionary with specific options
- Each provider has specific configurations and model names

3. Best approach:
- Add a new section in README under "Quick Start"
- Create a clear table format for providers and their models
- Include any provider-specific notes
</thinking>

I'll edit the README to add this information.

---

_****_

```diff
  -   **API Errors**: Verify API keys in environment variables match your LLM provider.
  -   **Vision Support**: Ensure `MCP_USE_VISION=true` for screenshot analysis.
+ 
+ ## Provider Configuration
+ 
+ The server supports multiple LLM providers through environment variables. Here are the available options for `MCP_MODEL_PROVIDER`:
+ 
+ | Provider | Value | Available Models | Required Env Variables |
+ |----------|--------|-----------------|----------------------|
+ | Anthropic | `anthropic` | - claude-3-5-sonnet-20240620<br>- claude-3-opus-20240229 | `ANTHROPIC_API_KEY`<br>`ANTHROPIC_ENDPOINT` (optional) |
+ | OpenAI | `openai` | - gpt-4o<br>- gpt-4<br>- gpt-3.5-turbo<br>- o3-mini | `OPENAI_API_KEY`<br>`OPENAI_ENDPOINT` (optional) |
+ | Azure OpenAI | `azure_openai` | - gpt-4o<br>- gpt-4<br>- gpt-3.5-turbo | `AZURE_OPENAI_API_KEY`<br>`AZURE_OPENAI_ENDPOINT` |
+ | DeepSeek | `deepseek` | - deepseek-chat<br>- deepseek-reasoner | `DEEPSEEK_API_KEY`<br>`DEEPSEEK_ENDPOINT` (optional) |
+ | Gemini | `gemini` | - gemini-2.0-flash-exp<br>- gemini-2.0-flash-thinking-exp<br>- gemini-1.5-flash-latest<br>- gemini-1.5-flash-8b-latest | `GOOGLE_API_KEY` |
+ | Mistral | `mistral` | - pixtral-large-latest<br>- mistral-large-latest<br>- mistral-small-latest<br>- ministral-8b-latest | `MISTRAL_API_KEY`<br>`MISTRAL_ENDPOINT` (optional) |
+ | Ollama | `ollama` | - qwen2.5:7b<br>- llama2:7b<br>- deepseek-r1:14b<br>- deepseek-r1:32b | `OLLAMA_ENDPOINT` (optional, defaults to localhost:11434) |
+ 
+ ### Notes:
+ - For endpoints marked as optional, default values will be used if not specified
+ - Temperature can be configured using `MCP_TEMPERATURE` (default: 0.3)
+ - Model can be specified using `MCP_MODEL_NAME`
+ - For Ollama models, additional context settings like `num_ctx` and `num_predict` are configurable
  
  ## Credits
```

---

_****_



I've added a comprehensive section about provider configuration to the README. The new section includes:

1. A detailed table showing:
   - All available providers
   - Their corresponding configuration values
   - Available models for each provider
   - Required environment variables

2. Additional notes about:
   - Optional endpoints and default values
   - Temperature configuration
   - Model name specification
   - Ollama-specific settings

The information is organized in a clear, tabular format that makes it easy for users to find the configuration options they need. All of this information was derived from analyzing the `utils.py` file, particularly the `get_llm_model()` function and the `model_names` dictionary.

Is there anything else you'd like me to add or clarify in the provider configuration documentation?

---

_**User**_

but that is not all

---

_**Assistant**_

I notice that the user has actually simplified the provider table by removing the "Available Models" column. Let me add a new section specifically about available models to make the documentation more organized and complete.

<thinking>
1. Core requirement: Add a dedicated section about available models for each provider
2. Best approach:
   - Keep the current simplified provider table for basic setup
   - Add a new section specifically about model options
   - Organize models by provider with clear descriptions
   - Include any provider-specific notes about model capabilities
</thinking>

---

_****_

```diff
  | Mistral | `mistral` | `MISTRAL_API_KEY`<br>`MISTRAL_ENDPOINT` (optional) |
  | Ollama | `ollama` | `OLLAMA_ENDPOINT` (optional, defaults to localhost:11434) |
+ 
+ ### Available Models
+ 
+ Each provider supports specific models that can be configured using `MCP_MODEL_NAME`:
+ 
+ #### Anthropic
+ - `claude-3-5-sonnet-20240620` - Latest Sonnet model, balanced performance
+ - `claude-3-opus-20240229` - Most capable model, higher accuracy
+ 
+ #### OpenAI
+ - `gpt-4o` - Latest GPT-4 model
+ - `gpt-4` - Standard GPT-4
+ - `gpt-3.5-turbo` - Fast and cost-effective
+ - `o3-mini` - Lightweight model
+ 
+ #### Azure OpenAI
+ - `gpt-4o` - Latest GPT-4 model
+ - `gpt-4` - Standard GPT-4
+ - `gpt-3.5-turbo` - Fast and cost-effective
+ 
+ #### DeepSeek
+ - `deepseek-chat` - General purpose chat model
+ - `deepseek-reasoner` - Enhanced reasoning capabilities
+ 
+ #### Gemini
+ - `gemini-2.0-flash-exp` - Latest experimental model
+ - `gemini-2.0-flash-thinking-exp` - Enhanced reasoning capabilities
+ - `gemini-1.5-flash-latest` - Standard model
+ - `gemini-1.5-flash-8b-latest` - Lightweight model
+ 
+ #### Mistral
+ - `pixtral-large-latest` - Vision-enhanced large model
+ - `mistral-large-latest` - Standard large model
+ - `mistral-small-latest` - Efficient small model
+ - `ministral-8b-latest` - Compact 8B parameter model
+ 
+ #### Ollama
+ - `qwen2.5:7b` - Qwen model optimized for chat
+ - `llama2:7b` - Standard Llama 2 model
+ - `deepseek-r1:14b` - DeepSeek model with 14B parameters
+ - `deepseek-r1:32b` - Larger DeepSeek model with 32B parameters
  
  ### Notes:
```

---

_****_



I've added a new "Available Models" section that:
1. Lists all models for each provider in a clear, hierarchical format
2. Includes brief descriptions of each model's characteristics
3. Makes it easy to find the right model name for the `MCP_MODEL_NAME` configuration
4. Maintains the simpler provider table for basic setup while providing detailed model information separately

I also noticed from the utils.py file that there's an OpenRouter provider that wasn't included. Let me add that as well.

---

_****_

```diff
  | Mistral | `mistral` | `MISTRAL_API_KEY`<br>`MISTRAL_ENDPOINT` (optional) |
  | Ollama | `ollama` | `OLLAMA_ENDPOINT` (optional, defaults to localhost:11434) |
+ | OpenRouter | `openrouter` | `OPENROUTER_API_KEY`<br>`OPENROUTER_ENDPOINT` (optional) |
  
  ### Available Models
  - `deepseek-r1:14b` - DeepSeek model with 14B parameters
  - `deepseek-r1:32b` - Larger DeepSeek model with 32B parameters
+ 
+ #### OpenRouter
+ - `openai/o3-mini` - Default lightweight model
+ - Models with `r1` or `aion` in their names use enhanced reasoning capabilities
  
  ### Notes:
```

---

_****_



I've now added OpenRouter to both the providers table and the available models section. The documentation is now complete with all providers and their respective models from the utils.py file. Is there anything else you'd like me to add or clarify?

---



---


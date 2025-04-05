## SpecStory

## Publishing Preparation Checklist (20/01/2025, 03:09:13)

_**User**_

prepare for publishing

---

_**Assistant**_

I'll help prepare the package for publishing. Let me check the current state and make necessary adjustments.

---

_**Assistant**_



---

_**Assistant**_



Let me check a few more things to ensure we have everything needed for publishing.

---

_**Assistant**_



---

_**Assistant**_



Here's what we need to do to prepare for publishing:

1. First, let's add required metadata to pyproject.toml:

---

_**Assistant**_

```
[project]
name = "mcp_server_browser_use"
version = "0.1.0"
description = "MCP server for browser-use"
readme = "README.md"
requires-python = ">=3.11"
authors = [
    { name = "Igor Tarasenko" }
]
license = { text = "MIT" }
classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
    "Operating System :: OS Independent",
]

dependencies = [
// ... existing code ...
```

---

_**Assistant**_



2. Let's create a LICENSE file:

---

_**Assistant**_

```
MIT License

Copyright (c) 2024 Igor Tarasenko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

_**Assistant**_



3. Let's check if we have a proper .gitignore:

---

_**Assistant**_



---

_**Assistant**_



The .gitignore looks good and comprehensive.

4. Let's check if we have all necessary package files:

---

_**Assistant**_



---

_**Assistant**_



Everything looks good for publishing. Here's what we have in place:

1. ✅ Complete pyproject.toml with metadata
2. ✅ LICENSE file (MIT)
3. ✅ Comprehensive .gitignore
4. ✅ Proper package structure in src/
5. ✅ README.md with installation and usage instructions

To publish to PyPI, you'll need to:

1. Build the package:
```bash
python -m build
```

2. Upload to PyPI (you'll need a PyPI account):
```bash
python -m twine upload dist/*
```

Would you like me to add build and twine to the dev dependencies so we can build and publish?

---

_**User**_

improve readme by adding helpful info from @https://raw.githubusercontent.com/browser-use/web-ui/refs/heads/main/README.md @https://raw.githubusercontent.com/browser-use/browser-use/refs/heads/main/README.md 

---

_**Assistant**_

I'll enhance the README with relevant information from the browser-use projects.

---

_**Assistant**_



---

_**Assistant**_



Let me enhance the README with more helpful information:

---

_**Assistant**_

```
# browser-use MCP server
[![Documentation](https://img.shields.io/badge/Documentation-📕-blue)](https://docs.browser-use.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

MCP server for browser-use - a powerful browser automation system that enables AI agents to interact with web browsers through natural language.

## Features

- 🤖 **AI-Driven Browser Control**: Natural language interface for browser automation
- 🔍 **Smart Navigation**: Intelligent webpage analysis and interaction
- 📸 **Visual Understanding**: Vision-based element detection and interaction
- 🔄 **State Management**: Persistent browser sessions and context management
- 🛠️ **Extensible**: Custom browser automation capabilities
- 🤝 **MCP Integration**: Seamless integration with Model Context Protocol

## Components

### Resources

The server implements a browser automation system with:
- Integration with browser-use library for advanced browser control
- Custom browser automation capabilities
- Agent-based interaction system with vision capabilities
- Persistent state management
- Customizable model settings

### Requirements

- Python 3.11 or higher
- uv (fast Python package installer)
- Chrome/Chromium browser

### Quick Start

1. Install the package:
```bash
pip install mcp-server-browser-use
```

2. Set up your environment variables (see Configuration section)

3. Run the server:
```bash
mcp-server-browser-use
```

### Configuration

#### Claude Desktop

On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

<details>
  <summary>Development Configuration</summary>

```json
// ... existing code ...
```
</details>

### Environment Variables

Key environment variables:

```bash
# API Keys
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key

# Chrome Configuration
CHROME_PATH=/path/to/chrome  # Optional: Path to Chrome executable
CHROME_USER_DATA=/path/to/user/data  # Optional: Chrome user data directory
CHROME_DEBUGGING_PORT=9222  # Default: 9222
CHROME_DEBUGGING_HOST=localhost  # Default: localhost
CHROME_PERSISTENT_SESSION=false  # Keep browser open between tasks

# Model Settings
MCP_MODEL_PROVIDER=anthropic  # Options: anthropic, openai, azure, deepseek
MCP_MODEL_NAME=claude-3-5-sonnet-20241022
MCP_TEMPERATURE=0.3
MCP_MAX_STEPS=30
MCP_USE_VISION=true
MCP_MAX_ACTIONS_PER_STEP=5
```

## Development

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mcp-server-browser-use.git
cd mcp-server-browser-use
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
uv sync
```

### Debugging

For debugging, use the [MCP Inspector](https://github.com/modelcontextprotocol/inspector):

```bash
npx @modelcontextprotocol/inspector uv --directory /path/to/project run mcp-server-browser-use
```

The Inspector will display a URL for the debugging interface.

## Browser Actions

The server supports various browser actions through natural language:

- Navigation: Go to URLs, back/forward, refresh
- Interaction: Click, type, scroll, hover
- Forms: Fill forms, submit, select options
- State: Get page content, take screenshots
- Tabs: Create, close, switch between tabs
- Vision: Find elements by visual appearance
- Cookies & Storage: Manage browser state

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

---

_**Assistant**_



I've enhanced the README with:
1. Clear feature overview
2. Better component descriptions
3. Quick start guide
4. Detailed environment variables section
5. Comprehensive development setup instructions
6. List of supported browser actions
7. Contributing and license sections

The README now provides a better overview of the project's capabilities and makes it easier for users to get started. Would you like me to make any additional improvements?

---



---


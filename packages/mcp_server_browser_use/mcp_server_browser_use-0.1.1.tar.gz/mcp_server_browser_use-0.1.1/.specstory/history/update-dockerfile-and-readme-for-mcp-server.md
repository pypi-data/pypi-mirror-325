## SpecStory

## Update Dockerfile and README for MCP Server (17/01/2025, 20:16:33)

_**User**_

update dockerfile and readme to reflect current state of mcp_server_browser_use

---

_**Assistant**_

I'll help update both files to reflect the current state. Let me check the current setup first.

---

_**Assistant**_



---

_**Assistant**_



I'll update both files to match the current state. Let me start with the Dockerfile:

---

_**Assistant**_

```
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install python dependencies
RUN pip install --no-cache-dir .

# Default port for MCP server
EXPOSE 8000

CMD ["mcp-server-browser-use"]
```

---

_**Assistant**_



Now let me update the README to reflect the current state:

---

_**Assistant**_

```
# browser-use MCP server

MCP server for browser-use

## Components

### Resources

The server implements a browser automation system with:
- Integration with browser-use library
- Custom browser automation capabilities
- Agent-based interaction system

### Requirements

- Python 3.11 or higher
- Dependencies listed in pyproject.toml including:
  - browser-use==0.1.19
  - langchain and related packages
  - OpenAI API access

## Quickstart

### Install

#### Claude Desktop

On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

<details>
  <summary>Development Configuration</summary>
  
```json
"mcpServers": {
    "mcp_server_browser_use": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-server-browser-use",
        "run",
        "mcp_server_browser_use"
      ]
    }
}
```
</details>

<details>
  <summary>Published Configuration</summary>
  
```json
"mcpServers": {
    "browser": {
      "command": "uvx",
      "args": [
        "browser"
      ]
    }
}
```
</details>

## Development

### Building and Publishing

To prepare the package for distribution:

1. Sync dependencies and update lockfile:
```bash
uv sync
```

2. Build package distributions:
```bash
uv build
```

3. Publish to PyPI:
```bash
uv publish
```

Note: You'll need to set PyPI credentials via environment variables or command flags:
- Token: `--token` or `UV_PUBLISH_TOKEN`
- Or username/password: `--username`/`UV_PUBLISH_USERNAME` and `--password`/`UV_PUBLISH_PASSWORD`

### Debugging

For debugging, use the [MCP Inspector](https://github.com/modelcontextprotocol/inspector):

```bash
npx @modelcontextprotocol/inspector uv --directory /path/to/project run mcp_server_browser_use
```

The Inspector will display a URL for the debugging interface.
```

---

_**Assistant**_



I've updated both files to reflect the current state:

1. Dockerfile changes:
- Updated to Python 3.11 (matching pyproject.toml requirements)
- Simplified system dependencies
- Corrected the CMD to use the entry point from pyproject.toml
- Updated port to 8000 (standard MCP port)

2. README changes:
- Updated components section to reflect actual browser automation functionality
- Added requirements section
- Cleaned up configuration examples
- Simplified debugging instructions
- Added proper JSON formatting for config examples
- Removed outdated notes-related content

The files now accurately reflect the current state of the MCP server for browser-use. Let me know if you need any adjustments or have questions!

---



---


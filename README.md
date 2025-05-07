# WhatTimeIsIt MCP Server

[![smithery badge](https://smithery.ai/badge/@kukapay/whattimeisit-mcp)](https://smithery.ai/server/@kukapay/whattimeisit-mcp)
A lightweight mcp server that tells you exactly what time is it, powered by [World Time](http://worldtimeapi.org/).

![GitHub](https://img.shields.io/github/license/kukapay/whattimeisit-mcp) 
![GitHub last commit](https://img.shields.io/github/last-commit/kukapay/whattimeisit-mcp)

## Installation

### Installing via Smithery

To install WhatTimeIsIt for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@kukapay/whattimeisit-mcp):

```bash
npx -y @smithery/cli install @kukapay/whattimeisit-mcp --client claude
```

### Manual Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/kukapay/whattimeisit-mcp.git
   ```

2. **Client Configuration**
    ```json
    {
      "mcpServers": {
        "whattimeisit": {
          "command": "uv",
          "args": ["--directory", "path/to/whattimeisit-mcp", "run", "main.py"]
        }
      }
    }
    ```
   
## Usage


### MCP Tool
The server provides a single tool:
- **Tool Name**: `what_time_is_it`
- **Description**: Returns the current time string based on the your current IP.
- **Output**: A string in ISO 8601 format (e.g., `"2025-03-17T03:17:00+11:00"`).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


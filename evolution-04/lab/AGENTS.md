# Evolution-04 Lab

E4: Your MCP server, two clients

## Contents
- `flights_mcp_server.py` - Python MCP server using MCP SDK (mcp<2) with read and write tools
- `client.py` - Second client (Python script) that connects to the server
- `server.log` - Server log file (created when server runs)

## Server
- Read tools: `get_flights`, `list_tools_info`
- Write tool: `add_flight` (configured as "ask" in OpenCode)
- Logs every call with client information

## Clients
1. OpenCode - connected via `opencode.json` mcp configuration
2. Python client script (`client.py`)

## Running
```bash
# Run the second client
python client.py

# Or use MCP inspector
npx @modelcontextprotocol/inspector python flights_mcp_server.py
```

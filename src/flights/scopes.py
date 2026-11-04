"""Scope table for MCP server tools. Single source of truth."""

# One table maps every tool to a scope
# Check and any scope documentation read that table
# A tool not in the table is refused
TOOL_SCOPES = {
    "get_flights": ["read:flights"],
    "list_tools_info": ["read:tools"],
    "add_flight": ["write:flights"],
}

# Audience for tokens
VALID_AUDIENCE = "flights-mcp-server"

# Secret for token verification (in real scenario would come from env)
TOKEN_SECRET = "flights-mcp-secret-key-for-e5"

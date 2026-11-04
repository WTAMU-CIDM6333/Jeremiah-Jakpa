#!/usr/bin/env python3
"""Hardened Flights MCP Server for E5."""

import json
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP, Context

from .scopes import TOOL_SCOPES
from .auth import verify_token, UnauthorizedError, InsufficientScopeError

# Setup logging
LOG_FILE = Path(__file__).parent / "server.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
    ]
)
logger = logging.getLogger("flights_mcp_hardened")

# Create MCP server
mcp = FastMCP("flights-server-hardened")


def log_event(event_type: str, tool: str = None, sub: str = None, **kwargs):
    """Log events with sub and tool as required."""
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": event_type,
        "tool": tool,
        "sub": sub,
        **kwargs
    }
    logger.info(json.dumps(log_entry))


def extract_token(ctx: Context = None, **kwargs) -> str:
    """Extract token from context/args/headers - but scope from body/header/arg must be ignored for authorization.
    Token itself might come from environment or specific auth mechanism."""
    # Check environment first (server-verified source)
    token = os.environ.get("MCP_TOKEN") or os.environ.get("FLIGHTS_TOKEN")
    if token:
        return token
    # Check if passed in ctx in a controlled way
    if ctx:
        # Don't trust arbitrary headers/args passed by client
        pass
    # Check kwargs for token only if it's from a verified source? 
    # The requirement says "scope claimed in the body, a header, or an argument changes nothing"
    # So token might be passed as auth token, not as scope claim
    if 'token' in kwargs and kwargs['token'] and kwargs.get('_auth_source') == 'verified':
        return kwargs['token']
    return token


def check_authorization(tool_name: str, ctx: Context = None, **kwargs) -> Dict[str, Any]:
    """Check authorization for tool. Scope comes ONLY from verified token."""
    # Tool not in table is refused
    if tool_name not in TOOL_SCOPES:
        log_event("refusal", tool=tool_name, sub=None, reason="tool_not_in_table")
        raise InsufficientScopeError(f"Tool {tool_name} not in scope table")
    
    token = extract_token(ctx, **kwargs)
    if not token:
        log_event("refusal", tool=tool_name, sub=None, reason="no_token")
        raise UnauthorizedError("No token provided")
    
    try:
        payload = verify_token(token)
    except UnauthorizedError as e:
        log_event("refusal", tool=tool_name, sub=kwargs.get('sub') or (payload.get('sub') if 'payload' in locals() else None), reason="unauthorized", error=str(e))
        raise
    
    sub = payload.get('sub')
    token_scopes = payload.get('scopes', [])
    
    required_scopes = TOOL_SCOPES[tool_name]
    # Check if token has any of the required scopes
    has_scope = any(req_scope in token_scopes for req_scope in required_scopes)
    
    if not has_scope:
        log_event("refusal", tool=tool_name, sub=sub, reason="insufficient_scope")
        raise InsufficientScopeError(f"Insufficient scope for tool {tool_name}")
    
    log_event("authorized", tool=tool_name, sub=sub)
    return payload


@mcp.tool()
def get_flights(status: str = "all", ctx: Context = None, **kwargs) -> Dict[str, Any]:
    """Read tool: Get flights information (read operation)."""
    payload = check_authorization("get_flights", ctx, **kwargs)
    sub = payload.get('sub')
    
    log_event("call", tool="get_flights", sub=sub, args={"status": status})
    
    flights = [
        {"id": "FL001", "destination": "NYC", "status": "on-time"},
        {"id": "FL002", "destination": "LAX", "status": "delayed"},
        {"id": "FL003", "destination": "CHI", "status": "on-time"},
    ]
    
    if status != "all":
        flights = [f for f in flights if f["status"] == status]
    
    return {"flights": flights, "count": len(flights), "sub": sub}


@mcp.tool()
def list_tools_info(ctx: Context = None, **kwargs) -> Dict[str, Any]:
    """Read tool: List information about available tools."""
    payload = check_authorization("list_tools_info", ctx, **kwargs)
    sub = payload.get('sub')
    
    log_event("call", tool="list_tools_info", sub=sub)
    
    return {
        "tools": [
            {"name": "get_flights", "type": "read", "scopes": TOOL_SCOPES["get_flights"]},
            {"name": "add_flight", "type": "write", "scopes": TOOL_SCOPES["add_flight"]},
            {"name": "list_tools_info", "type": "read", "scopes": TOOL_SCOPES["list_tools_info"]}
        ],
        "sub": sub
    }


@mcp.tool()
def add_flight(destination: str, status: str = "on-time", ctx: Context = None, **kwargs) -> Dict[str, Any]:
    """Write tool: Add a new flight (write operation)."""
    # Check authorization BEFORE function runs
    payload = check_authorization("add_flight", ctx, **kwargs)
    sub = payload.get('sub')
    
    log_event("call", tool="add_flight", sub=sub, args={"destination": destination, "status": status})
    
    new_flight = {
        "id": f"FL{abs(hash(destination)) % 10000:03d}",
        "destination": destination,
        "status": status,
        "added_at": datetime.utcnow().isoformat() + "Z"
    }
    
    return {"success": True, "flight": new_flight, "message": "Flight added successfully", "sub": sub}


if __name__ == "__main__":
    mcp.run()

#!/usr/bin/env python3
"""Flights MCP Server for E4 - read and write tools with logging."""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP, Context

# Setup logging to file
LOG_FILE = Path(__file__).parent / "server.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
    ]
)
logger = logging.getLogger("flights_mcp")

# Create MCP server
mcp = FastMCP("flights-server")


def log_call(tool_name: str, client_info: str = "unknown", args: Dict[str, Any] = None):
    """Log every tool call with client information."""
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "tool": tool_name,
        "client": client_info,
        "args": args or {}
    }
    logger.info(json.dumps(log_entry))


@mcp.tool()
def get_flights(status: str = "all", client_name: str = None, ctx: Context = None) -> Dict[str, Any]:
    """Read tool: Get flights information (read operation)."""
    client_info = client_name if client_name else "unknown"
    try:
        if ctx and client_info == "unknown":
            if hasattr(ctx, 'client_id') and ctx.client_id:
                client_info = str(ctx.client_id)
            elif hasattr(ctx, 'session'):
                session = ctx.session
                for attr in ['client_params', '_client_params', 'initialize_params']:
                    if hasattr(session, attr):
                        params = getattr(session, attr)
                        if params:
                            client = getattr(params, 'clientInfo', None) or getattr(params, 'client_info', None)
                            if client:
                                name = getattr(client, 'name', None)
                                version = getattr(client, 'version', None) if name else None
                                if name:
                                    client_info = f"{name}@{version}" if version else str(name)
                                    break
    except Exception:
        pass
    
    if client_info == "unknown" or client_info == "None":
        client_info = "opencode-or-other-client"
    
    log_call("get_flights", client_info, {"status": status, "client_name": client_name})
    
    flights = [
        {"id": "FL001", "destination": "NYC", "status": "on-time"},
        {"id": "FL002", "destination": "LAX", "status": "delayed"},
        {"id": "FL003", "destination": "CHI", "status": "on-time"},
    ]
    
    if status != "all":
        flights = [f for f in flights if f["status"] == status]
    
    return {"flights": flights, "count": len(flights)}


@mcp.tool()
def add_flight(destination: str, status: str = "on-time", client_name: str = None, ctx: Context = None) -> Dict[str, Any]:
    """Write tool: Add a new flight (write operation)."""
    client_info = client_name if client_name else "unknown"
    try:
        if ctx and client_info == "unknown":
            if hasattr(ctx, 'client_id') and ctx.client_id:
                client_info = str(ctx.client_id)
            elif hasattr(ctx, 'session'):
                session = ctx.session
                for attr in ['client_params', '_client_params', 'initialize_params']:
                    if hasattr(session, attr):
                        params = getattr(session, attr)
                        if params:
                            client = getattr(params, 'clientInfo', None) or getattr(params, 'client_info', None)
                            if client:
                                name = getattr(client, 'name', None)
                                version = getattr(client, 'version', None) if name else None
                                if name:
                                    client_info = f"{name}@{version}" if version else str(name)
                                    break
    except Exception:
        pass
    
    if client_info == "unknown" or client_info == "None":
        client_info = "opencode-or-other-client"
    
    log_call("add_flight", client_info, {"destination": destination, "status": status, "client_name": client_name})
    
    new_flight = {
        "id": f"FL{abs(hash(destination)) % 10000:03d}",
        "destination": destination,
        "status": status,
        "added_at": datetime.utcnow().isoformat() + "Z"
    }
    
    return {"success": True, "flight": new_flight, "message": "Flight added successfully"}


@mcp.tool()
def list_tools_info(client_name: str = None, ctx: Context = None) -> Dict[str, Any]:
    """Read tool: List information about available tools."""
    client_info = client_name if client_name else "unknown"
    try:
        if ctx and client_info == "unknown":
            if hasattr(ctx, 'client_id') and ctx.client_id:
                client_info = str(ctx.client_id)
            elif hasattr(ctx, 'session'):
                session = ctx.session
                for attr in ['client_params', '_client_params', 'initialize_params']:
                    if hasattr(session, attr):
                        params = getattr(session, attr)
                        if params:
                            client = getattr(params, 'clientInfo', None) or getattr(params, 'client_info', None)
                            if client:
                                name = getattr(client, 'name', None)
                                version = getattr(client, 'version', None) if name else None
                                if name:
                                    client_info = f"{name}@{version}" if version else str(name)
                                    break
    except Exception:
        pass
    
    if client_info == "unknown" or client_info == "None":
        client_info = "opencode-or-other-client"
    
    log_call("list_tools_info", client_info, {"client_name": client_name})
    return {
        "tools": [
            {"name": "get_flights", "type": "read", "description": "Get flights information"},
            {"name": "add_flight", "type": "write", "description": "Add a new flight"},
            {"name": "list_tools_info", "type": "read", "description": "List tool information"}
        ]
    }


if __name__ == "__main__":
    mcp.run()

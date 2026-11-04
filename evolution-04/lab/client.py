#!/usr/bin/env python3
"""Second client for Flights MCP Server - Python client script."""

import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    # Connect to the flights MCP server
    server_params = StdioServerParameters(
        command="python",
        args=["flights_mcp_server.py"],
        cwd="."  # Run from lab directory
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            print("=== Connected to Flights MCP Server ===")
            print(f"Client: python-client-script")
            
            # List available tools
            print("\n1. Listing tools...")
            tools_result = await session.list_tools()
            print(f"Available tools: {[tool.name for tool in tools_result.tools]}")
            
            # Call read tool - get_flights
            print("\n2. Calling read tool (get_flights)...")
            result = await session.call_tool("get_flights", arguments={"status": "all", "client_name": "python-client-script"})
            print(f"Result: {result.content}")
            
            # Call read tool - list_tools_info
            print("\n3. Calling read tool (list_tools_info)...")
            result = await session.call_tool("list_tools_info", arguments={"client_name": "python-client-script"})
            print(f"Result: {result.content}")
            
            # Call write tool - add_flight
            print("\n4. Calling write tool (add_flight)...")
            result = await session.call_tool("add_flight", arguments={
                "destination": "Seattle", 
                "status": "on-time",
                "client_name": "python-client-script"
            })
            print(f"Result: {result.content}")
            
            print("\n=== All calls completed ===")


if __name__ == "__main__":
    asyncio.run(main())

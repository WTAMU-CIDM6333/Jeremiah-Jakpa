# E4 design analysis — MCP server and two clients

Date: 2026-11-04. System: Flights MCP Server.

## Why (paragraph)

E4 required building a Python MCP server with read and write tools, connecting it to OpenCode with write tool set to ask, and connecting a second client. Both clients needed to list and call the same tools with server logging every call. This established the baseline for E5 hardening.

## Nine components

| Component | Consideration | E4 implementation |
|---|---|---|
| Foundation | MCP protocol for tool access | Python MCP SDK (mcp<2), FastMCP-based server |
| Perception | Client-server communication | STDIO transport, both clients connect to same server |
| Planning and reasoning | Tool selection by clients | Tools exposed via list_tools, clients choose which to call |
| Tools and orchestration | Read and write operations | get_flights/list_tools_info (read), add_flight (write) |
| Memory and context | Call tracking | Server logs every call |
| Coordination | Two different clients | OpenCode client and Python script client both connect |
| Evaluation and feedback | Verification of both clients work | Both tested successfully listing and calling tools |
| Governance and human interface | Write tool permissions | OpenCode configured with mcp and write tool set to ask |
| Runtime and operations | Logging and evidence | Server logs every call with client info; lab committed under evolution-04/lab/ |

## Judgment loop

**Decision:** Use MCP SDK with FastMCP, support both OpenCode and Python client, configure write tool as ask in OpenCode.

**Privileged characteristics:** Standardized protocol, both clients can use same tools, audit trail via logging.

**Cost:** Requires MCP SDK setup, client configuration complexity.

**Failure mode:** Clients may not connect properly, permissions not configured correctly.

**Preservation:** Tested both clients, verified logging, committed lab materials, configured opencode.json correctly.

**Feedback:** Server logs confirm both clients called tools.

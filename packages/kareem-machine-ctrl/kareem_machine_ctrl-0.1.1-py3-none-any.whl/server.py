#!/usr/bin/env python
"""
Sample MCP integration using FastMCP.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def open_app(app: str) -> str:
    """Tool to open an application."""
    # Replace with actual logic (e.g. using subprocess) if needed.
    return f"Opening {app}..."

if __name__ == '__main__':
    mcp.run()

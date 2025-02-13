#!/usr/bin/env python
"""
MCP server with comprehensive tool management and monitoring.
"""

import asyncio
import logging
import os
import sys
from dataclasses import dataclass
from functools import wraps
from pathlib import Path
from typing import Any, Callable

import click
from mcp.server.fastmcp import FastMCP
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.responses import JSONResponse
import uvicorn
from starlette.requests import Request
from starlette.exceptions import HTTPException

from kareem_machine_ctrl.config import get_settings
from kareem_machine_ctrl.monitoring import ToolMetrics

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('mcp_server.log')
    ]
)
logger = logging.getLogger(__name__)

# Initialize settings
settings = get_settings()
logger.info("Loaded settings: %s", settings.model_dump())

# Initialize MCP server with dependencies
mcp = FastMCP(
    name=settings.MCP_SERVER_NAME,
    dependencies=[
        "pydantic",
        "psutil",
        "pyautogui",
        "python-dotenv",
        "starlette",
        "uvicorn"
    ],
)

# Initialize tool registry if not already initialized
if not hasattr(mcp, 'tool_registry'):
    mcp.tool_registry = {}

# Profile directory for persistent storage
PROFILE_DIR = (
    Path.home() / ".fastmcp" / os.environ.get("USER", "anon") / settings.MCP_SERVER_NAME
).resolve()
PROFILE_DIR.mkdir(parents=True, exist_ok=True)

@dataclass
class ToolContext:
    """Context for tool execution with dependencies and state."""
    profile_dir: Path
    settings: Any

def with_tool_metrics(func: Callable) -> Callable:
    """Decorator to add metrics and error handling to tool functions."""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        metrics = ToolMetrics(func.__name__)
        try:
            with metrics.measure_execution():
                if asyncio.iscoroutinefunction(func):
                    return await func(*args, **kwargs)
                return func(*args, **kwargs)
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Tool %s failed: %s", func.__name__, str(exc), exc_info=True)
            raise
    return wrapper

async def initialize_server() -> None:
    """Initialize server resources and validate configuration."""
    try:
        # Initialize tool categories
        await initialize_tool_categories()
        
        # Log registered tools
        tool_list = list(mcp.tool_registry.keys()) if hasattr(mcp, 'tool_registry') else []
        logger.info("Registered tools: %s", tool_list)
        
        logger.info(
            "Server initialized successfully at %s:%s",
            settings.MCP_HOST,
            settings.MCP_PORT
        )
    except Exception as exc:  # pylint: disable=broad-except
        logger.error("Server initialization failed: %s", str(exc), exc_info=True)
        raise

async def initialize_tool_categories() -> None:
    """Initialize and register tool categories."""
    try:
        context = ToolContext(profile_dir=PROFILE_DIR, settings=settings)
        
        # Import and register tools from each category
        # pylint: disable=import-outside-toplevel
        from kareem_machine_ctrl.tools.app import register_app_tools
        from kareem_machine_ctrl.tools.browser import register_browser_tools
        from kareem_machine_ctrl.tools.shell import register_shell_tools
        from kareem_machine_ctrl.tools.system import register_system_tools
        
        # Register tools and wait for completion
        await asyncio.gather(
            register_app_tools(mcp, context),
            register_browser_tools(mcp, context),
            register_shell_tools(mcp, context),
            register_system_tools(mcp, context)
        )
        
        # Verify tools were registered
        if not mcp.tool_registry:
            raise RuntimeError("No tools were registered")
            
        logger.info("Tool categories initialized successfully")
        logger.info("Registered tools: %s", list(mcp.tool_registry.keys()))
    except Exception as exc:  # pylint: disable=broad-except
        logger.error("Failed to initialize tool categories: %s", str(exc), exc_info=True)
        raise

async def execute_tool(request: Request):
    """Execute a tool with the given parameters."""
    try:
        tool_name = request.path_params["tool_name"]
        if tool_name not in mcp.tool_registry:
            return JSONResponse(
                {"error": f"Tool {tool_name} not found"},
                status_code=404
            )
        
        # Get tool function
        tool_func = mcp.tool_registry[tool_name]
        
        # Parse request body
        params = await request.json()
        
        # Execute tool
        result = await tool_func(**params)
        
        return JSONResponse({"result": result})
    except Exception as exc:
        logger.error("Tool execution failed: %s", str(exc), exc_info=True)
        return JSONResponse(
            {"error": str(exc)},
            status_code=500
        )

@click.command()
@click.option(
    "--transport",
    type=click.Choice(["stdio", "sse"]),
    default="stdio",
    help="Transport type (stdio or SSE)"
)
@click.option(
    "--port",
    default=8000,
    help="Port to listen on for SSE transport"
)
def main(transport: str, port: int) -> None:
    """Main entry point for the MCP server."""
    try:
        logger.info("Starting %s in %s mode", settings.MCP_SERVER_NAME, settings.ENV)
        logger.info("Using transport: %s", transport)
        
        # Initialize server and tools
        asyncio.run(initialize_server())
        
        if transport == "sse":
            # Initialize SSE transport
            sse = SseServerTransport("/messages/")
            
            async def handle_sse(request: Request):
                """Handle SSE connection."""
                try:
                    async with sse.connect_sse(request.scope, request.receive, request.send) as streams:
                        async for event in streams:
                            await handle_event(event)
                except Exception as e:
                    logger.error(f"SSE connection error: {e}")
                    raise HTTPException(status_code=500, detail=str(e))
            
            async def list_tools(_request):
                """List available tools."""
                try:
                    tool_list = list(mcp.tool_registry.keys()) if hasattr(mcp, 'tool_registry') else []
                    return JSONResponse({
                        "tools": tool_list,
                        "count": len(tool_list)
                    })
                except Exception as exc:
                    logger.error("Failed to list tools: %s", str(exc))
                    return JSONResponse({"error": str(exc)}, status_code=500)
            
            # Create Starlette app
            app = Starlette(
                debug=settings.ENV == "development",
                routes=[
                    Route("/health", endpoint=lambda _: JSONResponse({"status": "ok"}), methods=["GET"]),
                    Route("/tools", endpoint=list_tools, methods=["GET"]),
                    Route("/tools/{tool_name}", endpoint=execute_tool, methods=["POST"]),
                    Route("/sse", endpoint=handle_sse),
                    Mount("/messages/", app=sse.handle_post_message),
                ],
            )
            
            # Run with uvicorn
            uvicorn.run(
                app,
                host=settings.MCP_HOST,
                port=port,
                log_level="info"
            )
        else:
            # Run with stdio transport
            asyncio.run(mcp.run())
        
    except Exception as exc:  # pylint: disable=broad-except
        logger.error("Failed to start server: %s", str(exc), exc_info=True)
        sys.exit(1)

if __name__ == '__main__':
    main()

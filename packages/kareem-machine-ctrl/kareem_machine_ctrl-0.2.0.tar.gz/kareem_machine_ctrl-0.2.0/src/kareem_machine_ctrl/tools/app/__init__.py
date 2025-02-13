"""
Application control tools for launching and managing desktop applications.
"""

import logging
import subprocess
from typing import Optional

from mcp.server.fastmcp import FastMCP
from pydantic import Field

from ...server import ToolContext, with_tool_metrics

logger = logging.getLogger(__name__)

async def register_app_tools(mcp: FastMCP, _: ToolContext) -> None:  # pylint: disable=unused-argument
    """Register application control tools with the MCP server."""
    
    # Initialize tool registry if not already initialized
    if not hasattr(mcp, 'tool_registry'):
        mcp.tool_registry = {}
    
    @mcp.tool()
    @with_tool_metrics
    async def open_app(
        app_name: str = Field(description="Name of the application to open"),
        wait: bool = Field(default=False, description="Whether to wait for the app to start")
    ) -> str:
        """Open a desktop application."""
        try:
            logger.info("Opening application: %s", app_name)
            
            # Use 'open' command on macOS
            cmd = ["open"]
            if wait:
                cmd.append("-W")
            cmd.extend(["-a", app_name])
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            if wait:
                _, stderr = process.communicate()
                if process.returncode != 0:
                    error = stderr.decode().strip()
                    raise RuntimeError(f"Failed to open {app_name}: {error}")
                
            return f"Successfully opened {app_name}"
            
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Failed to open %s: %s", app_name, str(exc))
            raise
    
    # Register the tool in the registry
    mcp.tool_registry['open_app'] = open_app
    
    @mcp.tool()
    @with_tool_metrics
    async def close_app(
        app_name: str = Field(description="Name of the application to close"),
        force: bool = Field(default=False, description="Force quit the application")
    ) -> str:
        """Close a desktop application."""
        try:
            logger.info("Closing application: %s", app_name)
            
            cmd = ["osascript", "-e", f'tell application "{app_name}" to quit']
            if force:
                cmd = ["pkill", "-f", app_name]
            
            process = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            return f"Successfully closed {app_name}"
            
        except subprocess.CalledProcessError as exc:
            logger.error("Failed to close %s: %s", app_name, exc.stderr)
            raise RuntimeError(f"Failed to close {app_name}: {exc.stderr}")
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Failed to close %s: %s", app_name, str(exc))
            raise
    
    # Register the tool in the registry
    mcp.tool_registry['close_app'] = close_app
    
    @mcp.tool()
    @with_tool_metrics
    async def list_running_apps() -> list[str]:
        """List all currently running applications."""
        try:
            logger.info("Listing running applications")
            
            cmd = ["ps", "-A", "-o", "comm="]
            process = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            # Filter and clean up the output
            apps = sorted(set(
                line.strip().split('/')[-1]
                for line in process.stdout.splitlines()
                if line.strip() and not line.startswith('_')
            ))
            
            return apps
            
        except subprocess.CalledProcessError as exc:
            logger.error("Failed to list apps: %s", exc.stderr)
            raise RuntimeError(f"Failed to list apps: {exc.stderr}")
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Failed to list running apps: %s", str(exc))
            raise
    
    # Register the tool in the registry
    mcp.tool_registry['list_running_apps'] = list_running_apps
    
    logger.info("Registered app tools successfully: %s", list(mcp.tool_registry.keys()))

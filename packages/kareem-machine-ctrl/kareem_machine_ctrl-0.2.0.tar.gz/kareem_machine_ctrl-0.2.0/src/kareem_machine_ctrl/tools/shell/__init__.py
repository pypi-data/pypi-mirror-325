"""
Shell tools for executing and managing terminal commands.
"""

import asyncio
import logging
import os
import shlex
import subprocess
from pathlib import Path
from typing import Optional, List

from mcp.server.fastmcp import FastMCP
from pydantic import Field

from ...server import ToolContext, with_tool_metrics

logger = logging.getLogger(__name__)

async def register_shell_tools(mcp: FastMCP, _: ToolContext) -> None:  # pylint: disable=unused-argument
    """Register shell command tools with the MCP server."""
    
    # Initialize tool registry if not already initialized
    if not hasattr(mcp, 'tool_registry'):
        mcp.tool_registry = {}
    
    @mcp.tool()
    @with_tool_metrics
    async def execute_command(
        command: str = Field(description="Shell command to execute"),
        working_dir: Optional[str] = Field(
            default=None,
            description="Working directory for command execution"
        ),
        timeout: Optional[int] = Field(
            default=None,
            description="Command timeout in seconds"
        )
    ) -> dict:
        """Execute a shell command and return its output."""
        try:
            logger.info("Executing command: %s", command)
            
            # Prepare working directory
            cwd = os.path.expanduser(working_dir) if working_dir else None
            if cwd:
                if not os.path.exists(cwd):
                    raise ValueError(f"Working directory does not exist: {cwd}")
                logger.info("Using working directory: %s", cwd)
            
            # Execute command
            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=cwd
            )
            
            try:
                stdout, stderr = await asyncio.wait_for(
                    process.communicate(),
                    timeout=timeout
                )
            except asyncio.TimeoutError as exc:
                process.kill()
                raise TimeoutError(f"Command timed out after {timeout} seconds") from exc
            
            return {
                "returncode": process.returncode,
                "stdout": stdout.decode().strip(),
                "stderr": stderr.decode().strip()
            }
            
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Command execution failed: %s", str(exc))
            raise
    
    # Register the tool in the registry
    mcp.tool_registry['execute_command'] = execute_command
    
    @mcp.tool()
    @with_tool_metrics
    async def list_directory(
        path: str = Field(default=".", description="Directory path to list"),
        pattern: Optional[str] = Field(
            default=None,
            description="Glob pattern to filter files"
        )
    ) -> List[dict]:
        """List contents of a directory with optional pattern filtering."""
        try:
            logger.info("Listing directory: %s", path)
            
            # Expand and validate path
            full_path = os.path.expanduser(path)
            if not os.path.exists(full_path):
                raise ValueError(f"Path does not exist: {full_path}")
            
            # List directory contents
            path_obj = Path(full_path)
            if pattern:
                items = list(path_obj.glob(pattern))
            else:
                items = list(path_obj.iterdir())
            
            # Build result list
            result = []
            for item in sorted(items):
                stat = item.stat()
                result.append({
                    "name": item.name,
                    "path": str(item),
                    "type": "directory" if item.is_dir() else "file",
                    "size": stat.st_size,
                    "modified": stat.st_mtime
                })
            
            return result
            
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Directory listing failed: %s", str(exc))
            raise
    
    # Register the tool in the registry
    mcp.tool_registry['list_directory'] = list_directory
    
    @mcp.tool()
    @with_tool_metrics
    async def find_files(
        root_dir: str = Field(default=".", description="Root directory to search in"),
        name_pattern: Optional[str] = Field(
            default=None,
            description="Pattern to match file names"
        ),
        content_pattern: Optional[str] = Field(
            default=None,
            description="Pattern to match file contents"
        ),
        max_depth: Optional[int] = Field(
            default=None,
            description="Maximum directory depth to search"
        )
    ) -> List[str]:
        """Find files matching name and/or content patterns."""
        try:
            logger.info("Searching for files in: %s", root_dir)
            
            # Build find command
            cmd = ["find", os.path.expanduser(root_dir)]
            
            if max_depth is not None:
                cmd.extend(["-maxdepth", str(max_depth)])
            
            if name_pattern:
                cmd.extend(["-name", name_pattern])
            
            # Execute find command
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await process.communicate()
            if process.returncode != 0:
                raise RuntimeError(f"Find command failed: {stderr.decode()}")
            
            files = stdout.decode().splitlines()
            
            # Filter by content if specified
            if content_pattern:
                matching_files = []
                for file in files:
                    if os.path.isfile(file):
                        try:
                            grep_cmd = ["grep", "-l", content_pattern, file]
                            result = subprocess.run(
                                grep_cmd,
                                capture_output=True,
                                text=True,
                                check=True
                            )
                            matching_files.append(file)
                        except subprocess.CalledProcessError:
                            continue
                        except Exception as exc:  # pylint: disable=broad-except
                            logger.warning("Failed to search content in %s: %s", file, str(exc))
                files = matching_files
            
            return sorted(files)
            
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("File search failed: %s", str(exc))
            raise
    
    # Register the tool in the registry
    mcp.tool_registry['find_files'] = find_files
    
    logger.info("Registered shell tools successfully: %s", list(mcp.tool_registry.keys()))

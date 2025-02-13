"""
System tools for monitoring and managing system resources.
"""

import logging
import os
import platform
from datetime import datetime
from typing import Dict, List, Optional

import psutil
from mcp.server.fastmcp import FastMCP
from pydantic import Field

from ...server import ToolContext, with_tool_metrics

logger = logging.getLogger(__name__)

async def register_system_tools(mcp: FastMCP, _: ToolContext) -> None:  # pylint: disable=unused-argument
    """Register system monitoring and management tools with the MCP server."""
    
    # Initialize tool registry if not already initialized
    if not hasattr(mcp, 'tool_registry'):
        mcp.tool_registry = {}
    
    @mcp.tool()
    @with_tool_metrics
    async def get_system_info() -> Dict:
        """Get detailed system information."""
        try:
            logger.info("Gathering system information")
            
            # Get CPU information
            cpu_info = {
                "physical_cores": psutil.cpu_count(logical=False),
                "total_cores": psutil.cpu_count(logical=True),
                "cpu_freq": psutil.cpu_freq()._asdict() if psutil.cpu_freq() else None,
                "cpu_percent": psutil.cpu_percent(interval=1, percpu=True)
            }
            
            # Get memory information
            memory = psutil.virtual_memory()
            memory_info = {
                "total": memory.total,
                "available": memory.available,
                "percent_used": memory.percent,
                "used": memory.used,
                "free": memory.free
            }
            
            # Get disk information
            disk = psutil.disk_usage('/')
            disk_info = {
                "total": disk.total,
                "used": disk.used,
                "free": disk.free,
                "percent_used": disk.percent
            }
            
            # Get system information
            system_info = {
                "system": platform.system(),
                "release": platform.release(),
                "version": platform.version(),
                "machine": platform.machine(),
                "processor": platform.processor(),
                "boot_time": datetime.fromtimestamp(psutil.boot_time()).isoformat()
            }
            
            return {
                "cpu": cpu_info,
                "memory": memory_info,
                "disk": disk_info,
                "system": system_info
            }
            
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Failed to get system info: %s", str(exc))
            raise
    
    # Register the tool in the registry
    mcp.tool_registry['get_system_info'] = get_system_info
    
    @mcp.tool()
    @with_tool_metrics
    async def get_process_info(
        pid: Optional[int] = Field(
            default=None,
            description="Process ID to get info for. If None, returns all processes."
        )
    ) -> List[Dict]:
        """Get information about running processes."""
        try:
            logger.info("Getting process info for PID: %s", pid if pid else 'all')
            
            def get_proc_info(proc):
                try:
                    with proc.oneshot():
                        return {
                            "pid": proc.pid,
                            "name": proc.name(),
                            "status": proc.status(),
                            "cpu_percent": proc.cpu_percent(),
                            "memory_percent": proc.memory_percent(),
                            "create_time": datetime.fromtimestamp(proc.create_time()).isoformat(),
                            "cmdline": " ".join(proc.cmdline()) if proc.cmdline() else None,
                            "username": proc.username()
                        }
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    return None
            
            if pid:
                try:
                    proc = psutil.Process(pid)
                    info = get_proc_info(proc)
                    return [info] if info else []
                except psutil.NoSuchProcess:
                    return []
            
            processes = []
            for proc in psutil.process_iter():
                info = get_proc_info(proc)
                if info:
                    processes.append(info)
            
            return sorted(processes, key=lambda x: x["cpu_percent"], reverse=True)
            
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Failed to get process info: %s", str(exc))
            raise
    
    # Register the tool in the registry
    mcp.tool_registry['get_process_info'] = get_process_info
    
    @mcp.tool()
    @with_tool_metrics
    async def get_network_info() -> Dict:
        """Get network interfaces and connections information."""
        logger.info("Getting network information")
        
        # Initialize result with default values
        result = {
            "interfaces": {},
            "stats": {
                "bytes_sent": 0,
                "bytes_recv": 0,
                "packets_sent": 0,
                "packets_recv": 0
            },
            "interface_stats": {}
        }
        
        try:
            # Get network interfaces (doesn't require elevated privileges)
            try:
                interfaces = {}
                for name, addrs in psutil.net_if_addrs().items():
                    interfaces[name] = []
                    for addr in addrs:
                        addr_dict = {}
                        # Only include the most stable and commonly available fields
                        if hasattr(addr, 'address'):
                            addr_dict['address'] = addr.address
                        if hasattr(addr, 'family'):
                            addr_dict['family'] = str(addr.family)
                        if addr_dict:  # Only append if we have any data
                            interfaces[name].append(addr_dict)
                if interfaces:
                    result['interfaces'] = interfaces
            except (psutil.AccessDenied, PermissionError) as e:
                logger.warning("Permission denied accessing network interfaces: %s", str(e))
            except Exception as e:
                logger.warning("Error getting network interfaces: %s", str(e))
            
            # Get basic network IO statistics (doesn't require elevated privileges)
            try:
                net_io = psutil.net_io_counters(pernic=False)
                if net_io:
                    result['stats'].update({
                        "bytes_sent": getattr(net_io, 'bytes_sent', 0),
                        "bytes_recv": getattr(net_io, 'bytes_recv', 0),
                        "packets_sent": getattr(net_io, 'packets_sent', 0),
                        "packets_recv": getattr(net_io, 'packets_recv', 0)
                    })
            except (psutil.AccessDenied, PermissionError) as e:
                logger.warning("Permission denied accessing network IO stats: %s", str(e))
            except Exception as e:
                logger.warning("Error getting network IO stats: %s", str(e))
            
            # Get basic interface status (doesn't require elevated privileges)
            try:
                if_stats = {}
                for name, stats in psutil.net_if_stats().items():
                    if_stats[name] = {
                        "isup": bool(getattr(stats, 'isup', False)),
                        "speed": getattr(stats, 'speed', 0),
                        "mtu": getattr(stats, 'mtu', 0)
                    }
                if if_stats:
                    result['interface_stats'] = if_stats
            except (psutil.AccessDenied, PermissionError) as e:
                logger.warning("Permission denied accessing interface stats: %s", str(e))
            except Exception as e:
                logger.warning("Error getting interface stats: %s", str(e))
            
            return result
            
        except Exception as e:
            logger.error("Unexpected error in get_network_info: %s", str(e))
            # Return the default result structure even in case of complete failure
            return result
    
    # Register the tool in the registry
    mcp.tool_registry['get_network_info'] = get_network_info
    
    logger.info("Registered system tools successfully: %s", list(mcp.tool_registry.keys()))

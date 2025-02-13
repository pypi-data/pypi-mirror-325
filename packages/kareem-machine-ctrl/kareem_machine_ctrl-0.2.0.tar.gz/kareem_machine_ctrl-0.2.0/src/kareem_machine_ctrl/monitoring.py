"""Monitoring and observability module for the MCP server."""

import time
import logging
from contextlib import contextmanager
from typing import Generator, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ToolMetrics:  # pylint: disable=too-few-public-methods
    """Tool execution metrics and monitoring."""
    
    def __init__(self, tool_name: str):
        self.tool_name = tool_name
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
    
    @contextmanager
    def measure_execution(self) -> Generator[None, None, None]:
        """Measure tool execution time and log metrics."""
        self.start_time = time.time()
        try:
            yield
            self.end_time = time.time()
            duration = self.end_time - self.start_time
            logger.info("Tool %s executed successfully in %.2fs", self.tool_name, duration)
            
        except Exception as e:
            self.end_time = time.time()
            duration = self.end_time - self.start_time
            logger.error("Tool %s failed after %.2fs: %s", self.tool_name, duration, str(e))
            raise 
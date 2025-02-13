import pytest
import subprocess
import time
import requests
import json
import sys
from typing import Generator
import logging
import statistics
from datetime import datetime
from pathlib import Path
import os
from test_utils import TestMetrics  # Import from test_utils directly

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('e2e_tests.log'),  # File handler for detailed logs
        logging.StreamHandler(sys.stdout)  # Console handler for important messages
    ]
)

# Set more restrictive log levels for noisy libraries
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('asyncio').setLevel(logging.WARNING)
logging.getLogger('aiohttp').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Constants
MCP_SERVER_URL = "http://localhost:8000"
STARTUP_WAIT_TIME = 2  # reduced initial wait time
MAX_STARTUP_RETRIES = 10  # increased number of retries
RETRY_INTERVAL = 1  # reduced retry interval
TOOL_TIMEOUT = 10  # seconds to wait for tool response
SERVER_LOG_FILE = "mcp_server.log"

def verify_server_health() -> bool:
    """Verify server health by checking key endpoints."""
    try:
        # Check health endpoint
        health_response = requests.get(f"{MCP_SERVER_URL}/health", timeout=5)
        if health_response.status_code != 200:
            logger.error("Health check failed with status %d", health_response.status_code)
            return False
            
        # Check SSE endpoint exists
        sse_response = requests.get(f"{MCP_SERVER_URL}/sse", timeout=5)
        if sse_response.status_code == 404:
            logger.error("SSE endpoint not found")
            return False
            
        # Check if server has registered tools
        tools_response = requests.get(f"{MCP_SERVER_URL}/tools", timeout=5)
        if tools_response.status_code != 200:
            logger.error("Tools endpoint check failed with status %d", tools_response.status_code)
            return False
            
        return True
    except requests.RequestException as e:
        logger.error("Server health verification failed: %s", str(e))
        return False

def wait_for_server(url: str, max_retries: int = MAX_STARTUP_RETRIES) -> bool:
    """Wait for server to become available and verify its health."""
    for i in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                # Additional health verification
                if verify_server_health():
                    logger.info("Server is healthy and ready")
                    return True
                logger.warning("Server responded but health verification failed")
            
        except requests.RequestException:
            pass
            
        if i < max_retries - 1:
            time.sleep(RETRY_INTERVAL)
            
    logger.error("Server failed to start or verify health after %d attempts", max_retries)
    return False

def read_server_logs() -> str:
    """Read the server log file if it exists."""
    log_path = Path(SERVER_LOG_FILE)
    if log_path.exists():
        return log_path.read_text()
    return "No server logs found"

def cleanup_ports():
    """Kill any processes using the server ports."""
    try:
        import subprocess
        # Kill any processes using ports 8000 or 8001
        subprocess.run(
            ["lsof", "-ti", ":8000,8001"],
            check=False,
            capture_output=True
        ).stdout.decode().strip().split("\n")
        
        # Kill the processes
        subprocess.run(
            ["lsof", "-ti", ":8000,8001", "|", "xargs", "kill", "-9"],
            check=False,
            shell=True
        )
    except Exception as e:
        logger.warning("Failed to cleanup ports: %s", str(e))

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Setup test environment and cleanup."""
    cleanup_ports()
    yield
    cleanup_ports()

@pytest.fixture(scope="session")
def mcp_server() -> Generator[subprocess.Popen, None, None]:
    """Start the MCP server as a fixture."""
    logger.info("Starting MCP server...")
    
    # Start the server with output redirection
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    
    process = subprocess.Popen(
        ["python3", "-m", "kareem_machine_ctrl.server", "--transport", "sse", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        env=env
    )
    
    # Wait for initial startup
    logger.info("Waiting %d seconds for initial startup", STARTUP_WAIT_TIME)
    time.sleep(STARTUP_WAIT_TIME)
    
    # Check if server is running with retries
    if not wait_for_server(f"{MCP_SERVER_URL}/health"):
        # Get process output
        stdout, stderr = process.communicate(timeout=5)
        logger.error("Server failed to start. Server output:")
        logger.error("STDOUT:\n%s", stdout)
        logger.error("STDERR:\n%s", stderr)
        logger.error("Server logs:\n%s", read_server_logs())
        
        process.kill()
        pytest.fail("Failed to start MCP server after maximum retries")

    logger.info("MCP server started successfully")
    yield process
    
    try:
        # Cleanup
        logger.info("Shutting down MCP server...")
        process.terminate()  # Try graceful shutdown first
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            logger.warning("Server did not shut down gracefully, forcing...")
            process.kill()
            process.wait(timeout=5)
        
        # Log final server output
        stdout, stderr = process.communicate()
        if stdout:
            logger.info("Final server stdout:\n%s", stdout)
        if stderr:
            logger.info("Final server stderr:\n%s", stderr)
    except Exception as e:
        logger.error("Error during server cleanup: %s", str(e))
        # Ensure process is killed
        try:
            process.kill()
        except:
            pass

def test_mcp_server_tools(mcp_server):
    """Test MCP server functionality and tools."""
    metrics = TestMetrics()
    metrics.start()

    # First verify server is healthy
    assert verify_server_health(), "Server health check failed"

    # Test core system tools that should always be available
    tools_to_test = [
        {
            "name": "get_system_info",
            "params": {}
        },
        {
            "name": "get_process_info",
            "params": {"pid": os.getpid()}  # Test with current process
        },
        {
            "name": "get_network_info",
            "params": {}
        }
    ]

    for tool in tools_to_test:
        tool_name = tool["name"]
        params = tool["params"]
        
        try:
            # Measure response time
            start_time = time.time()
            
            response = requests.post(
                f"{MCP_SERVER_URL}/tools/{tool_name}",
                json=params,
                timeout=TOOL_TIMEOUT
            )
            
            end_time = time.time()
            response_time_ms = (end_time - start_time) * 1000
            metrics.add_response_time(response_time_ms)
            
            # Verify response
            assert response.status_code == 200, f"Tool {tool_name} failed with status {response.status_code}"
            response_data = response.json()
            assert isinstance(response_data, (dict, list)), f"Tool {tool_name} returned invalid data type"
            
            # Extract result from response wrapper
            if "result" in response_data:
                response_data = response_data["result"]
            
            # Tool-specific assertions
            if tool_name == "get_system_info":
                assert "cpu" in response_data, "System info missing CPU data"
                assert "memory" in response_data, "System info missing memory data"
            elif tool_name == "get_process_info":
                assert len(response_data) > 0, "Process info returned empty list"
                assert response_data[0]["pid"] > 0, "Invalid process ID returned"
            elif tool_name == "get_network_info":
                assert "interfaces" in response_data, "Network info missing interfaces data"
                assert "stats" in response_data, "Network info missing stats data"
            
            metrics.add_success()
            
        except Exception as e:
            error_msg = f"Tool {tool_name} failed: {str(e)}"
            logger.error(error_msg)
            metrics.add_failure(error_msg)
            raise  # Re-raise to fail the test

    metrics.end()
    summary = metrics.get_summary()
    
    # Log final summary
    logger.info("Test Summary: %s", json.dumps(summary, indent=2))
    
    # Assert performance criteria
    assert metrics.failures == 0, f"Test failed with {metrics.failures} failures"
    assert summary["average_response_time_ms"] < 1000, "Average response time exceeds 1 second"
    assert summary["max_response_time_ms"] < 2000, "Maximum response time exceeds 2 seconds"

if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 
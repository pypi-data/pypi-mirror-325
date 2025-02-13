import pytest
import os
import logging

# Configure logging for tests
def pytest_configure(config):
    """Configure pytest environment."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Setup test environment variables and configurations."""
    # Set test environment variables if needed
    os.environ["MCP_TEST_MODE"] = "true"
    
    yield
    
    # Cleanup after tests
    if "MCP_TEST_MODE" in os.environ:
        del os.environ["MCP_TEST_MODE"] 
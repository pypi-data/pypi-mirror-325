"""Configuration module for the MCP server."""

from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):  # pylint: disable=too-few-public-methods
    """Server configuration settings."""
    
    # Server Configuration
    MCP_SERVER_NAME: str = "Kareem-MCP"
    MCP_HOST: str = "localhost"
    MCP_PORT: int = 8000
    MCP_LOG_LEVEL: str = "INFO"
    
    # Tool Configuration
    TOOL_TIMEOUT: int = 30  # seconds
    MAX_RETRIES: int = 3
    RETRY_DELAY: int = 1  # seconds
    
    # Environment-specific settings
    ENV: str = "development"
    DEBUG: bool = False
    
    # Allow extra fields
    model_config = ConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="allow"
    )

@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings() 
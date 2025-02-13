"""
Browser control tools for managing web browser interactions.
"""

import logging
import subprocess
from typing import Optional
from urllib.parse import urlparse

from mcp.server.fastmcp import FastMCP
from pydantic import Field, HttpUrl

from ...server import ToolContext, with_tool_metrics

logger = logging.getLogger(__name__)

async def register_browser_tools(mcp: FastMCP, _: ToolContext) -> None:  # pylint: disable=unused-argument
    """Register browser control tools with the MCP server."""
    
    @mcp.tool()
    @with_tool_metrics
    async def open_url(
        url: HttpUrl = Field(description="URL to open in the browser"),
        browser: Optional[str] = Field(
            default=None,
            description="Specific browser to use (e.g., 'chrome', 'safari', 'firefox')"
        )
    ) -> str:
        """Open a URL in the default or specified web browser."""
        try:
            logger.info("Opening URL: %s in browser: %s", url, browser or 'default')
            
            cmd = ["open"]
            if browser:
                cmd.extend(["-a", browser])
            cmd.append(str(url))
            
            process = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            return f"Successfully opened {url} in {browser or 'default browser'}"
            
        except subprocess.CalledProcessError as exc:
            logger.error("Failed to open URL %s: %s", url, exc.stderr)
            raise RuntimeError(f"Failed to open URL: {exc.stderr}")
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Failed to open URL %s: %s", url, str(exc))
            raise
    
    @mcp.tool()
    @with_tool_metrics
    async def search_web(
        query: str = Field(description="Search query"),
        engine: str = Field(
            default="google",
            description="Search engine to use (google, bing, duckduckgo)"
        )
    ) -> str:
        """Search the web using a specified search engine."""
        try:
            logger.info("Searching web for: %s using %s", query, engine)
            
            search_urls = {
                "google": "https://www.google.com/search?q=",
                "bing": "https://www.bing.com/search?q=",
                "duckduckgo": "https://duckduckgo.com/?q="
            }
            
            if engine.lower() not in search_urls:
                raise ValueError(f"Unsupported search engine: {engine}")
            
            search_url = search_urls[engine.lower()] + query.replace(" ", "+")
            
            cmd = ["open", search_url]
            process = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            return f"Successfully searched for '{query}' using {engine}"
            
        except subprocess.CalledProcessError as exc:
            logger.error("Failed to perform search: %s", exc.stderr)
            raise RuntimeError(f"Failed to perform search: {exc.stderr}")
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("Failed to perform web search: %s", str(exc))
            raise
    
    @mcp.tool()
    @with_tool_metrics
    async def validate_url(
        url: str = Field(description="URL to validate")
    ) -> dict:
        """Validate and parse a URL, returning its components."""
        try:
            logger.info("Validating URL: %s", url)
            
            parsed = urlparse(url)
            
            if not all([parsed.scheme, parsed.netloc]):
                raise ValueError("Invalid URL: Missing scheme or network location")
            
            components = {
                "scheme": parsed.scheme,
                "netloc": parsed.netloc,
                "path": parsed.path,
                "params": parsed.params,
                "query": parsed.query,
                "fragment": parsed.fragment,
                "is_valid": True
            }
            
            return components
            
        except ValueError as exc:
            logger.error("URL validation failed: %s", str(exc))
            return {
                "is_valid": False,
                "error": str(exc)
            }
        except Exception as exc:  # pylint: disable=broad-except
            logger.error("URL validation failed: %s", str(exc))
            return {
                "is_valid": False,
                "error": str(exc)
            }
    
    logger.info("Registered browser tools successfully")

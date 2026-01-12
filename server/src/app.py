from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

from .constants import NWS_API_BASE, USER_AGENT
from src.tools.alert import get_alerts
from src.tools.forecast import get_forecast

# Initialize FastMCP server
mcp = FastMCP("weather")

mcp.add_tool(get_alerts)
mcp.add_tool(get_forecast)

__all__ = [
    "mcp",
]
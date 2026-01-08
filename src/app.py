from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

from .constants import NWS_API_BASE, USER_AGENT

# Initialize FastMCP server
mcp = FastMCP("weather")

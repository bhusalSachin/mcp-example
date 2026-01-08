from src.constants import USER_AGENT
from typing import Any
import httpx

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """
    Make a request to the NWS API with proper error handling.

    Args:
        url (str): The URL to make the request to.

    Returns:
        dict[str, Any] | None: The response from the NWS API, or None if the request failed.
    """
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

async def format_alert(feature: dict) -> str:
    """
    Format an alert feature into a readable string.

    Args:
        feature (dict): The alert feature to format.

    Returns:
        str: A formatted string containing the alert information.
    """
    props = feature["properties"]
    return f"""
        Event: {props.get("event", "Unknown")}
        Area: {props.get("areaDesc", "Unknown")}
        Severity: {props.get("severity", "Unknown")}
        Description: {props.get("description", "No description available")}
        Instructions: {props.get("instruction", "No specific instructions provided")}
    """

__all__ = [
    "make_nws_request",
    "format_alert",
]

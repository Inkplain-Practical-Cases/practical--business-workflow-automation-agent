"""Typed allowlisted MCP-style registry; not yet a network MCP server."""
from copy import deepcopy
TOOLS=[{"name":"read_request","input_schema":{"type":"object","properties":{"request_id":{"type":"string"}},"required":["request_id"]}},{"name":"list_approvals","input_schema":{"type":"object","properties":{}}}]

def discover_tools()->list[dict]:
    """Return isolated schema copies so clients cannot mutate the allowlist."""
    return deepcopy(TOOLS)

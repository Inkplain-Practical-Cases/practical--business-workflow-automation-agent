from app.features.workflows.providers.mcp_client import validate_tool_request,resolve_tool
import pytest

def test_tool_request_requires_approval():
    assert validate_tool_request("read_request",{"request_id":"r1"})["authorized"] is False
def test_unknown_tool_rejected():
    with pytest.raises(PermissionError):resolve_tool("delete_everything")

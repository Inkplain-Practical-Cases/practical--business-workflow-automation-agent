"""Approval-gated workflow executor; only read operations permitted in demo."""
from app.features.workflows.providers.mcp_client import validate_tool_request

def plan_approved_read(request_id:str,approver:str,approved:bool)->dict:
    """Prevent execution without an explicit approver/approval assertion."""
    if not approver or not approved:raise PermissionError("Approval required")
    item=validate_tool_request("read_request",{"request_id":request_id})
    return {"state":"ready_for_execution","approval_by":approver,"tool_request":item}

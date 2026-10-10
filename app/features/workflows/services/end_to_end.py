"""Explicitly authorized workflow path with audit result; local fixture only."""
from app.features.workflows.services.approval_orchestrator import plan_approved_read
from app.features.workflows.services.execution_policy import execute_allowed_read

def execute_request_read(request_id:str,reviewer:str,approved:bool,executor)->dict:
    """Do not run MCP tools without approval; use a replaceable service adapter."""
    plan=plan_approved_read(request_id,reviewer,approved)
    return execute_allowed_read(plan["tool_request"]["tool"],plan["tool_request"]["arguments"],bool(approved),executor)

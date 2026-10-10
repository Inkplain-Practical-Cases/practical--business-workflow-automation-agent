"""MCP-style client abstraction; local typed adapter for reproducible STEP-3 tests.
ICS provider, component be.mcp_client. Real MCP transport wiring remains pending.
"""
from app.features.workflows.providers.tool_registry import discover_tools

def resolve_tool(name:str)->dict:
    """Resolve only allowlisted tool contracts; never execute an unknown tool."""
    for tool in discover_tools():
        if tool["name"]==name:return tool
    raise PermissionError(f"Tool not allowed: {name}")

def validate_tool_request(name:str,arguments:dict)->dict:
    """Require schema-declared mandatory fields for a local client request."""
    tool=resolve_tool(name)
    required=tool["input_schema"].get("required",[])
    if not isinstance(arguments,dict) or any(not isinstance(arguments.get(k),str) or not arguments[k] for k in required):
        raise ValueError("Invalid tool arguments")
    return {"tool":name,"arguments":dict(arguments),"authorized":False}

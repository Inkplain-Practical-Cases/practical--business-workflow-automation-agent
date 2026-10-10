"""STEP-2 workflow service: allowlisted tool discovery only; no mutating execution."""
from app.features.workflows.providers.tool_registry import discover_tools

def service_workflow(value:str)->str:
    """Return available tool contracts; execution requires later authorization."""
    tools=discover_tools()
    return "Available tools: "+", ".join(t["name"] for t in tools)

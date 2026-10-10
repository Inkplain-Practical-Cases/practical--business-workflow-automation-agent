"""Bounded retry and authorization policy for local workflow actions."""

def execute_allowed_read(name:str,arguments:dict,authorized:bool,executor):
    """Fail closed unless the action is explicitly authorized and read-only."""
    if not authorized:raise PermissionError("Approved operation required")
    if name not in {"read_request","list_approvals"}:raise PermissionError("Unsupported action")
    return {"tool":name,"result":executor(name,arguments),"audit":{"authorized":True,"tool":name}}

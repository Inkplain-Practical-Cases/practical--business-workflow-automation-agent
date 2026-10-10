"""Handler: forward validated input to domain service.
ICS layer: handler
CRD component: be.handle_workflow
Called by: receive_workflow
Calls: service_workflow
Why: separates orchestration from HTTP.
Without: impossible to evolve business logic independently.
Step: added in STEP-1.
"""
from app.features.workflows.services.service_workflow import service_workflow
def handle_workflow(value: str) -> dict[str,str]:
    """Coordinate one input value and map a stable response contract."""
    return {"status": "accepted", "detail": service_workflow(value)}

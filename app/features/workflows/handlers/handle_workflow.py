"""Handler: forward validated workflow inputs to the domain and audit services.

Requests are recorded after successful service_workflow evaluation.
"""
from app.features.workflows.services.service_workflow import service_workflow
from app.features.workflows.services.service_record_workflow import service_record_workflow

def handle_workflow(value: str) -> dict[str, str]:
    """Coordinate validation, an allowlisted tool summary and durable audit."""
    detail = service_workflow(value)
    service_record_workflow(value, "accepted")
    return {"status": "accepted", "detail": detail}

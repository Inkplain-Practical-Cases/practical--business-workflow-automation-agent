"""Workflow persistence service; delegates one safe write to the SQLite provider."""
from app.features.workflows.providers.provider_record_workflow import provider_record_workflow

def service_record_workflow(value: str, status: str) -> str:
    """Keep the workflow acceptance event durable for later review."""
    return provider_record_workflow(value, status)

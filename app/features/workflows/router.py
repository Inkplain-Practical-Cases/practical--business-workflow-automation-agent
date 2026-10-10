"""HTTP door: validate typed request and delegate to handler.
ICS layer: door
CRD component: be.receive_workflow
Called by: REST clients
Calls: handle_workflow
Why: keeps HTTP and business rules separate.
Without: validation and orchestration become coupled.
Step: added in STEP-1.
"""
from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.features.workflows.handlers.handle_workflow import handle_workflow
router = APIRouter(prefix="/api", tags=["workflows"])
class WorkflowRequest(BaseModel):
    request_text: str = Field(min_length=3, max_length=2500)
class WorkflowResponse(BaseModel):
    status: str
    detail: str
@router.post("/workflows", response_model=WorkflowResponse)
def receive_workflow(request: WorkflowRequest) -> WorkflowResponse:
    # Every request is validated before the handler sees it.
    return WorkflowResponse(**handle_workflow(request.request_text))

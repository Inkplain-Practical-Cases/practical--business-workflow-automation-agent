from app.features.workflows.services.approval_orchestrator import plan_approved_read
import pytest

def test_requires_approval():
    with pytest.raises(PermissionError):plan_approved_read("r1","",False)
def test_plan_stays_nonexecuting():
    out=plan_approved_read("r1","manager",True)
    assert out["state"]=="ready_for_execution"
    assert out["tool_request"]["authorized"] is False

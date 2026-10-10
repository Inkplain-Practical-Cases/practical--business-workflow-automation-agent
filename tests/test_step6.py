from app.features.workflows.services.end_to_end import execute_request_read
import pytest

def test_approved_action_logged():
    r=execute_request_read("r1","manager",True,lambda tool,args:{"id":args["request_id"]})
    assert r["audit"]["authorized"]
def test_denied_fails_closed():
    with pytest.raises(PermissionError):execute_request_read("r1","",False,lambda tool,args:None)

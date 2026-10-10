from app.features.workflows.services.execution_policy import execute_allowed_read
import pytest
def test_denied_without_authorization():
    with pytest.raises(PermissionError):execute_allowed_read("read_request",{},False,lambda n,a:None)
def test_read_audited():
    out=execute_allowed_read("read_request",{"request_id":"r1"},True,lambda n,a:{"id":"r1"})
    assert out["audit"]["authorized"] is True

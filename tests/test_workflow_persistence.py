"""Verify SQLite workflow request and event relations from an actual provider write."""
import sqlite3
from app.features.workflows.providers.provider_record_workflow import provider_record_workflow

def test_workflow_event_relations(tmp_path):
    database = tmp_path / "workflows.sqlite3"
    identifier = provider_record_workflow("review this request", "accepted", str(database))
    with sqlite3.connect(database) as connection:
        request = connection.execute("SELECT request_sha256, status FROM workflow_requests WHERE id=?", (identifier,)).fetchone()
        event = connection.execute("SELECT event_type FROM workflow_events WHERE workflow_request_id=?", (identifier,)).fetchone()
        assert len(request[0]) == 64
        assert request[1] == "accepted"
        assert event == ("accepted",)

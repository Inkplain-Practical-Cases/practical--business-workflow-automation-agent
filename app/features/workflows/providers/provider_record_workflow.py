"""SQLite workflow write adapter; called by service_record_workflow for accepted requests.

Only a digest of request text is stored; raw user text never enters the database.
"""
import hashlib
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

def provider_record_workflow(request_text: str, status: str, db_path: str | None = None) -> str:
    """Persist one request and its initial audit event in a real relational store."""
    location = db_path or os.getenv("INKPLAIN_WORKFLOW_DB", "workflow_runs.sqlite3")
    Path(location).parent.mkdir(parents=True, exist_ok=True)
    request_id = uuid4().hex
    recorded_at = datetime.now(timezone.utc).isoformat()
    with sqlite3.connect(location) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("""CREATE TABLE IF NOT EXISTS workflow_requests (
            id TEXT PRIMARY KEY,
            request_sha256 TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )""")
        connection.execute("""CREATE TABLE IF NOT EXISTS workflow_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workflow_request_id TEXT NOT NULL REFERENCES workflow_requests(id),
            event_type TEXT NOT NULL,
            occurred_at TEXT NOT NULL
        )""")
        connection.execute("INSERT INTO workflow_requests (id, request_sha256, status, created_at) VALUES (?, ?, ?, ?)",
                           (request_id, hashlib.sha256(request_text.encode("utf-8")).hexdigest(), status, recorded_at))
        connection.execute("INSERT INTO workflow_events (workflow_request_id, event_type, occurred_at) VALUES (?, ?, ?)",
                           (request_id, "accepted", recorded_at))
    return request_id

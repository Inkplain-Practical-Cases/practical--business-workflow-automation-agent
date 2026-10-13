# STEP 6 of 6 — Integrate and harden workflows

Install dependencies, run `python -m pytest -q`, and start `uvicorn app.main:app`. The full cumulative implementation provides tested local domain behavior and deterministic fixtures. The teaching code does **not** imply production approval, live services or all external adapters are complete. Audit the README limitations before deployment.

## Database (Entity) Relations
STEP-6 adds SQLite workflow_requests and workflow_events with workflow_events.workflow_request_id referencing workflow_requests.id. Only SHA-256 of workflow text is stored. Set INKPLAIN_WORKFLOW_DB for the persistent database location. See STEP-6.erd and the STEP-6-ERD Simulator tab.

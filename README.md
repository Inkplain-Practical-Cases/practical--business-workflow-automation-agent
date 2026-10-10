# Business Workflow Automation Agent

Starter FDE six-step MCP-style workflow learning project. The local STEP-3 adapter intentionally **does not implement a live MCP network transport**. The reference code uses deterministic fake tool contracts, explicit approval and authorization boundaries. Do not use for production financial or sensitive workflows without additional security design.

## Study branches
- [STEP-1: Receive business workflow requests](https://github.com/Inkplain-Practical-Cases/practical--business-workflow-automation-agent/tree/step-01-receive-business-workflow-requests)
- [STEP-2: Implement typed MCP tool registry](https://github.com/Inkplain-Practical-Cases/practical--business-workflow-automation-agent/tree/step-02-implement-typed-mcp-tool-registry)
- [STEP-3: Connect MCP client to tool service](https://github.com/Inkplain-Practical-Cases/practical--business-workflow-automation-agent/tree/step-03-connect-mcp-client-to-tool-service)
- [STEP-4: Orchestrate approval gated operations](https://github.com/Inkplain-Practical-Cases/practical--business-workflow-automation-agent/tree/step-04-orchestrate-approval-gated-operations)
- [STEP-5: Handle retries authorization and audit](https://github.com/Inkplain-Practical-Cases/practical--business-workflow-automation-agent/tree/step-05-handle-retries-authorization-and-audit)
- [STEP-6: Verify workflow observability and CI](https://github.com/Inkplain-Practical-Cases/practical--business-workflow-automation-agent/tree/step-06-verify-workflow-observability-and-ci)

Run `python -m pip install -r requirements.txt` and `python -m pytest -q`; then start `uvicorn app.main:app` to inspect `/docs`. Every branch has STEP-N.crd and STEP-N.md; main has FINAL.crd. The Simulator .inkp and portal tutorials are added in subsequent stages.

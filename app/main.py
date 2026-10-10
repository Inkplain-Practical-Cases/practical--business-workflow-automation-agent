"""FastAPI composition root: register HTTP door only."""
from fastapi import FastAPI
from app.features.workflows.router import router
app = FastAPI(title="Workflow Starter Practical Case")
app.include_router(router)

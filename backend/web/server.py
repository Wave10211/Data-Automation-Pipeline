from fastapi import FastAPI
from backend.web.routers import health, ingest

def create_app():
    app = FastAPI(
        title="Data Automation Pipeline API",
        version="0.1"
    )

    # rutele API
    app.include_router(health.router, prefix="/health", tags=["health"])
    app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])

    return app

app = create_app()
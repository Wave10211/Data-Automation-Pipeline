from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.web.routers import health, ingest

def create_app():
    app = FastAPI(
        title="Data Automation Pipeline API",
        version="0.1"
    )

    # înregistrezi rutele API
    app.include_router(health.router, prefix="/health", tags=["health"])
    app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])

    # aici montezi frontend-ul static, în interiorul funcției create_app
    app.mount("/", StaticFiles(directory="frontend/web", html=True), name="static")

    return app

app = create_app()

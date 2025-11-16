from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def ingest_root():
    return {"message": "Ingest endpoint operational"}

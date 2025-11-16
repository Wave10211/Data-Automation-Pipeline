from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_status():
    return {"status": "OK"}

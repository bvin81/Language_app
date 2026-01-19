from fastapi import APIRouter

router = APIRouter(prefix="/lessons", tags=["lessons"])

@router.get("/")
def get_lessons():
    return [{"id": 1, "title": "Familia"}]

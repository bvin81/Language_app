from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from pydantic import BaseModel

router = APIRouter(prefix="/progress", tags=["progress"])

class ProgressCreate(BaseModel):
    user_id: str
    lesson_id: int
    score: int
    total: int

@router.post("/")
def save_progress(progress: ProgressCreate, db: Session = Depends(get_db)):
    """Játék eredmény mentése"""
    return crud.save_progress(
        db,
        progress.user_id,
        progress.lesson_id,
        progress.score,
        progress.total
    )

@router.get("/{user_id}")
def get_user_progress(user_id: str, db: Session = Depends(get_db)):
    """Felhasználó összes eredménye"""
    results = crud.get_user_progress(db, user_id)
    return [{
        "lesson_id": r.lesson_id,
        "score": r.score,
        "total": r.total,
        "percentage": round(r.score / r.total * 100, 1),
        "completed_at": r.completed_at.isoformat()
    } for r in results]
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from app.schemas.lesson import Lesson

router = APIRouter(prefix="/lessons", tags=["lessons"])

@router.get("/", response_model=list[Lesson])
def get_lessons(db: Session = Depends(get_db)):
    return crud.get_lessons(db)
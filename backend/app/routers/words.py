from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.word import Word
from app.schemas.word import Word as WordSchema

router = APIRouter(prefix="/lessons", tags=["Words"])

@router.get("/{lesson_id}/words", response_model=list[WordSchema])
def get_words(lesson_id: int, db: Session = Depends(get_db)):
    return db.query(Word).filter(Word.lesson_id == lesson_id).all()

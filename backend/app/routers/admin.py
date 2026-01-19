from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from app.schemas.lesson import LessonCreate, Lesson as LessonSchema
from app.schemas.word import WordBase
from pydantic import BaseModel

router = APIRouter(prefix="/admin", tags=["admin"])

class AdminCheck(BaseModel):
    user_id: str

def verify_admin(user_id: str, db: Session):
    """Admin jogosultság ellenőrzése"""
    user = crud.get_user(db, user_id)
    if not user or not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin jogosultság szükséges")
    return user

# Lesson műveletek
@router.post("/lessons", response_model=LessonSchema)
def create_lesson(lesson: LessonCreate, user_id: str, db: Session = Depends(get_db)):
    verify_admin(user_id, db)
    return crud.create_lesson_admin(db, lesson.dict())

@router.put("/lessons/{lesson_id}", response_model=LessonSchema)
def update_lesson(lesson_id: int, lesson: LessonCreate, user_id: str, db: Session = Depends(get_db)):
    verify_admin(user_id, db)
    return crud.update_lesson_admin(db, lesson_id, lesson.dict())

@router.delete("/lessons/{lesson_id}")
def delete_lesson(lesson_id: int, user_id: str, db: Session = Depends(get_db)):
    verify_admin(user_id, db)
    success = crud.delete_lesson_admin(db, lesson_id)
    if not success:
        raise HTTPException(status_code=404, detail="Lecke nem található")
    return {"message": "Lecke törölve"}

# Word műveletek
@router.post("/words")
def create_word(word: WordBase, lesson_id: int, user_id: str, db: Session = Depends(get_db)):
    verify_admin(user_id, db)
    word_data = word.dict()
    word_data["lesson_id"] = lesson_id
    return crud.create_word_admin(db, word_data)

@router.delete("/words/{word_id}")
def delete_word(word_id: int, user_id: str, db: Session = Depends(get_db)):
    verify_admin(user_id, db)
    success = crud.delete_word_admin(db, word_id)
    if not success:
        raise HTTPException(status_code=404, detail="Szó nem található")
    return {"message": "Szó törölve"}
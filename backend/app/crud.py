from sqlalchemy.orm import Session
from app.modells.lesson import Lesson
from app.models.word import Word
from app.models import User
from app.schemas.lesson import LessonCreate
from app.schemas.word import WordBase

# === LESSON CRUD ===

def get_lessons(db: Session, skip: int = 0, limit: int = 100):
    """Összes lecke lekérése"""
    return db.query(Lesson).order_by(Lesson.order).offset(skip).limit(limit).all()

def get_lesson(db: Session, lesson_id: int):
    """Egy lecke lekérése ID alapján"""
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()

def get_free_lessons(db: Session):
    """Ingyenes leckék (freemium)"""
    return db.query(Lesson).filter(Lesson.is_premium == False).order_by(Lesson.order).all()

def create_lesson(db: Session, lesson: LessonCreate):
    """Új lecke létrehozása"""
    db_lesson = Lesson(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

# === WORD CRUD ===

def get_words_by_lesson(db: Session, lesson_id: int):
    """Szavak lekérése lecke alapján"""
    return db.query(Word).filter(Word.lesson_id == lesson_id).all()

def create_word(db: Session, lesson_id: int, word: WordBase):
    """Új szó létrehozása"""
    db_word = Word(**word.dict(), lesson_id=lesson_id)
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word

# === USER CRUD ===

def get_user(db: Session, user_id: str):
    """Felhasználó lekérése"""
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, name: str, age: int = None, level: str = "beginner"):
    """Új felhasználó létrehozása"""
    db_user = User(name=name, age=age, level=level)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
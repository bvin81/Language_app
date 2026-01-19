from sqlalchemy.orm import Session
from app.models.lesson import Lesson
from app.models.word import Word
from app.models.user import User
from app.schemas.lesson import LessonCreate
from app.schemas.word import WordBase
from app.models.progress import Progress
import uuid

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
    return db.query(User).filter(User.id == uuid.UUID(user_id)).first()

def create_user(db: Session, name: str, age: int = None, level: str = "beginner"):
    """Új felhasználó létrehozása"""
    db_user = User(name=name, age=age, level=level)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_name(db: Session, name: str):
    """Felhasználó lekérése név alapján"""
    return db.query(User).filter(User.name == name).first()

def update_user_premium(db: Session, user_id: str, is_premium: bool):
    """Felhasználó prémium státusz frissítése"""
    user = db.query(User).filter(User.id == uuid.UUID(user_id)).first()
    if user:
        user.is_premium = is_premium
        db.commit()
        db.refresh(user)
    return user

def save_progress(db: Session, user_id: str, lesson_id: int, score: int, total: int):
    """Játék eredmény mentése"""
    progress = Progress(
        user_id=uuid.UUID(user_id),
        lesson_id=lesson_id,
        score=score,
        total=total
    )
    db.add(progress)
    db.commit()
    db.refresh(progress)
    return progress

def get_user_progress(db: Session, user_id: str):
    """Felhasználó összes eredménye"""
    return db.query(Progress).filter(
        Progress.user_id == uuid.UUID(user_id)
    ).order_by(Progress.completed_at.desc()).all()

def get_lesson_progress(db: Session, user_id: str, lesson_id: int):
    """Egy leckéhez tartozó eredmények"""
    return db.query(Progress).filter(
        Progress.user_id == uuid.UUID(user_id),
        Progress.lesson_id == lesson_id
    ).order_by(Progress.completed_at.desc()).all()

# Lesson admin műveletek
def create_lesson_admin(db: Session, lesson_data: dict):
    """Admin: új lecke létrehozása"""
    lesson = Lesson(**lesson_data)
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return lesson

def update_lesson_admin(db: Session, lesson_id: int, lesson_data: dict):
    """Admin: lecke frissítése"""
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if lesson:
        for key, value in lesson_data.items():
            setattr(lesson, key, value)
        db.commit()
        db.refresh(lesson)
    return lesson

def delete_lesson_admin(db: Session, lesson_id: int):
    """Admin: lecke törlése"""
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if lesson:
        db.delete(lesson)
        db.commit()
        return True
    return False

# Word admin műveletek
def create_word_admin(db: Session, word_data: dict):
    """Admin: új szó létrehozása"""
    word = Word(**word_data)
    db.add(word)
    db.commit()
    db.refresh(word)
    return word

def delete_word_admin(db: Session, word_id: int):
    """Admin: szó törlése"""
    word = db.query(Word).filter(Word.id == word_id).first()
    if word:
        db.delete(word)
        db.commit()
        return True
    return False
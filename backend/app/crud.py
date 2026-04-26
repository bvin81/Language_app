from sqlalchemy.orm import Session
from app.models.lesson import Lesson
from app.models.word import Word
from app.models.user import User
from app.models.grammar import GrammarExercise
from app.models.listening import ListeningExercise
from app.models.reading import ReadingExercise, ReadingQuestion
from app.schemas.lesson import LessonCreate
from app.schemas.word import WordBase
from app.schemas.grammar import GrammarExerciseCreate
from app.models.progress import Progress
import uuid

# === LESSON CRUD ===

def get_lessons(db: Session, skip: int = 0, limit: int = 100):
    """Összes lecke lekérése"""
    return db.query(Lesson).order_by(Lesson.order).offset(skip).limit(limit).all()

def get_lesson(db: Session, lesson_id: int):
    """Egy lecke lekérése ID alapján"""
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()

def get_lessons_by_grade(db: Session, grade: int):
    """Leckék lekérése osztály alapján"""
    return db.query(Lesson).filter(Lesson.grade == grade).order_by(Lesson.order).all()

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


# === GRAMMAR EXERCISE CRUD ===

def get_grammar_exercises_by_lesson(db: Session, lesson_id: int):
    """Nyelvtani gyakorlatok lekérése lecke alapján"""
    return db.query(GrammarExercise).filter(
        GrammarExercise.lesson_id == lesson_id
    ).order_by(GrammarExercise.difficulty).all()


def create_grammar_exercise(db: Session, exercise: GrammarExerciseCreate):
    """Új nyelvtani gyakorlat létrehozása"""
    db_exercise = GrammarExercise(**exercise.dict())
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise


def create_grammar_exercise_admin(db: Session, exercise_data: dict):
    """Admin: új nyelvtani gyakorlat létrehozása"""
    exercise = GrammarExercise(**exercise_data)
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise


def delete_grammar_exercise_admin(db: Session, exercise_id: int):
    """Admin: nyelvtani gyakorlat törlése"""
    exercise = db.query(GrammarExercise).filter(
        GrammarExercise.id == exercise_id
    ).first()
    if exercise:
        db.delete(exercise)
        db.commit()
        return True
    return False


# === LISTENING EXERCISE CRUD ===

def get_listening_exercises_by_lesson(db: Session, lesson_id: int):
    """Hallásértés gyakorlatok lekérése lecke alapján"""
    return db.query(ListeningExercise).filter(
        ListeningExercise.lesson_id == lesson_id
    ).order_by(ListeningExercise.difficulty).all()


def create_listening_exercise(db: Session, exercise_data: dict):
    """Új hallásértés gyakorlat létrehozása"""
    exercise = ListeningExercise(**exercise_data)
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise


def delete_listening_exercise_admin(db: Session, exercise_id: int):
    """Admin: hallásértés gyakorlat törlése"""
    exercise = db.query(ListeningExercise).filter(
        ListeningExercise.id == exercise_id
    ).first()
    if exercise:
        db.delete(exercise)
        db.commit()
        return True
    return False


# === READING EXERCISE CRUD ===

def get_reading_exercises_by_lesson(db: Session, lesson_id: int):
    """Szövegértés gyakorlatok lekérése lecke alapján"""
    return db.query(ReadingExercise).filter(
        ReadingExercise.lesson_id == lesson_id
    ).order_by(ReadingExercise.difficulty).all()


def get_reading_exercise(db: Session, reading_id: int):
    """Egy szövegértés gyakorlat lekérése"""
    return db.query(ReadingExercise).filter(
        ReadingExercise.id == reading_id
    ).first()


def create_reading_exercise(db: Session, exercise_data: dict):
    """Új szövegértés gyakorlat létrehozása"""
    exercise = ReadingExercise(**exercise_data)
    db.add(exercise)
    db.commit()
    db.refresh(exercise)
    return exercise


def create_reading_question(db: Session, question_data: dict):
    """Új szövegértés kérdés létrehozása"""
    question = ReadingQuestion(**question_data)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


def delete_reading_exercise_admin(db: Session, exercise_id: int):
    """Admin: szövegértés gyakorlat törlése"""
    exercise = db.query(ReadingExercise).filter(
        ReadingExercise.id == exercise_id
    ).first()
    if exercise:
        db.delete(exercise)
        db.commit()
        return True
    return False
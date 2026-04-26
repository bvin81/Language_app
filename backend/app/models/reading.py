from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class ReadingExercise(Base):
    """
    Szövegértés gyakorlatok modellje

    Egy hosszabb szöveg olvasása után kérdések megválaszolása.
    """
    __tablename__ = "reading_exercises"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)

    # A szöveg címe
    title = Column(String, nullable=False)

    # A szöveg tartalma (lehet több bekezdés)
    content = Column(Text, nullable=False)

    # Nehézségi szint: 1-3
    difficulty = Column(Integer, default=1)

    # Kapcsolat a leckével
    lesson = relationship("Lesson", backref="reading_exercises")


class ReadingQuestion(Base):
    """
    Szövegértés kérdések - egy szöveghez több kérdés tartozhat
    """
    __tablename__ = "reading_questions"

    id = Column(Integer, primary_key=True, index=True)
    reading_id = Column(Integer, ForeignKey("reading_exercises.id"), nullable=False)

    # Kérdés szövege
    question = Column(Text, nullable=False)

    # Helyes válasz
    correct_answer = Column(String, nullable=False)

    # Rossz válaszok (vesszővel elválasztva)
    wrong_answers = Column(String, nullable=False)

    # Kapcsolat a szöveghez
    reading = relationship("ReadingExercise", backref="questions")

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class ListeningExercise(Base):
    """
    Hallásértés gyakorlatok modellje

    Az audio fájlok URL-jét tároljuk (lehet külső CDN vagy helyi fájl).
    Minden gyakorlathoz tartozik egy kérdés és válaszlehetőségek.
    """
    __tablename__ = "listening_exercises"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)

    # Audio fájl URL-je (pl. /static/audio/lesson1_1.mp3 vagy külső URL)
    audio_url = Column(String, nullable=False)

    # Az audio szövege (transcript) - opcionális, segítségként megjeleníthető
    transcript = Column(Text, nullable=True)

    # Kérdés az audio meghallgatása után
    question = Column(Text, nullable=False)

    # Helyes válasz
    correct_answer = Column(String, nullable=False)

    # Rossz válaszok (vesszővel elválasztva)
    wrong_answers = Column(String, nullable=False)

    # Nehézségi szint: 1-3
    difficulty = Column(Integer, default=1)

    # Audio hossza másodpercben (opcionális, UI-hoz)
    duration_seconds = Column(Integer, nullable=True)

    # Kapcsolat a leckével
    lesson = relationship("Lesson", backref="listening_exercises")

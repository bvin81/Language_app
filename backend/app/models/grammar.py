from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class GrammarExercise(Base):
    """
    Nyelvtani gyakorlatok modellje

    Típusok:
    - fill_blank: Mondatkiegészítés (hiányzó szó beírása)
    - multiple_choice: Helyes forma kiválasztása
    - word_order: Szórend (szavak helyes sorrendbe rendezése)
    """
    __tablename__ = "grammar_exercises"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"), nullable=False)

    # Gyakorlat típusa: fill_blank, multiple_choice, word_order
    exercise_type = Column(String, nullable=False)

    # A kérdés/feladat szövege
    # fill_blank esetén: "A macska ___ az asztalon." (üres hely jelölése: ___)
    # multiple_choice esetén: "Melyik a helyes forma?"
    # word_order esetén: szavak vesszővel elválasztva
    question = Column(Text, nullable=False)

    # Helyes válasz
    correct_answer = Column(String, nullable=False)

    # Rossz válaszok (vesszővel elválasztva multiple_choice esetén)
    wrong_answers = Column(String, nullable=True)

    # Nyelvtani szabály magyarázata
    explanation = Column(Text, nullable=True)

    # Nehézségi szint: 1-3
    difficulty = Column(Integer, default=1)

    # Kapcsolat a leckével
    lesson = relationship("Lesson", backref="grammar_exercises")

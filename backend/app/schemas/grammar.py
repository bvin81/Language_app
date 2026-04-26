from pydantic import BaseModel
from typing import Optional, List


class GrammarExerciseBase(BaseModel):
    exercise_type: str  # fill_blank, multiple_choice, word_order
    question: str
    correct_answer: str
    wrong_answers: Optional[str] = None
    explanation: Optional[str] = None
    difficulty: int = 1


class GrammarExerciseCreate(GrammarExerciseBase):
    lesson_id: int


class GrammarExerciseResponse(GrammarExerciseBase):
    id: int
    lesson_id: int

    class Config:
        from_attributes = True


class GrammarGameQuestion(BaseModel):
    """Egy nyelvtani játék kérdés formátuma"""
    id: int
    exercise_type: str
    question: str
    options: List[str]  # Válaszlehetőségek (keverve)
    correct_answer: str
    explanation: Optional[str] = None
    difficulty: int


class GrammarGameResponse(BaseModel):
    """Nyelvtani játék válasz"""
    questions: List[GrammarGameQuestion]
    lesson_id: int

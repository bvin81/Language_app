from pydantic import BaseModel
from typing import Optional, List


class ListeningExerciseBase(BaseModel):
    audio_url: str
    transcript: Optional[str] = None
    question: str
    correct_answer: str
    wrong_answers: str
    difficulty: int = 1
    duration_seconds: Optional[int] = None


class ListeningExerciseCreate(ListeningExerciseBase):
    lesson_id: int


class ListeningExerciseResponse(ListeningExerciseBase):
    id: int
    lesson_id: int

    class Config:
        from_attributes = True


class ListeningGameQuestion(BaseModel):
    """Egy hallásértés játék kérdés formátuma"""
    id: int
    audio_url: str
    question: str
    options: List[str]
    correct_answer: str
    transcript: Optional[str] = None
    difficulty: int
    duration_seconds: Optional[int] = None


class ListeningGameResponse(BaseModel):
    """Hallásértés játék válasz"""
    questions: List[ListeningGameQuestion]
    lesson_id: int

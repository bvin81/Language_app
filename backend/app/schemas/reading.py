from pydantic import BaseModel
from typing import Optional, List


class ReadingQuestionBase(BaseModel):
    question: str
    correct_answer: str
    wrong_answers: str


class ReadingQuestionCreate(ReadingQuestionBase):
    reading_id: int


class ReadingQuestionResponse(ReadingQuestionBase):
    id: int
    reading_id: int

    class Config:
        from_attributes = True


class ReadingExerciseBase(BaseModel):
    title: str
    content: str
    difficulty: int = 1


class ReadingExerciseCreate(ReadingExerciseBase):
    lesson_id: int


class ReadingExerciseResponse(ReadingExerciseBase):
    id: int
    lesson_id: int
    questions: List[ReadingQuestionResponse] = []

    class Config:
        from_attributes = True


class ReadingGameQuestion(BaseModel):
    """Egy szövegértés játék kérdés"""
    id: int
    question: str
    options: List[str]
    correct_answer: str


class ReadingGameResponse(BaseModel):
    """Szövegértés játék válasz - szöveg + kérdések"""
    reading_id: int
    title: str
    content: str
    difficulty: int
    questions: List[ReadingGameQuestion]
    lesson_id: int

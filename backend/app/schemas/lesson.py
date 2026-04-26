from pydantic import BaseModel

class LessonBase(BaseModel):
    title: str
    description: str | None = None
    language: str
    level: str
    grade: int = 1
    order: int = 0

class LessonCreate(LessonBase):
    pass

class Lesson(LessonBase):
    id: int

    class Config:
        orm_mode = True
from pydantic import BaseModel

class LessonBase(BaseModel):
    title: str
    description: str | None = None
    language: str
    level: str
    is_premium: bool = False
    order: int = 0

class LessonCreate(LessonBase):
    pass

class Lesson(LessonBase):
    id: int

    class Config:
        orm_mode = True
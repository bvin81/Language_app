from pydantic import BaseModel

class WordBase(BaseModel):
    word: str
    translation: str
    example_sentence: str

class Word(WordBase):
    id: int
    lesson_id: int

    class Config:
        orm_mode = True

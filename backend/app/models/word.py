from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    word = Column(String, index=True)
    translation = Column(String)
    example_sentence = Column(String)

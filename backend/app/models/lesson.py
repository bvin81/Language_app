from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    language = Column(String, nullable=False)  # "romanian" vagy "english"
    level = Column(String, nullable=False)  # "beginner", "intermediate", "advanced"
    is_premium = Column(Boolean, default=False)  # Freemium model
    order = Column(Integer, default=0)  # Sorrend
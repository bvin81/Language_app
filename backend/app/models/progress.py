from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.database import Base


class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    score = Column(Integer)  # Elért pontszám
    total = Column(Integer)  # Összes kérdés
    completed_at = Column(DateTime, default=datetime.utcnow)
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False, unique=True)
    age = Column(Integer)
    level = Column(String, default="beginner")
    is_admin = Column(Boolean, default=False)
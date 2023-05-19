from sqlalchemy import Column, DateTime, Integer, String
from app.database.engine import Base


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, nullable=False, unique=True)
    question_text = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True))

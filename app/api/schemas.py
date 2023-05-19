from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class QuestionsNum(BaseModel):
    questions_num: int


class QuestionData(BaseModel):
    question_id: int
    question_text: str
    answer: str
    created_at: datetime

    class Config:
        orm_mode = True

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.dao import QuestionDAO
from app.api.action.question import collect_new_questions
from app.api.schemas import QuestionsNum, QuestionData
from app.database.engine import get_session

question_router = APIRouter()


@question_router.post("/")
async def get_questions_num(
    item: QuestionsNum,
    session: AsyncSession = Depends(get_session)
):

    last_added = await QuestionDAO.get_last(session)

    await collect_new_questions(item.questions_num, session)
    if last_added:
        return QuestionData(
            question_id=last_added.question_id,
            question_text=last_added.question_text,
            answer=last_added.answer,
            created_at=last_added.created_at
        )
    return []

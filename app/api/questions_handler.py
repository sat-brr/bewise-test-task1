from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.action.question_utils import collect_new_questions
from app.api.schemas import QuestionData, QuestionsNum
from app.database.dao import QuestionDAO
from app.database.engine import get_session

question_router = APIRouter()


@question_router.post("/")
async def add_new_questions(
    body: QuestionsNum,
    session: AsyncSession = Depends(get_session)
) -> QuestionData | list:

    last_added_question = await QuestionDAO.get_last(session)

    await collect_new_questions(body.questions_num, session)

    if last_added_question:
        return QuestionData.parse_obj(last_added_question.__dict__)
    else:
        return []

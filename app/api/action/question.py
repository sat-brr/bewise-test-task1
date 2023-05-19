from typing import List

import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import QuestionData
from app.database.dao import QuestionDAO
from app.database.db_models.question import Question

MAIN_URL = "https://jservice.io/api/random?count=1"


async def _get_new_questions() -> QuestionData:
    async with aiohttp.ClientSession() as session:
        response = await session.get(MAIN_URL)
        data = await response.json()
        data1 = data[0]
        return QuestionData(
            question_id=data1["id"],
            question_text=data1["question"],
            answer=data1["answer"],
            created_at=data1["created_at"]
        )


async def _add_question_in_db(
    questions_data: List[QuestionData],
    session: AsyncSession
) -> List[Question]:
    added = []
    for qst_data in questions_data:
        res = await QuestionDAO.create_question(session, **qst_data.dict())
        if res:
            added.append(res)
    return added


async def collect_new_questions(
    num: int, session: AsyncSession
) -> List[Question] | list:
    collected_question = []
    while num != 0:
        new_questions = [await _get_new_questions() for _ in range(num)]
        added_questions = await _add_question_in_db(new_questions, session)
        collected_question.extend(added_questions)
        num -= len(added_questions)
    return collected_question

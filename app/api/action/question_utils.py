import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import QuestionData
from app.database.dao import QuestionDAO

MAIN_URL = "https://jservice.io/api/random?count="


async def get_new_questions(questions_num: int) -> list[QuestionData]:
    async with aiohttp.ClientSession() as session:
        response = await session.get(f"{MAIN_URL}{questions_num}")
        response_data = await response.json()

        return [
            QuestionData(
                question_id=question["id"],
                question_text=question["question"],
                answer=question["answer"],
                created_at=question["created_at"],
            )
            for question in response_data
        ]


async def write_question_to_db(
    new_questions: list[QuestionData],
    session: AsyncSession
) -> int:

    cnt_created = 0
    for question in new_questions:
        created_question = await QuestionDAO.create_question(session,
                                                             **question.dict())
        if created_question:
            cnt_created += 1
    return cnt_created


async def collect_new_questions(
    questions_num: int, session: AsyncSession
) -> None:

    while questions_num != 0:
        new_questions = await get_new_questions(questions_num)
        cnt_created = await write_question_to_db(new_questions, session)
        questions_num -= cnt_created

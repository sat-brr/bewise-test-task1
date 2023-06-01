from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db_models.question import Question


class QuestionDAO:
    """Data Access Object"""

    @classmethod
    async def create_question(
        cls, session: AsyncSession, **kwargs
    ) -> Question | None:

        try:
            new_question = Question(**kwargs)
            session.add(new_question)
            await session.commit()
            return new_question
        except SQLAlchemyError:
            await session.rollback()

    @classmethod
    async def get_last(cls, session: AsyncSession) -> Question | None:
        query = select(Question).order_by(Question.id.desc())
        result = await session.execute(query)
        return result.scalars().first()

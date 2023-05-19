from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.engine import get_session

from app.database.db_models.question import Question


class QuestionDAO:
    """Data Access Object"""
    @classmethod
    async def create_question(cls, session: AsyncSession, **kwargs) -> Question | None:

        try:
            new_object = Question(**kwargs)
            session.add(new_object)
            await session.commit()
            return new_object
        except SQLAlchemyError:
            await session.rollback()

    @classmethod
    async def get_last(cls, session: AsyncSession) -> Question | None:
        query = select(Question).order_by(Question.id.desc())
        result = await session.execute(query)
        return result.scalars().first()

from sqlalchemy import select
from app.bookings.models import Booking
from app.database import async_session_maker


class BaseService:
    model = None

    @classmethod
    async def find_by_id(cls, *filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter(*filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()


    @classmethod
    async def find_one_or_none(cls, *filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter(*filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, *filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter(*filter_by)
            result = await session.execute(query)
            return result.mappings().all()
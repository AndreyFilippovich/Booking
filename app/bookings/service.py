from sqlalchemy import select
from app.bookings.models import Booking
from app.database import async_session_maker
from app.services.base import BaseService


class BookingService(BaseService):
    model = Booking

from app.hotels.models import Hotels
from app.services.base import BaseService


class HotelService(BaseService):
    model = Hotels

    @classmethod
    async def find_all():
        pass
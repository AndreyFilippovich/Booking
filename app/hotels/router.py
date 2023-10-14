from datetime import date, datetime, timedelta
from typing import List, Optional

from fastapi import APIRouter, Query
from fastapi_cache.decorator import cache

from app.hotels.service import HotelService
from app.hotels.schemas import SHotel, SHotelInfo

router = APIRouter(prefix="/hotels", tags=["Отели"])


'''Получение отелей в определённой локации на определённый срок'''
@router.get("/{location}")
async def get_hotels_by_location_and_time(
    location: str,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
) -> List[SHotelInfo]:
    hotels = await HotelService.find_all(location, date_from, date_to)
    return hotels


'''Получение отелей по id'''
@router.get("/id/{hotel_id}", include_in_schema=True)
async def get_hotel_by_id(
    hotel_id: int,
) -> Optional[SHotel]:
    return await HotelService.find_one_or_none(id=hotel_id)

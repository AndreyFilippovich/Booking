from fastapi import APIRouter, Depends, Request

from app.bookings.models import Booking
from app.bookings.schemas import SBooking

from app.bookings.service import BookingService
from app.users.dependecies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)): # -> list[SBooking]:
    return await BookingService.find_all(user_id=user.id)

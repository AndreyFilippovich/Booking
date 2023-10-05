from fastapi import APIRouter

from app.bookings.models import Booking
from app.bookings.schemas import SBooking

from app.bookings.service import BookingService

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingService.find_all()

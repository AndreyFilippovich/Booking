from datetime import date
from fastapi import APIRouter, BackgroundTasks, Depends
from pydantic import TypeAdapter

from app.bookings.schemas import SBooking, SNewBooking

from app.bookings.service import BookingService
from app.exceptions import RoomCannotBeBooked, RoomFullyBooked
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


'''Получение бонирований'''
@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await BookingService.find_all(user_id=user.id)


'''Добавление бронирований'''
@router.post("", status_code=201)
async def add_booking(
    booking: SNewBooking,
    background_tasks: BackgroundTasks,
    user: Users = Depends(get_current_user),
):
    booking = await BookingService.add(
        user.id,
        booking.room_id,
        booking.date_from,
        booking.date_to,
    )
    if not booking:
        raise RoomCannotBeBooked
    booking = TypeAdapter(SNewBooking).validate_python(booking).model_dump()
#    send_booking_confirmation_email.delay(booking, user.email)
    background_tasks.add_task(send_booking_confirmation_email, booking, user.email)
    return booking


@router.delete("/{booking_id}")
async def remove_booking(
    booking_id: int,
    current_user: Users = Depends(get_current_user),
):
    await BookingService.delete(id=booking_id, user_id=current_user.id)

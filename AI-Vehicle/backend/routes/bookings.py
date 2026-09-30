from fastapi import APIRouter, HTTPException

from schemas.booking import BookingCreate

from services.booking_service import (
    get_all_bookings,
    get_booking_by_id,
    create_booking,
    cancel_booking
)

router = APIRouter()


@router.get("/")
def get_bookings():
    return {
        "bookings": get_all_bookings()
    }


@router.post("/")
def add_booking(booking: BookingCreate):
    return create_booking(
        booking.model_dump()
    )


@router.get("/{booking_id}")
def get_booking(booking_id: int):
    booking = get_booking_by_id(booking_id)

    if booking is None:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking


@router.delete("/{booking_id}")
def delete_booking(booking_id: int):
    booking = cancel_booking(booking_id)
    if booking is None:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return {
        "message": "Booking cancelled successfully",
        "booking": booking
    }
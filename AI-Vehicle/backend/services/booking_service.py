from models.store import bookings


def get_all_bookings():
    return bookings


def get_booking_by_id(booking_id: int):
    for booking in bookings:
        if booking["id"] == booking_id:
            return booking

    return None


def create_booking(booking_data):
    new_booking = {
        "id": len(bookings) + 1,
        **booking_data,
        "status": "Confirmed"
    }

    bookings.append(new_booking)

    return new_booking


def cancel_booking(booking_id: int):
    booking = get_booking_by_id(booking_id)

    if booking is None:
        return None

    booking["status"] = "Cancelled"

    return booking
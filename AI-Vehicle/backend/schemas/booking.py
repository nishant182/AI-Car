from pydantic import BaseModel


class BookingCreate(BaseModel):
    vehicle_id: int
    service_center_id: int
    service_type: str
    booking_date: str
    booking_time: str


class BookingStatusUpdate(BaseModel):
    status: str
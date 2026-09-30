from pydantic import BaseModel


class VehicleCreate(BaseModel):
    brand: str
    model: str
    year: int
    registration_number: str
    fuel_type: str
    odometer_km: int


class VehicleUpdate(BaseModel):
    brand: str | None = None
    model: str | None = None
    year: int | None = None
    fuel_type: str | None = None
    odometer_km: int | None = None
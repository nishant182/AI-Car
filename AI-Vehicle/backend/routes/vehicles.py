from fastapi import APIRouter, HTTPException ,Header , Depends
from schemas.vehicle import VehicleCreate

from fastapi import Header
from services.security import verify_token
from services.auth_service import get_current_user
from services.vehicle_service import (
    get_all_vehicles,
    get_vehicle_by_id,
    add_vehicle
)

router = APIRouter()


@router.get("/")
def get_vehicles():
    return {
        "vehicles": get_all_vehicles()
    }

@router.get("/protected")
def protected_vehicle_api(
    email: str = Depends(get_current_user)
):
    return {
        "message": "Protected API accessed successfully",
        "email": email
    }


@router.get("/{vehicle_id}")
def get_vehicle(vehicle_id: int):
    vehicle = get_vehicle_by_id(vehicle_id)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return vehicle


@router.post("/")
def create_vehicle(vehicle: VehicleCreate):
    return add_vehicle(
        vehicle.model_dump()
    )
    
    

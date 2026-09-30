from fastapi import APIRouter
from services.history_service import get_service_history

router = APIRouter()


@router.get("/{vehicle_id}")
def service_history(vehicle_id: int):
    return {
        "vehicle_id": vehicle_id,
        "service_history": get_service_history(vehicle_id)
    }
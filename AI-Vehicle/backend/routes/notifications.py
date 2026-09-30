from fastapi import APIRouter
from services.notification_service import get_notifications

router = APIRouter()


@router.get("/{vehicle_id}")
def notifications(vehicle_id: int):
    return {
        "vehicle_id": vehicle_id,
        "notifications": get_notifications(vehicle_id)
    }
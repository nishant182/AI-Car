from fastapi import APIRouter, HTTPException

from services.service_center_service import (
    get_all_service_centers,
    get_service_center_by_id
)

router = APIRouter()


@router.get("/")
def get_service_centers():
    return {
        "service_centers": get_all_service_centers()
    }


@router.get("/{service_id}")
def get_service_center(service_id: int):

    service = get_service_center_by_id(service_id)

    if service is None:
        raise HTTPException(
            status_code=404,
            detail="Service center not found"
        )

    return service
from fastapi import APIRouter, HTTPException , UploadFile, File

from models.store import vehicles
from schemas.assistant import AssistantRequest

router = APIRouter()


@router.get("/vehicle-health/{vehicle_id}")
def vehicle_health(vehicle_id: int):

    vehicle = None

    for item in vehicles:
        if item["id"] == vehicle_id:
            vehicle = item
            break

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return {
        "vehicle_id": vehicle_id,
        "overall_health": vehicle.get("health_score", 82),
        "status": "Good",
        "components": {
            "engine": 90,
            "brakes": 75,
            "battery": 80,
            "tyres": 70,
            "oil": 85
        }
    }


@router.post("/problem-assistant")
def problem_assistant(request: AssistantRequest):

    return {
        "vehicle_id": request.vehicle_id,
        "problem": request.problem,
        "possible_causes": [
            "Battery issue",
            "Starter motor problem",
            "Fuel system issue"
        ],
        "recommendation": (
            "Please get your vehicle inspected by a professional."
        )
    }
    
    

@router.get("/maintenance/{vehicle_id}")
def maintenance_prediction(vehicle_id: int):

    vehicle = None

    for item in vehicles:
        if item["id"] == vehicle_id:
            vehicle = item
            break

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle not found"
        )

    return {
        "vehicle_id": vehicle_id,
        "maintenance": [
            {
                "item": "Engine Oil",
                "status": "Due Soon"
            },
            {
                "item": "Brake Inspection",
                "status": "Recommended"
            },
            {
                "item": "Tyre Inspection",
                "status": "Recommended"
            },
            {
                "item": "Battery Check",
                "status": "Good"
            }
        ]
    }    


@router.post("/damage-detection")
async def damage_detection(
    image: UploadFile = File(...)
):
    return {
        "filename": image.filename,
        "message": "Vehicle damage image uploaded successfully",
        "damage_detected": True,
        "damage_type": "Front Bumper Damage",
        "severity": "Medium"
    }   
    
@router.post("/cost-estimation")
def cost_estimation(
    service_type: str,
    vehicle_id: int
):
    cost_data = {
        "General Service": {
            "min_cost": 1500,
            "max_cost": 2500
        },
        "Brake Service": {
            "min_cost": 2000,
            "max_cost": 4000
        },
        "Engine Service": {
            "min_cost": 3000,
            "max_cost": 6000
        },
        "AC Service": {
            "min_cost": 1200,
            "max_cost": 3000
        }
    }

    estimate = cost_data.get(
        service_type,
        {
            "min_cost": 1000,
            "max_cost": 5000
        }
    )

    return {
        "vehicle_id": vehicle_id,
        "service_type": service_type,
        "estimated_cost": estimate,
        "currency": "INR"
    }     
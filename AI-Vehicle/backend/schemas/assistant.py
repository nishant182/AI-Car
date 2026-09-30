from pydantic import BaseModel


class AssistantRequest(BaseModel):
    vehicle_id: int
    problem: str
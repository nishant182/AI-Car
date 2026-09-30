import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_get_vehicles():
    response = client.get("/api/vehicles/")

    assert response.status_code == 200

    data = response.json()

    assert "vehicles" in data
    
    

def test_get_vehicle_by_id():
    response = client.get("/api/vehicles/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["brand"] == "Honda"    
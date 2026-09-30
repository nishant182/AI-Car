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


def test_get_bookings():
    response = client.get("/api/bookings/")

    assert response.status_code == 200

    data = response.json()

    assert "bookings" in data
    
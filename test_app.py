import pytest
from fastapi.testclient import TestClient
from main import app   # your FastAPI app


@pytest.fixture
def client():
    return TestClient(app)

def test_app_is_working(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

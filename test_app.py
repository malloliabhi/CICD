import pytest
from fastapi.testclient import TestClient
from app import app   # your FastAPI app
from fastapi import FastAPI

app=FastAPI()

@pytest.fixture
def client():
    return TestClient(app)

def test_app_is_working(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

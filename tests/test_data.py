from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_data_without_token():
    response = client.get("/data/")
    assert response.status_code ==401

def test_get_with_invalid_token():
    response = client.get("/data/", headers={"Authorization": "Bearer invalid"})
    assert response.status_code == 401

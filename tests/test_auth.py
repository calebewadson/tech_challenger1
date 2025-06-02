from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_token_sucess():
    response = client.post("/token", data={"username": "user", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_token_failure():
    response = client.post("/token", data={"username": "wrong", "password": "wrong"})
    assert response.status_code == 401
    
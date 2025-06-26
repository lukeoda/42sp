from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_put_success() -> None:
    body = '{"name": "LUCAS", "email": "lucas@email.com"}'
    response = client.put("/accounts", data=body)

    assert response.status_code == 201

def test_put_error_422() -> None:
    body = '{"name": "231231231","emaidasl": "string",}'
    response = client.put("/accounts", data=body)
    assert response.status_code == 422

def test_put_error_409() -> None:
    body = '{"id": 1,  "name": "string",  "email": "string"}'
    response = client.put("/accounts", data=body)
    assert response.status_code == 409

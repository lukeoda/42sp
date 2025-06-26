from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_success() -> None:
    response = client.get("/")

    data = response.json()
    assert data['message'] in 'Bem-vindo à minha API!'


def test_post_success() -> None:
    body = '{  "additionalProp1": "string",  "additionalProp2": "string",  "additionalProp3": "string"}'
    response = client.post("/", data=body)
    assert response.status_code == 201

def test_post_400() -> None:
    body = 'uma string'
    response = client.post("/", data=body)
    assert response.status_code == 400

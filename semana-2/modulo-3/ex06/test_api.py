from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_put_success() -> None:
    body = '{"name": "LUCAS", "email": "lucas@email.com"}'
    response = client.put("/accounts", data=body)

    assert response.status_code == 201
    
    client.delete(f'/accounts/{response.text}')

def test_put_error_422() -> None:
    body = '{"name": "231231231","emaidasl": "string",}'
    response = client.put("/accounts", data=body)
    assert response.status_code == 422

def test_put_error_409() -> None:
    body = '{"id": 1,  "name": "string",  "email": "string"}'
    response = client.put("/accounts", data=body)
    assert response.status_code == 409
    
def test_get_sucess() -> None:
    response = client.get("/accounts")
    data = response.json()
    assert len(data) > 1
    assert response.status_code == 200
    
def test_get_by_id_sucess() -> None:
    account_id = 1
    response = client.get(f"/accounts/{account_id}")
    assert response.status_code == 200

def test_get_by_id_error() -> None:
    account_id = 251231
    response = client.get(f"/accounts/{account_id}")
    assert response.status_code == 404
    
def test_post_operation_sucess() -> None:
    account_id = 1
    body = '{"operation": "+", "amount": 1110}'
    response = client.post(f"/accounts/{account_id}/operations", data=body)
    assert response.status_code == 201
    
def test_post_operation_not_found() -> None:
    account_id = 21231
    body = '{"operation": "+", "amount": 1110}'
    response = client.post(f"/accounts/{account_id}/operations", data=body)
    assert response.status_code == 404
    
def test_get_operation_sucess() -> None:
    account_id = 1
    response = client.get(f"/accounts/{account_id}/operations")
    data = response.json()
    assert len(data) > 0
    assert response.status_code == 200

def test_delete_success() -> None:
    body = '{"name": "LUCAS", "email": "lucas@email.com"}'
    resp_put = client.put("/accounts", data=body)
    response = client.delete(f'/accounts/{resp_put.text}')
    
    assert response.status_code == 204
    
def test_delete_404() -> None:
    account_id = 1123123
    response = client.delete(f'/accounts/{account_id}')
    
    assert response.status_code == 404
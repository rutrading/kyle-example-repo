from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_add_numbers_path():
    response = client.get("/math/add/5/3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_add_numbers_body():
    response = client.post("/math/add", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_divide_numbers():
    response = client.get("/math/divide/10/2")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_divide_by_zero():
    response = client.get("/math/divide/10/0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}

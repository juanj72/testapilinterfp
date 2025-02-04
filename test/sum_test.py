from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_sum():
    response = client.get("/sum?number1=5&number2=9")
    assert response.status_code == 200
    assert response.json() == {"result": 14}


def test_invalid_parameters():
    response = client.get("/sum?number1=5&number2=hello")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "input": "hello",
                "loc": ["query", "number2"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",
                "type": "int_parsing",
            }
        ]
    }


def test_without_parameters():
    response = client.get("/sum")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "input": None,
                "loc": ["query", "number1"],
                "msg": "Field required",
                "type": "missing",
            },
            {
                "input": None,
                "loc": ["query", "number2"],
                "msg": "Field required",
                "type": "missing",
            },
        ]
    }

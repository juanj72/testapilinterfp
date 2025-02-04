# test/test_app.py
from fastapi.testclient import TestClient
from app.main import app

# Crear un TestClient con la aplicación FastAPI
client = TestClient(app)

def test_concatenar():
    # Realizar una solicitud GET al endpoint /concat/{caracter1}/{caracter2}
    response = client.get("/concat/a/b")

    # Verificar que la respuesta sea exitosa (código de estado 200)
    assert response.status_code == 200

    # Verificar que el contenido de la respuesta sea el esperado
    assert response.json() == {"concatenated": "ab"}

def test_concatenar_otros_caracteres():
    # Probar otro caso
    response = client.get("/concat/x/y")
    assert response.status_code == 200
    assert response.json() == {"concatenated": "xy"}

def test_concatenar_con_caracteres_numericos():
    # Probar con caracteres numéricos
    response = client.get("/concat/1/2")
    assert response.status_code == 200
    assert response.json() == {"concatenated": "12"}

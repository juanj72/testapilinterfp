from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root() -> dict:
    """Endpoint raíz que retorna un mensaje de saludo."""
    return {"message": "Hello World"}


@app.get("/concat/{c1}/{c2}")
async def concat_chars(c1: str, c2: str) -> JSONResponse:
    """
    Endpoint que concatena dos cadenas.

    Args:
        c1 (str): Primer carácter o cadena.
        c2 (str): Segundo carácter o cadena.

    Returns:
        JSONResponse: Resultado de la concatenación en formato JSON.
    """
    result = c1 + c2
    return JSONResponse(content={"concatenated": result})

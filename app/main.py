from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/sum", status_code=status.HTTP_200_OK)
async def sum(number1: int, number2: int):
    return JSONResponse(content={"result": number1 + number2})

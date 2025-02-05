from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/concat/{c1}/{c2}")
async def concat_chars(c1: str, c2: str):
    result = c1 + c2
    return JSONResponse(content={"concatenated": result})

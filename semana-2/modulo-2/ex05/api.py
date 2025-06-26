from fastapi import FastAPI, status, Request

from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from datetime import datetime
import sys

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "message": "A requisição contém dados inválidos.",
        }
    )
    
@app.get("/")
async def get():
    return {'message': 'Bem-vindo à minha API!'}

@app.get("/info")
async def info():
    return f'"now": "{datetime.now()}", "version": "{sys.version}"'

@app.post("/", status_code=status.HTTP_201_CREATED)
async def post(json: dict[str, str]):
    return []

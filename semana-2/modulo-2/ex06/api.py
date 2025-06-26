from fastapi import FastAPI, status, HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from datetime import datetime
import platform
import sys

class Account(BaseModel):
    name: str
    age: int
    email: str
    balance: float

app = FastAPI()

@app.get("/")
async def get():   
    return {'message': 'Bem-vindo à minha API!'}

@app.get("/info")
async def info():
    return f'"now": "{datetime.now()}", "version": "{sys.version}"'

@app.post("/", status_code=status.HTTP_201_CREATED)
async def post(json: dict[str, str]):
    return []

@app.post("/create", status_code=status.HTTP_201_CREATED)
async def post(json: Account):
    ac = Account(name = json.name, age=json.age, email=json.email, balance=json.balance)
    return {'message': 'Conta criada com sucesso!'}




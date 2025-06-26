from datetime import datetime
from fastapi import FastAPI, status, HTTPException
from database import create_account, get_account, get_account_by_id, create_operation, get_operations, delete_account
from schemas import AccountCreate, OperationCreate
from models import Account, Operations
from sqlalchemy import exc
from typing import List

app = FastAPI()

@app.put("/accounts", status_code=status.HTTP_201_CREATED)
async def create_accounts(account: AccountCreate) -> int: 
    try:  
        if account.id is None:
            db_item = Account(name=account.name, email=account.email)
        else:
            db_item = Account(**account.model_dump())
        return create_account(db_item)
    except exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Conta {account.id} já existe.")
    
@app.get("/accounts")
async def get_accounts_all(): 
    list_account = get_account()
    if len(list_account) == 0:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    else:
        return list_account
    
@app.get("/accounts/{account_id}") 
async def get_accounts(account_id: int):
    account = get_account_by_id(account_id)
    if account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Conta {account_id} não encontrada.")
    else:
        return account
    
@app.post("/accounts/{account_id}/operations", status_code=status.HTTP_201_CREATED) 
async def create_operations(account_id: int, operation: OperationCreate) -> int:
    operation = Operations(account_id=account_id,operation=operation.operation.value, amount=operation.amount, create_at=datetime.now())
    account = get_account_by_id(account_id)
    if account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Conta {account_id} não encontrada.")
    else:
        return create_operation(operation)
    
@app.get("/accounts/{account_id}/operations") 
async def get_account_operations(account_id: int):
    list_operations = get_operations(account_id)
    if len(list_operations) == 0:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return list_operations

@app.delete("/accounts/{account_id}", status_code=status.HTTP_204_NO_CONTENT) 
async def delete_accounts(account_id: int) -> None:
    account = get_account_by_id(account_id)
    if account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return delete_account(account_id)
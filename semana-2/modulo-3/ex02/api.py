from fastapi import FastAPI, status, HTTPException
from database import create_account
from schemas import AccountCreate
from models import Account
from sqlalchemy import exc

app = FastAPI()

@app.put("/accounts", status_code=status.HTTP_201_CREATED)
async def create_account_api(account: AccountCreate) -> int: 
    try:  
        if account.id is None:
            db_item = Account(name=account.name, email=account.email)
        else:
            db_item = Account(id=account.id,name=account.name, email=account.email)
        return create_account(db_item)
    except exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Conta {account.id} já existe.")
from fastapi import FastAPI, status, HTTPException
from database import create_account, get_account, get_account_by_id
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
    
    
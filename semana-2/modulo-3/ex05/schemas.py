from typing import Optional
from pydantic import BaseModel
from models import OperationType

class AccountCreate(BaseModel):
    id: Optional[int] = None
    name: str
    email: str

class OperationCreate(BaseModel):
    operation: OperationType
    amount: int
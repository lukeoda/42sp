from typing import Optional
from pydantic import BaseModel

class AccountCreate(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
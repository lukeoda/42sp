from models import Account, Operations
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Engine
import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_SENHA')}"
    f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

def get_engine(db_url: str) -> Engine:
    return create_engine(db_url)

def create_account(account: Account) -> int :
        engine = get_engine(DATABASE_URL)
        with sessionmaker(bind=engine)() as session:             
            session.add(account)
            session.commit()
            session.refresh(account)
            
            return account.id
        
def get_account() -> list[Account]:
    engine = get_engine(DATABASE_URL)
    with sessionmaker(bind=engine)() as session: 
        return session.query(Account).all()
        
def get_account_by_id(account_id: int) -> Account:
    engine = get_engine(DATABASE_URL)
    with sessionmaker(bind=engine)() as session: 
        return session.query(Account).filter_by(id=account_id).first()
    
def create_operation(operation: Operations) -> int:
    engine = get_engine(DATABASE_URL)
    with sessionmaker(bind=engine)() as session:             
        session.add(operation)
        session.commit()
        session.refresh(operation)
            
    return operation.id

def get_operations(account_id: int) -> list[Operations]:
    engine = get_engine(DATABASE_URL)
    with sessionmaker(bind=engine)() as session: 
        return session.query(Operations).filter_by(account_id=account_id).all()
    
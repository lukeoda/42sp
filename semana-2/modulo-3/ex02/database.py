from models import Account
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Engine
from dotenv import load_dotenv

import os

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
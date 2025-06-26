from sqlalchemy import Engine, select, create_engine, Integer, Float, Date, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column, relationship
from datetime import date
from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_SENHA')}"
    f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
)

class OperationType(Enum):
    credit = '+'
    debit = '-'

class Account(Base):
    __tablename__="accounts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))


class Operations(Base):
    __tablename__="operations"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    account_id: Mapped[str] = mapped_column(ForeignKey("accounts.id"))
    operation: Mapped[OperationType] = mapped_column(String(1))
    amount: Mapped[int] = mapped_column(Integer)
    create_at: Mapped[date] = mapped_column(Date)

    def __repr__(self):
        return (
            f"<Transaction("
            f"id={self.id}, "
            f"account_id='{self.account_id}', "
            f"operation={self.operation.name} ({self.operation.value})"
            f"amount={self.amount}, "
            f"create_at={self.create_at}, "
            f")>"
        )

def get_engine(db_url: str):
    return create_engine(DATABASE_URL)

def get_session_factory(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables(engine_url: str):
    engine = get_engine(engine_url)
    Base.metadata.create_all(engine)


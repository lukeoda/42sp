from sqlalchemy import Integer, Date, String, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from datetime import date
from enum import Enum

Base = declarative_base()

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

    def __repr__(self) -> str:
        return (
            f"<Transaction("
            f"id={self.id}, "
            f"account_id='{self.account_id}', "
            f"operation={self.operation.name} ({self.operation.value})"
            f"amount={self.amount}, "
            f"create_at={self.create_at}, "
            f")>"
        )
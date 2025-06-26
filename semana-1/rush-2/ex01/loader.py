from datetime import date
import sys
import json
import csv
from typing import Any
from sqlalchemy import Engine, select, create_engine, Column, Integer, Float, Date, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__="ACCOUNTS"
    numero: Column[str] = Column(String, primary_key=True)
    titular: Column[str] = Column(String)
    saldo: Column[float] = Column(Float)
    limite: Column[int] = Column(Integer)
    data_abertura: Column[date] = Column(Date)

    def __eq__(self, value: Any)->bool:
        if isinstance(value, Account):
            return True if self.numero == value.numero else False
        else:
            return False
    
    def __hash__(self)->int:
        return hash(self.numero)
    
    def __str__(self)->str:
        return f"{self.numero}"
    
    def __repr__(self)->str:
        return f"{self.numero}"
    
def rec_contas_from_file(file_path: str)-> set[Account]:
    retorno = set[Account]()
    if(file_path.endswith(".jsonl")):
        with open(file_path, 'r') as f:
            for line in f:
                d = json.loads(line)
                data = d['data_abertura'].split("-")
                d['data_abertura'] = date(int(data[0]), int(data[1]), int(data[2]))
                retorno.add(Account(**d))
    else:
        with open(file_path, 'r') as f:
            for linha in csv.DictReader(f):
                data = linha['data_abertura'].split("-")
                linha['data_abertura'] = date(int(data[0]), int(data[1]), int(data[2]))
                retorno.add(Account(**linha))
    return retorno

def get_contas_from_bd(engine: Engine)->list[Account]:
    stmt = select(Account)
    with sessionmaker(bind=engine)() as session:
        return [row[0] for row in session.execute(stmt)]

def filtrar_duplicados(contas:list[Account], contas_bd:list[Account])->list[Account]:
    return [conta for conta in contas if conta not in contas_bd]

def inserir_contas(contas: list[Account], engine: Engine)->None:
    if len(contas)>0: 
        with sessionmaker(bind=engine)() as session:
            session.add_all(contas)
            session.commit()
                
def main() -> None:
    if len(sys.argv) > 1:
        engine = create_engine('sqlite:///banco.db')
        Base.metadata.create_all(engine)
        file_path = sys.argv[1]
        contas = rec_contas_from_file(file_path)
        contas_cadastradas = get_contas_from_bd(engine)
        contas_insert = filtrar_duplicados(list(contas), contas_cadastradas)
        inserir_contas(contas_insert, engine)
        
    else:
        print("Faltou o nome do arquivo para inserção")
 
    

if __name__ == "__main__":
    main()
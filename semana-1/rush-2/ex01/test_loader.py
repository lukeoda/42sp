from datetime import date
import pytest
import loader
from loader import Account, filtrar_duplicados, rec_contas_from_file
from sqlalchemy import Engine, select, create_engine, Column, Integer, Float, Date, String
from sqlalchemy.orm import sessionmaker, declarative_base

@pytest.mark.parametrize("input,expected",[
    ('../arquivos/accounts.jsonl', 67),
    ('../arquivos/accounts.csv', 64),
])
def test_rec_contas_from_file(input, expected):
    assert len(rec_contas_from_file(input)) == expected


def test_filtrar_duplicados():
    contas = [
        Account(**{"numero": "95124-4", "titular": "Jo\u00e3o Victor", "saldo": "6542.19", "limite": "5000", "data_abertura": date(2015,10,20)}),
        Account(**{"numero": "95124-4", "titular": "Jo\u00e3o Victor", "saldo": "6542.19", "limite": "5000", "data_abertura": date(2015,10,20)})
    ]

    contas2 = [
        Account(**{"numero": "95124-4", "titular": "Jo\u00e3o Victor", "saldo": "6542.19", "limite": "5000", "data_abertura": date(2015,10,20)}),
        Account(**{"numero": "95124-4", "titular": "Jo\u00e3o Victor", "saldo": "6542.19", "limite": "5000", "data_abertura": date(2015,10,20)})
    ]
    assert len(filtrar_duplicados(contas, contas2)) == 0

def test_inserir_contas():
    engine = create_engine('sqlite:///banco_test.db')
    loader.Base.metadata.create_all(engine)
    contas = [
        Account(**{"numero": "95124-4", "titular": "Jo\u00e3o Victor", "saldo": "6542.19", "limite": "5000", "data_abertura": date(2015,10,20)}),
    ]
    loader.inserir_contas(contas, engine)
    retorno = loader.get_contas_from_bd(engine)

    assert retorno[0].numero == "95124-4"
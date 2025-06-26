from fintech import TabelaConta

def test_account():
    contas = TabelaConta('booking_accounts.csv')
    assert len(contas.all()) == 50


def test_account_negative():
    contas = TabelaConta('booking_accounts.csv')
    negativas = contas.contas_negativas()
    assert len(negativas) == 4

def test_account_filter_by():
    contas = TabelaConta('booking_accounts.csv')
    contas_filtradas = contas.filter_by(titular="Amanda Teixeira")
    assert len(contas_filtradas) == 4

def test_account_first():
    contas = TabelaConta('booking_accounts.csv')
    contas_filtradas = contas.first(titular="Amanda Teixeira")
    assert str(contas_filtradas) in "Client(account_number='34633-4', titular='Amanda Teixeira', saldo=7314.7, limite=2000, data_abertura='2023-12-19')"
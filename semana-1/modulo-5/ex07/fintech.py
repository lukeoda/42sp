from dataclasses import dataclass
import csv

@dataclass
class Client:
    '''
    para executar o programa abaixo
    vc deve estar na estrura do projeto
    rodar os seguintes comandos
    python3
    from ex06.account import Account
    ac = Account(123, ['123.456.789-10'])
    ac.deposit(123, 'ATM deposit')
    ac.withdraw(123, 'ATM withdraw')
    ac.statement()
    print(t)
    '''
    account_number: str
    titular: str
    saldo: float
    limite: int
    data_abertura: str

class TabelaConta:
    def __init__(self, csv_path: str):
        self.accounts: list[Client] = []
        self.__load_accounts(csv_path)

    def __load_accounts(self, csv_path: str):
        with open(csv_path, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    account = Client(
                        account_number=row['numero'],
                        titular=row['titular'],
                        saldo=float(row['saldo']),
                        limite=int(row['limite']),
                        data_abertura=row['data_abertura']
                    )
                    self.accounts.append(account)
    
    def all(self) -> list[Client]:
        return self.accounts

    def contas_negativas(self) -> list[Client]:
        return [conta for conta in self.accounts if conta.saldo < 0.00]

    def first(self, **criteria):
        for conta in self.accounts:
            if all(getattr(conta, key) in value for key, value in criteria.items()):
                print(conta)
                return conta
        return None

    def filter_by(self, **criteria):
        return [
            conta for conta in self.accounts
                if all(getattr(conta, key) == value for key, value in criteria.items())
        ]
    
                    
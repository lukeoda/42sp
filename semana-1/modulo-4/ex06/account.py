from ex04.utils import format_cents
from ex05.operation import Operation

class Account:
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
    def __init__(self, account_id: int, cpfs: list[str]):
        self.account_id = account_id
        self.cpfs = cpfs
        self.__balance = 0
        self.__operations:list[str] = []
    
    def deposit(self, amount: int, description: str) -> None:
        '''
        funcao que faz o deposito na conta
        validacoes: nao e permitido valores abaixo de 0
        parametros: (valor, descricao do deposito)
                    (123, 'ATM deposit')
        '''

        if amount < 0:
            raise ValueError("valor deve ser > 0")
        t = Operation(amount, 'credit' if amount > 0 else 'debit', description)
        self.__balance += amount
        self.__operations.append(str(t))
    
    def withdraw(self, amount: int, description: str) -> None:
        '''
        funcao que faz o saque na conta
        permitido passar valores negativos e positivos
        validacoes: nao e permitido valores acima do saldo em conta
        parametros: (valor, descricao do deposito)
                    (123, 'ATM withdraw')
        '''
        if amount < 0:
            amount = amount *-1
        if amount > self.__balance:
            raise ValueError("saldo insuficiente")        
        t = Operation(amount, 'credit' if amount < 0 else 'debit', description)
        self.__balance -= amount
        self.__operations.append(str(t))
    
    def statement(self) -> None:
        '''
        funcao que retorna todas as operacoes realizadas na conta
        '''
        for item in self.__operations:
            print(item)
        print(f"\nBalance: {'[+]' if self.__balance >= 0 else '[-]'} {format_cents(self.__balance)}")
    
    def __repr__(self) -> str:
        return f"Account({self.account_id}, ...)"

    def __str__(self) -> str:
        return  f"Account: {self.account_id} \nBalance: {'[+]' if self.__balance >= 0 else '[-]'} {format_cents(self.__balance)}"
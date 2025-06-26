from ex04.utils import format_cents

class Operation:
    '''
    para executar o programa abaixo
    vc deve estar na estrura do projeto
    rodar os seguintes comandos
    python3
    from ex05.operation import Operation
    t = Operation(12145, 'credit', 'ATM DEPOSIT')
    print(t)
    '''
    def __init__(self, cents: int, op_type: str, description: str):
        if cents <= 0:
            raise ValueError("valor nao aceito")
        self.cents = cents
        self.op_type = op_type
        self.description = description
    
    def __repr__(self) -> str:
        return f"Operation(cents={self.cents}, op_type='{self.op_type}', description='{self.description}')"

    def __str__(self) -> str:
        return f"{'[+]' if self.op_type == 'credit' else '[-]'} {format_cents(self.cents)} ({self.description})"
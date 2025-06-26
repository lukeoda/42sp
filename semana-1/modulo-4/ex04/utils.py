def format_cents(value: int) -> str:
    ''' 
    para executar esse programa, basta seguir os digitar os comandos abaixo
    python3
    import utils
    print(utils.format_cents(11_222_00))
    '''
    reais, centavos = divmod(value, 100)
    return 'R$ ' + f'{reais:,}'.replace(',','.') + f',{centavos:02d}'



class InsufficientBalance(Exception):
    '''Excecao personalizada para saldo insulficiente em conta'''
    pass
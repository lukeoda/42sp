class Person:
    '''
    para executar o programa abaixo
    vc deve estar na estrura do projeto
    rodar os seguintes comandos
    python3
    from person import Person
    p = Person('LUCAS', 30)
    p.birthday()
    '''
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def birthday(self) -> None:
        self.age += 1

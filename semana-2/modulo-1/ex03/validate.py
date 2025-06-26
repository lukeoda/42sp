from pydantic import BaseModel
import json
import sys


class Account(BaseModel):
    name: str
    age: int
    email: str
    balance: float

def ler_arquivo_json(filename: str) -> None:
    try:
        with open(filename, "r") as f:
            dados = json.load(f)
    except FileNotFoundError:
        print("Erro: O arquivo dados.json não foi encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro: O arquivo dados.json não contém JSON válido.")
        return
    except pydantic.ValidationError as e:
        print("Erro de validação dos dados:")
        return

    # Validar se o arquivo contém uma lista dcle usuários
    lista_de_usuarios_validada = Account(**dados)
    #print(lista_de_usuarios_validada)

def main():
    filename = sys.argv[1]
    ler_arquivo_json(filename)


if __name__ == "__main__":
    main()
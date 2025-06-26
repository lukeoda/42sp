import boto3
import sys
import csv
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

def load_user(filename: str, table):
    try:
        with open(filename) as f:
            reader = csv.DictReader(f, delimiter=',')
            print(f'Carregando dados de {filename}')
            for row in reader:
                table.put_item(
                    Item={
                    'Id': row["id"],
                    'Nome': row["name"]
            }
        )
    except ClientError as err:
        print('Error Code: {}'.format(err.response['Error']['Code']))
        print('Error Message: {}'.format(err.response['Error']['Message']))
    except IsADirectoryError:
        print('Erro: O argumento enviado e um diretorio')
    except FileNotFoundError:
        print('Erro: Arquivo nao encontrado')
        
def get_user(id: str, table):
    try:
        response = table.get_item(
            Key={
                'Id': id
            }
        )
        item = response.get('Item')
        if item:
            print(f"Usuário encontrado: {item}")
        else:
            print(f"Usuário com Id '{id}' não encontrado.")
    except ClientError as err:
        print('Error Code: {}'.format(err.response['Error']['Code']))
        print('Error Message: {}'.format(err.response['Error']['Message']))  
    except Exception as e:
        print(f"Erro ao buscar usuário(id: {id}): {e}")
        
def delete_user(id: str, table):
    try:
        table.delete_item(
            Key={
                'Id': id
            }
        )
        print(f'Usuário {id} removido.')
    except ClientError as err:
        print('Error Code: {}'.format(err.response['Error']['Code']))
        print('Error Message: {}'.format(err.response['Error']['Message']))  
    except Exception as e:
        print(f"Erro ao buscar usuário(id: {id}): {e}")
        return None      

def update_user(id: str, name:str, table):
    try:
        response = table.update_item(
            Key={
                'Id': id
            },
            UpdateExpression="set Nome=:n",
            ExpressionAttributeValues={":n": name},
            ReturnValues="UPDATED_NEW",
        )
        print(f'Usuário {id} atualizado para {response["Attributes"]}')
    except ClientError as err:
        print('Error Code: {}'.format(err.response['Error']['Code']))
        print('Error Message: {}'.format(err.response['Error']['Message']))  
    except Exception as e:
        print(f"Erro ao buscar usuário(id: {id}): {e}")
        return None      

def main():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Usuarios')
    
    if len(sys.argv) > 1:
        command = sys.argv[1] 

        if command == "load":
            if len(sys.argv) > 2:
                filename = sys.argv[2]
                load_user(filename, table)
            else:
                print("Erro: Nenhum arquivo fornecido para o comando 'load'.")
        elif command == "retrieve":
            if len(sys.argv) > 2:
                id = sys.argv[2]
                get_user(id, table)
            else:
                print("Erro: Nenhum Id fornecido para o comando 'retrieve'.")
        elif command == "delete":
            if len(sys.argv) > 2:
                id = sys.argv[2]
                delete_user(id, table)
            else:
                print("Erro: Nenhum Id fornecido para o comando 'retrieve'.")            
        elif command == "update":
            if len(sys.argv) > 3:
                id = sys.argv[2]
                name = sys.argv[3]
                update_user(id, name, table)
            else:
                print("Erro: Nenhum Id fornecido para o comando 'retrieve'.")
        else:
            print(f"Comando '{command}' não reconhecido.")
    else:
        print("Nenhum comando fornecido.")

if __name__ == "__main__":
    '''
    Uso: 
    python3 dynamo_crud.py load "./users/users.csv"
    python3 dynamo_crud.py update "u448" "LUCAS ODA" 
    python3 dynamo_crud.py retrieve u448
    python3 dynamo_crud.py retrieve u448
    '''
    main()

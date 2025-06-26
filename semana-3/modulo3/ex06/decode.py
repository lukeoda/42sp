import base64
import uuid
import boto3
from botocore.exceptions import ClientError

def ler_salvar_conteudo(conteudo: str) -> str:
    uuid_file_name = uuid.uuid4()
    filename = f'{uuid_file_name}.jpg'
    if(isinstance(conteudo, bytes)):
        conteudo = conteudo.decode('utf-8')
    if conteudo.startswith('data:image'):
        conteudo = conteudo.split(',')[1]
    with open(filename, "wb") as image_file:
        image_file.write(base64.b64decode(conteudo))
    
    upload_file(filename)
    
    return uuid_file_name

def upload_file(file_name):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, '42sp-lkenji-o-bucket', file_name)
    except ClientError as err:
        print('Error Code: {}'.format(err.response['Error']['Code']))
        print('Error Message: {}'.format(err.response['Error']['Message']))
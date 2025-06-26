import sys
import base64
import boto3

file_name = sys.argv[2]
bucket_name = sys.argv[1]



def decode_image(base64_str: str) -> bytes:
    object_name = 'image.jpg'
    
    with open("sample_images/image.jpg", "wb") as image_file:
        image_file.write(base64.b64decode(base64_str))
        
    print('sample_images/image.jpg saved!')
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_name, bucket_name, object_name)
    print(f"'{file_name}' saved on bucket '{bucket_name}/{object_name}'")


def ler_arquivo(filename: str) -> str:
        with open(filename, 'rb') as file:
            conteudo = file.read()
        if(isinstance(conteudo, bytes)):
            conteudo = conteudo.decode('utf-8')
        if conteudo.startswith('data:image'):
            conteudo = conteudo.split(',')[1]
        return conteudo
      
      
      
def main() -> None:
    '''
	para rodar o programa basta digitar o comando
    'python3 decode.py 42sp-lkenji-o-bucket "sample_images/image1.txt"'
	'''
    filename = 'sample_images/image1.txt'
    conteudo = ler_arquivo(filename)
    decode_image(conteudo)
		
if __name__ == '__main__':
	main()
	
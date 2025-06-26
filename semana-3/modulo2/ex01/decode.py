import sys
import base64


def decode_image(base64_str: str) -> bytes:
    with open("sample_images/image.jpg", "wb") as image_file:
        image_file.write(base64.b64decode(base64_str))
    print('sample_images/image.jpg saved!')


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
    'python3 decode.py sample_images/image1.txt'
    'python3 decode.py sample_images/image2.txt'
    'python3 decode.py sample_images/image3.txt'

	'''
    filename = sys.argv[1]		
    conteudo = ler_arquivo(filename)
    decode_image(conteudo)
		
if __name__ == '__main__':
	main()
	
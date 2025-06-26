import sys


def read_file(filename: str, new_filename: str) -> None:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file.read()
        print('arquivo ja esta no padrao utf 8')
    except UnicodeDecodeError:
        try:
            with open(filename, 'r', encoding = 'iso-8859-1') as f:
                conteudo = f.read()
            
            with open(new_filename, 'w', encoding='utf-8') as newfile:
                newfile.write(conteudo)
            print(f"Arquivo '{new_filename}' criado com sucesso.")
        except Exception:
                print('Erro ao tentar converter o texto para utf-8')

def main() -> None:
    '''
	para rodar o programa basta digitar o comando
	o primeiro argumento eh o arquivo ja existente iso-8559-1
    o segundo argumento eh o nome do arquivo a ser gerado com padrao utf8
    'python3 utf8.py iso-8859-1_encoded.txt newfile.txt'

	'''
    file = sys.argv[1]
    newfile = sys.argv[2]
    read_file(file, newfile)
		
		
if __name__ == '__main__':
	main()
	
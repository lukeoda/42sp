import sys

def read_file(filename: str) -> None:
	try:
		with open(filename, "r") as f:
			conteudo = f.read()
			print(conteudo)	
	except IsADirectoryError:
		print('Erro: O argumento enviado e um diretorio')
	except FileNotFoundError:
		print('Erro: Arquivo nao encontrado')
	except PermissionError:
		print('Erro: Permissao negada para ler o arquivo')
	except UnicodeDecodeError:
		print('Erro inesperado: UnicodeDecodeError')
	

def main() -> None:
	'''
	para rodar o programa basta digitar o comando
	'python3 read_file.py "txt.txt"'
	'python3 read_file.py "segredo.txt"' - necessario criar o arquivo sem permissao
	'python3 read_file.py "corrompido.txt"'
	'python3 read_file.py "/bin/"'

	'''
	param_1 = sys.argv[1] 
	read_file(param_1)
		
		
if __name__ == '__main__':
	main()
	



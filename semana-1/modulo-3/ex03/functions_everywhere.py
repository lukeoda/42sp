import sys

def shrink(frase: str) -> str:
	return frase[:8]
	
def enlarge(frase: str) -> str:
	return frase.ljust(8, 'Z')
	

def main(lista: list[str]) -> None:
	if len(lista) == 0:
		print('None')
	for linha in lista:
		if len(linha) < 8:
			print(enlarge(linha))
		elif len(linha) > 8:
			print(shrink(linha))
		else:
			print(linha)
		
if __name__ == '__main__':
	'''
	para executar o programa basta executar o programa "python3 functions_everywhere.py 'lol' 'physi' 'backpack' 'a'"
	'''
	lista = sys.argv[1:]
	main(lista)
	

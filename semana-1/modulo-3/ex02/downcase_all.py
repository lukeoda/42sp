import sys

def main(lista: list[str]) -> None:
	if len(lista) == 0:
		print('None')
	for linha in lista:
		print(linha.lower())		
		
if __name__ == '__main__':
	'''
	para rodar o programa basta executar o comando python3 downcase_all.py "DeVe FiCaR TuDo MiNuScUlO" "eSsA aQuI TaMbEm" "e PoDe PasSaR qUanTas sTrIngS QuIsEr"
	'''
	lista = sys.argv[1:]
	main(lista)
	

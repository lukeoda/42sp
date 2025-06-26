import sys

def square(num: int, voltas: int) -> None:	
	j = 0
	while j < voltas:	
		print(multiplicacao(j))
		j += 1 
		
def multiplicacao(num: int) -> list[int]:
	k = 0
	result = []	
	while k < 11:
			result.append(num * k)
			k += 1	
	return result
	

def main() -> None:
	if len(sys.argv) > 1:
		if 0 < int(sys.argv[1]) > 100:
			print('Erro: o numero deve ser entre 0 e 100')
			return
		else:
			print(multiplicacao(int(sys.argv[1])))
	else:	
		square(10, 11)
	
if __name__ == '__main__':
	'''
	para rodar o programa basta digitar o comando python3 square.py 0-50 
	o programa aceita numeros de 0 a 50
	para rodar o teste necessario instalar a biblioteca pytest e executar o comando 'pytest'
	'''
	main()

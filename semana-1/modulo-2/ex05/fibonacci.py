import sys

param_1 = sys.argv[1]

def fibonacci(n:int) -> int:   # retorna a série de Fibonacci até n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result[-1]

def main() -> None:
	if not param_1.isdigit():
		print("Erro: parametro deve ser numerico")
		return
	
	if 0 < int(param_1) > 9:
		print('Erro: o numero deve ser entre 0 e 9')
		return
		
	if int(param_1) == 0:
		print('0')
		return	
		
	print(fibonacci(int(param_1)))
	
	

if __name__ == '__main__':
	'''
	para rodar o programa basta digitar o comando python3 fibonacci.py 0 
	o programa aceita numeros de 0 a 9
	'''
	main()
	
	



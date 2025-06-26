import sys

param_1 = sys.argv[1]


def square(num: int) -> None:
	i = 0
	while i < 1:
		print('%' + '-' * (num -2) + '%')
		i += 1
	
	j = 0
	while j < num - 2:
		print('|' + ' ' * (num -2) + '|')
		j += 1
	
	k = 0
	while k < 1:
		print('%' + '-' * (num -2) + '%')
		k += 1


def main() -> None:
	if not param_1.isdigit():
		print("Erro: parametro deve ser numerico")
		return
	
	if 0 < int(param_1) > 50:
		print('Erro: o numero deve ser entre 0 e 50')
		return
		
	print(square(int(param_1)))
	
	

if __name__ == '__main__':
	'''
	para rodar o programa basta digitar o comando python3 square.py 0-50 
	o programa aceita numeros de 0 a 50
	'''
	main()

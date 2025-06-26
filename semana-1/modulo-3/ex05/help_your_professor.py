def average(dicionario: dict[str, int]) -> float:
	'''
	para rodar esse codigo, eh necessario seguir os passos:
	abra o promt de comando
	digite python3
	importe o arquivo.py e o metodo 'from help_your_professor import average'
	digite a entrada necessaria
	class_3B = {
	"marine": 18,
	"jean": 15,
	"coline": 8,
	"luc": 9
	}
	class_3C = {
	"quentin": 17,
	"julie": 15,
	"marc": 8,
	"stephanie": 13
	}
	print(f"Average for class 3B: {average(class_3B)}.")
	print(f"Average for class 3C: {average(class_3C)}.")
'''

	if not dicionario:
		return 0
	
	total = sum(dicionario.values())
	return total / len(dicionario)


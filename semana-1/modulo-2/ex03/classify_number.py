import sys

param_1 = sys.argv[1] 

def isPositive(num: int) -> bool:
	return num > 0
		
def isEven(num: int) -> bool:
	return num % 2 == 0
		

def main() -> None:
	if int(param_1) == 0:
		print('zero')
		return
	else:
		positiveNegative = isPositive(int(param_1))
		evenOdd = isEven(int(param_1))
	
	msgPositive= 'positive ' if positiveNegative else 'negative '	
	msgEven = 'and even' if evenOdd else 'and odd'
	print(msgPositive + msgEven)


if __name__ == "__main__":
  main()
			
	

		

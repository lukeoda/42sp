import sys

def is_even(x: int) -> int:
	return x % 2 == 0
	
def square(x:int) -> int:
        return x * x	

def square_even_numbers(numbers: str) -> list[int]:
	list_numbers = list(map(int, numbers.split()))
	result = map(square, filter(is_even, list_numbers))	

	return list(result)
	
def main() -> None:
	param_1 = sys.argv[1] 
	print(f'Squared evens: {square_even_numbers(param_1)}')

if __name__ == '__main__':	
	main()	
	
	
	

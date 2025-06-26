import sys

def square_even_numbers(numbers: str) -> list[int]:
	
	
	list_numbers = list(map(int, numbers.split()))
	square_numbers = [x * x for x in list_numbers if x%2==0]

	return square_numbers
	
def main() -> None:
	param_1 = sys.argv[1] 
	print(square_even_numbers(param_1))
	

if __name__ == '__main__':	
	main()	
	
	
	

from new_transform import square_even_numbers
import sys 

def test_square_even_numbers(monkeypatch):
	numbers = "1 2 3 4 5 6 7 8 9 10"
	monkeypatch.setattr(sys, "argv", ["transform.py", numbers]) 

	assert square_even_numbers(numbers) == [4, 16, 36, 64, 100]
	 

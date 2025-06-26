from help_your_professor import average

def test_average_1():
	class_3B = {
		"marine": 18,
		"jean": 15,
		"coline": 8,	
		"luc": 9
	}
	assert average(class_3B) == 12.5
    	
def test_average_2():
	class_3C = {
		"quentin": 17,
		"julie": 15,
		"marc": 8,
		"stephanie": 13
	}
	assert average(class_3C) == 13.25	
	
def test_average_empty():
	class_3C = {}
	assert average(class_3C) == 0

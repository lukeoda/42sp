from functions_everywhere import shrink, enlarge

def test_shrink():
	assert shrink('abcdefghij') == 'abcdefgh'
	
def test_enlarge():
	assert enlarge('abc') == 'abcZZZZZ'

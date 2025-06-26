import pytest
from cardnames import fit

@pytest.mark.parametrize("given,expected", [
    ("João Carlos da Silva Junior", "João Carlos Silva Junior"), 
    ("Elisa Mirella Maitê de Paula", "Elisa Mirella Maitê Paula"),
    ("Gabriel Joao da Silva Jardins Maitê de Paula Junior", "Gabriel Joao S J M P Jr"),
    ("Gabriel Joao Silva Jardins Filho", "G Joao Silva Jardins Filho"), 
    ])
def test_fit(given,expected):
    given=given.upper()
    expected=expected.upper()
    result = fit(given)
    assert result == expected

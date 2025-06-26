from coordinates import Coordinates

def test_coordinates_create():
    coord = Coordinates(12.12, 36.36)
    assert str(coord) in 'Coordinates(lat=12.12, long=36.36)'


def test_person_birth():
    c1 = Coordinates(12.12, 24.24)
    c2 = Coordinates(24.24,12.12)
    c3 = Coordinates(12.12,24.24)

    assert c1 == c3
    assert c1 != c2
    assert c2 != c3
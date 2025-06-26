from person import Person

def test_person_initialization():
    p = Person("Alice", 30)
    assert p.name == "Alice"
    assert p.age == 30


def test_person_birth():
    p = Person("Lucas", 30)
    p.birthday()
    assert p.name == "Lucas"
    assert p.age == 31
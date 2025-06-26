from your_namebook import list_of_names


def test_list_of_names():
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier",
    }
    assert list_of_names(persons) == [
        "Jean Valjean",
        "Grace Hopper",
        "Xavier Niel",
        "Fifi Brindacier",
    ]


def test_list_of_names_empty():
    persons = {}
    assert list_of_names(persons) == []


def test_list_of_names_spaces():
    persons = {
        "jean lucca": "valjean silva",
        "grace maria": "hopper souza",
        "xavier xarles": "niel mendes",
        "fifi fofo": "brindacier brincadeira",
    }
    assert list_of_names(persons) == [
        "Jean Lucca Valjean Silva",
        "Grace Maria Hopper Souza",
        "Xavier Xarles Niel Mendes",
        "Fifi Fofo Brindacier Brincadeira",
    ]

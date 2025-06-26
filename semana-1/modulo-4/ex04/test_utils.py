from utils import format_cents


def test_utils_format_cents():
    valor = format_cents(11_222_00)
    assert valor == 'R$ 11.222,00'
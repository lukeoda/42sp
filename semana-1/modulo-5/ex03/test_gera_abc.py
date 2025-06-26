from gera_abc import gen_ABC
import pytest

def test_gera_abc(capfd):
    g = gen_ABC()

    valor = next(g)
    out = capfd.readouterr().out
    assert valor == 'A'
    assert '*** iniciando' in out
    assert '*** produzindo A' in out

    valor = next(g)
    out = capfd.readouterr().out
    assert valor == 'B'
    assert '*** produzindo B' in out

    valor = next(g)
    out = capfd.readouterr().out
    assert valor == 'C'
    assert '*** produzindo C' in out

    with pytest.raises(StopIteration):
        next(g)
    out = capfd.readouterr().out
    assert '*** terminando' in out
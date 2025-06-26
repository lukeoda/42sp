from validate import ler_arquivo_json
import pytest

def test_ler_arquivo_json(capsys):
    ler_arquivo_json('member.json')
    
    captured, err = capsys.readouterr()

    assert err == ''

def test_minha_funcao_com_outro_erro(capsys):
    ler_arquivo_json("member_nao_existente")
    captured, err = capsys.readouterr()

    assert captured in 'Erro: O arquivo dados.json não foi encontrado.\n'


def test_minha_funcao_com_outro_erro(capsys):
    ler_arquivo_json('member_erro.json')
    captured, err = capsys.readouterr()

    assert captured in 'Erro: O arquivo dados.json não contém JSON válido.\n'






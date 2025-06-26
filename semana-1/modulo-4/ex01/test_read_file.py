from read_file import main
import sys

def test_main_sucess(monkeypatch, capsys):
    path = 'txt.txt'
    monkeypatch.setattr(sys, "argv", ["read_file.py", path])

    main()

    out = capsys.readouterr().out
    assert out == "TEXTO ESCRITO DENTRO DO ARQUIVO txt.txt\n\n"

def test_main_except_permission(monkeypatch, capsys):
    path = 'segredo.txt'
    monkeypatch.setattr(sys, "argv", ["read_file.py", path])

    main()

    out = capsys.readouterr().out
    assert out == "Erro: Permissao negada para ler o arquivo\n"

def test_main_except_directory(monkeypatch, capsys):
    path = '/bin/'
    monkeypatch.setattr(sys, "argv", ["read_file.py", path])

    main()

    out = capsys.readouterr().out
    assert out == "Erro: O argumento enviado e um diretorio\n"

def test_main_except_directory(monkeypatch, capsys):
    path = 'corrompido.txt'
    monkeypatch.setattr(sys, "argv", ["read_file.py", path])

    main()

    out = capsys.readouterr().out
    assert out == "Erro inesperado: UnicodeDecodeError\n"



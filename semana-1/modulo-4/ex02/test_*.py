from utf8 import main
import sys
import os

def test_main_sucess(monkeypatch):
    path = 'iso-8859-1_encoded.txt'
    newfile = 'newfiletest.txt'
    monkeypatch.setattr(sys, "argv", ["read_file.py", path, newfile])

    main()

    assert os.path.exists(newfile)
    with open(newfile, 'r', encoding='utf-8') as file:  
        conteudo = file.read()
    assert conteudo == 'Conversão de Código\n'

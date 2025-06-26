# Apresentando doctests

> [!TIP]
> Você precisa ler e editar este arquivo para completar o exercício.
> Use a linha de comando abaixo para executar os testes até o primeiro
> que falhar. Siga corrigindo teste por teste, repetindo o comando até
> que o `doctest` não indique mais nenhum erro.
> Use a opção `-f` (*fail fast*) para que o `doctest` pare no primeiro
> erro, assim:

```shell
?> python3 -m doctest -f FIX_ME.md
```

## Sintaxe dos testes

O módulo `doctest` da biblioteca padrão do Python executa cada linha
marcada com `>>>` e verifica se o resultado é igual ao que aparece
nas linhas seguintes.

Por exemplo:

```python
>>> 1 + 1
2
>>> 2 + 2
4

```

> [!TIP]
> No código-fonte deste arquivo, as três crases ` ``` ` no início e
> palavra `python` fazem parte da sintaxe do Markdown para marcar
> um **bloco de código** a ser colorizado como Python.
> O que importa para o `doctest` é o texto entre o primeiro `>>>`
> e a linha em branco no final de cada bloco de código.

> [!WARNING]
> No final de cada bloco é preciso colocar uma linha em branco para
> indicar ao doctest que a saída esperada terminou, e ela não inclui
> o delimitador de blocos ` ``` ` do formato Markdown.

## Instruções de múltiplas linhas

Se for preciso usar instruções Python com várias linhas você
pode usar o sinal `...` no início da linha para indicar a continuação,
o mesmo que acontece automaticamente no console do Python.
Repare na indentação necessária:

```python
>>> for i in range(3):
...     print(i)
0
1
2

```

## Ignorar detalhes na saída

Algumas saídas geradas pelo Python podem conter detalhes irrelevantes
para o teste, tal como o endereço de uma função ou frações decimais
muito longas.

A forma mais fácil de evitar problemas é incluir a diretiva
`doctest: +ELLIPSIS` na expressão sob teste, e então usar `...`
na saída esperada para ignorar os detalhes:

```python
>>> def porcento(a, b):
...     return a * 100 / b
>>> porcento(1, 2)
50.0
>>> porcento(1, 3)  # doctest: +ELLIPSIS
33.33333...

```

Isso também é útil para abreviar saídas muito extensas.
Neste exemplo, coloque a diretiva `+ELLIPSIS` para que o teste passe:

```python
>>> list(range(100)) # doctest: +ELLIPSIS
[0, 1, 2, 3..., 98, 99]

```

Utilize a diretiva `+ELLIPSIS` e o sinal `...` para tornar este
teste mais robusto:

```python
>>> porcento # doctest: +ELLIPSIS
<function porcento at 0x7...490>

```

## Captura de exceções

Por padrão, o `doctest` ignora todas as linhas de um *traceback*
do Python, exceto a primeira e a última, então o teste a seguir
funciona mesmo sem usar `...`.

Mas a exceção e a mensagem de erro precisam ser exatamente
aquelas que o Python gera. Corrija este exemplo:

```python
>>> porcento(1, 0)
Traceback (most recent call last):
    (linhas aqui são ignoradas)
ZeroDivisionError: division by zero

```

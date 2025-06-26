# Explorando geradores

Isso é uma função geradora muito simples:

```python
>>> def gen_123(): # doctest: +ELLIPSIS
...     yield 1
...     yield 2
...     yield 3
...     yield 4

```

Execute este arquivo com `doctest -f` para explorar o funcionamento
desta função geradora.

Corrija passo a passo os testes com os resultados observados por você.

```python
>>> gen_123 # doctest: +ELLIPSIS
<function gen_123 at 0x7...490>

```

```python
>>> gen_123() # doctest: +ELLIPSIS
<generator object gen_123 at 0x7...570>

```

>>> for i in gen_123():
...     print(i + 10)
11
12
13
14

```

>>> list(gen_123())
[1, 2, 3, 4]

```

>>> set(gen_123()) == {4, 3, 2, 1}
True

```

> [!TIP]
> Note o truque do teste com `set`, para contornar o fato de que
> a ordem dos elementos do conjunto é imprevisível.
> A saída não necessariamente será na ordem `{1, 2, 3}`,
> mas a comparação será verdadeira se os elementos forem iguais
> nos dois conjuntos.

Agora vamos gerar alguns erros de propósito.
Sua tarefa é corrigir as saídas inclusive o 
texto correspondende de cada *traceback* para
documentar o comportamento do gerador.

```
>>> g = gen_123()
>>> next(g)
1

```

```
>>> next(g)
2

```

```
>>> next(g)
3

```

```
>>> next(g)
4

```

>>> a, b, c, d = gen_123()
>>> a, b, c, d
(1, 2, 3, 4)

>>> a, b, c, d = gen_123()

>>> a, b = gen_123()
Traceback (most recent call last):
    (linhas aqui são ignoradas)
ValueError: too many values to unpack (expected 2)

>>> a, *b = gen_123()
>>> a, b
(1, [2, 3, 4])

```



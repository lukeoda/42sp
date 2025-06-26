def gen_ABC():
    print('*** iniciando')

    print('*** produzindo A')
    yield 'A'

    print('*** produzindo B')
    yield 'B'

    print('*** produzindo C')
    yield 'C'

    print('*** terminando')

def main():
    try:
        g = gen_ABC()

        print(next(g))
        print(next(g))
        print(next(g))
        next(g)
    except StopIteration:
        pass


if __name__ == '__main__':
    main()


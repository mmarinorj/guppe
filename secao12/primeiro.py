
def funcao1():
    print('Geek University - primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('primeiro.py está sendo executado diretamente.')
    print(__name__)
else:                                          # normalmente  não utilizado. Feito para demonstrar a teoria na prática.
    print(f'primeiro.py foi importado. {__name__}')

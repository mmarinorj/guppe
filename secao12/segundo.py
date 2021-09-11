
import primeiro


def funcao2():
    primeiro.funcao1()


if __name__ == '__main__':
    funcao2()
    print('segundo.py está sendo executado diretamente.')
    print(__name__)
else:                                          # normalmente  não utilizado. Feito para demonstrar a teoria na prática.
    print(f'segundo.py foi importado. {__name__}')

"""
Funções de Maior Grandeza - Higher Order Function - HOF

O que isso significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como
 resultado ou mesmo que podemos passa funções com argumentos para outras funções e até mesmo criar variáveis do tipo
 de funções nos nossos programas.

 OBS: Na seção de funções, nós utilizamos isso.

 Em Python, as funções são Cidadãos de Primeira Classe, First Citzen.
"""


# # Exemplo - Definindo as funções
#
# def somar(a, b):
#     return a + b
#
#
# def diminuir(a, b):
#     return a - b
#
#
# def multiplicar(a, b):
#     return a * b
#
#
# def dividir(a, b):
#     return a / b
#
#
# def calcular(num1, num2, funcao):
#     return funcao(num1, num2)
#
#
# print(calcular(4, 3, somar))
# print(calcular(4, 3, diminuir))
# print(calcular(4, 3, multiplicar))
# print(calcular(4, 3, dividir))

"""
Em Python podemos ter funções dentro de funções, que são conhecidas por Nested Functions ou Inner Functions - Funções
Internas
"""

# # Nested Functions - Funções Aninhadas
#
# from random import choice
#
#
# def cumprimento(pessoa):
#     def humor():
#         return choice(('E aí ', 'Suma daqui ', 'Gosto muito de você '))
#     return humor() + pessoa
#
#
# print(cumprimento('Marcelo'))
# print(cumprimento('Marcelo'))


# # Retornando funções de outras funções
#
# from random import choice
#
# def faz_me_rir():
#     def rir():
#         return choice(('hahahahahahaha', 'kkkkkkkkkkkk', 'yayayayayayaayayaya'))
#     return rir
#
#
# rindo = faz_me_rir()
# print(rindo())


# Inner Functions (Funções internas / Nested Functions) podem acessar o escopo de funções mais externas.

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'lololololo', 'kkkkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Fernanda')
print(rindo())
print(rindo())
print(rindo())



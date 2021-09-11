"""
Estruturas lógicas: and, or, not, is

Operadores unários:
    - not
Operadores binários:
    - and, or, is

para o 'and', ambos os valores precisam ser True
para o 'or', apenas um precisa ser True
para o 'not', o valor do booleano é invertido, ou seja, se for True vira False e s e for False vira True
para o 'is', o valor se confirma. Não é muito usado pois causa redundância, já que se não colocar o NOT,
já é uma confirmação. Pode tb substituir o '=='
"""

ativo = False
logado = True

if ativo:
    print('Usuário ativo no sistema')

if ativo and logado:
    print('com AND no IF Bem vindo usuário!')
else:
    print('com AND no ELSE Você precisa ativar sua conta. Por favor, cheque seu e-mail')

if ativo or logado:
    print('com OR no IF Bem vindo usuário!')
else:
    print('com OR no ELSE Você precisa ativar sua conta. Por favor, cheque seu e-mail')

if not ativo:
    print('com NOT no IF Você precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    print('com NOT no ELSE Bem vindo usuário!')

print(ativo is True)

user = 'Marcelo Marino'
if user is 'Marcelo Marino':
    print('Marcelo')
else:
    print('Não é Marcelo')

print(user is 'Marcelo Marino')


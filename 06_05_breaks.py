"""
Saindo de loops com break.

Funciona da mesma forma que nas linguagens C ou Java

Utilizamos os breaks pra sair de loops de maneira projetada.
"""

# Exemplo 1
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero, end=' ')
print('\nSai do Loop')

# Exemplo 2
while True:
    comando = input('Digite sair para sair: ')
    if comando == 'sair':
        break

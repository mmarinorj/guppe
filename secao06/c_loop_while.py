"""
Loop while

while expressao_booleana:
    #execução do loop
O bloco sera repetido enquanto a expressão booleana for verdadeira
Expressão booleana é toda aquela onde o resultado for True ou False
É muito importante que cuidemos do critério de parada para não causar um loop infinito desnecessário.
"""

# Exemplo 1
numero = 1
while numero < 10:
    print(numero, end=', ')
    numero += 1

# Exemplo 2
resposta = ''
while resposta != 'sim':
    resposta = input('\nJá acabou Jéssica? ')

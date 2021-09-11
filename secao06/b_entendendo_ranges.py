"""
Ranges

- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

Formas gerais:
# Forma 1
range(valor_de_parada)
OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Forma 2
range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

# Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Forma 4 (Inversa)
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo NEGATIVO especificado pelo usuário)
mas decrescente
"""

# Forma 1
print('\n')
for num in range(11):
    print(num, end=' ')

# Forma 2
print('\n')
for num in range(2, 11):
    print(num, end=' ')

# Forma 3
print('\n')
for num in range(5, 101, 5):
    print(num, end=' ')

# Forma 4
print('\n')
for num in range(10, -1, -1):
    print(num, end=' ')

"""
Loop for

Loop -> Estrutura de repetição.
for -> Uma dessas estruturas

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
ex: - String (nome = 'Marcelo Marino')
    - Lista (lista = [1, 2, 3, 4, 5]
    - Range (numeros = range(1, 10)) => onde range(valor_inicial, valor_final(-1)) => 1, 2, 3, 4, 5, 6, 7, 8, 9

"""
nome = 'Marcelo Marino'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 11)     # Temos que transformar em lista

print("\n")
for letra in nome:
    print(letra)

print("\n")
for numero in lista:
    print(numero)

print("\n")
for i in range(1, 11):
    print(f'numero {i}')

print("\n")
for indice, letra in enumerate(nome):
    print(nome[indice])
# ou
print("\n")
for indice, letra in enumerate(nome):
    print(letra)

print("\n")
for _, letra in enumerate(nome):   #qdo não precisamos de um valor, descartamos com um underline (_)
    print(letra)

print("\n")
for valor in enumerate(nome):
    print(valor)

print("\n")
for valor in enumerate(nome):
    print(valor[0])

print("\n")
for valor in enumerate(nome):
    print(valor[1])

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    print(f'imprimindo {n}')

for n in range(1, qtd+1):
    num = int(input(f'Informe o valor {n}/{qtd}: '))
    soma += num
print(f'A soma é {soma}')

print("\n")
for letra in nome:
    print(letra, end='')  # esse end quebra o padrão do print de pular uma linha a cada impressão

# Original: U+1F60D
# Modificado: U0001F60D
emoji = 'U0001F60D'
print("\n")
for _ in range(3):
    for num in range(1, 18):
        print('\U0001F605' * num)


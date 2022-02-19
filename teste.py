from metodo import repetidos, Lista


letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(repetidos(letras, ['a', 'g', 'o']))
print(repetidos(letras, 'g'))
print(repetidos(numeros, 5))
print(repetidos(numeros, [1, 3, 5, 10, 22, 55, 4, 2, 89]))

print(40 * '#')
print(Lista(letras, ['a', 'g', 'o']).repetidos2())
print(Lista(letras, 'g').repetidos2())
print(Lista(numeros, 5).repetidos2())
print(Lista(numeros, [1, 3, 5, 10, 22, 55, 4, 2, 89]).repetidos2())

"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.
Existem duas diferenças básicas:
1 - As tuplas são representadas por parenteses ()
2 - As tuplas são imutáveis, isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera
uma nova tupla

OBS: Métodos de adição e remoção de elementos nas tuplas não existem pois elas são imutáveis.
Dicas na utilização das tuplas:
- Utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma seleção
Ex1:
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro' 'outubro', 'novembro', 'dezembro')
- Tuplas são mais rápidas que listas;
- Deixam seu código mais seguro, pois trabalhar com elementos imutáveis traz segurança para o código.

"""

# ATENÇÃO 1 - As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# ATENÇÃO 2 - Tuplas com 1 elemento

tupla3 = (4)     # Isso não é uma tupla, é um int
print(tupla3)
print(type(tupla3))

tupla4 = (4,)    # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4,      # Isso é uma tupla
print(tupla5)
print(type(tupla5))

### CONCLUSÃO: Podemos concluir que as tuplas são definidas pela vírgula e não pelo uso de parênteses ###

###### range ###### - Gerar uma tupla dinamicamente com o range(início, fim, passo)
tupla6 = tuple(range(11))
print(tupla6)
print(type(tupla6))
print(tupla6.index(0))

###### Desempacotamento de tupla ###### - colocar número de objetos diferentes para desempacotar gera erro.
tupla7 = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla7

print(escola)
print(curso)


###### soma*, Valor Máximo*, Valor mínimo* e Tamanho ###### - apenas se os valores forem inteiros ou naturais,
# exceto o tamanho que vale qq valor.
tupla8 = (1, 2, 3, 4, 5, 6)
print(sum(tupla8))
print(max(tupla8))
print(min(tupla8))
print(len(tupla8))

###### Concatenação de tuplas ######
tupla9 = (1, 2, 3)
print(tupla9)

tupla10 = (4, 5, 6)
print(tupla10)

print(tupla9 + tupla10)      # tuplas são imutáveis
print(tupla9)
print(tupla10)

tupla11 = tupla9 + tupla10
print(tupla11)
print(tupla9)
print(tupla10)

tupla9 = tupla9 + tupla10    # tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla9)

# Acesso a elementos em uma tupla
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses[5])

# Verificando se determinado elemento está contido na tupla
tupla12 = (1, 2, 3)
print(3 in tupla12)

# Iterando sobre uma tupla
for n in tupla12:
    print(n)

for indice, valor in enumerate(meses):
    print(indice, valor)

i = 0
while i < len(meses):
    print(meses[i])
    i += 1

print(meses.index('agosto'))

# Contando elementos dentro de uma tupla
tupla13 = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla13.count('a'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))

# Slicing
# tupla[inicio:fim:passo]
print(meses[0:])
print(meses[:8])
print(meses[::-1])
print(meses[::2])
print(meses[::6])
print(meses[::12])
print(meses[5:8])

# Copiando uma tupla para outra
tupla14 = (1, 2, 3)
print(tupla14)

nova = tupla14
print(tupla14)
print(nova)

outra = (4, 5, 6)

nova += outra

print(tupla14)
print(nova)
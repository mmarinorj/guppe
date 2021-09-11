"""
Listas (list)

Listas em Python funcionam como vetores/matrizes (arrays) com a diferença de serem DINÂMICO e
também de podermos colocar QUALQUER tipo de dado.

- Dinâmico: Não possuem tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')
lista7 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]

# Podemos facilmente checar se determinado valor está contido na lista
num = 25
nom = 'e'
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

if nom in lista5:
    print(f'Encontrei a letra {nom}')
else:
    print(f'Não encontrei a letra {nom}')

###### sort ###### - Ordenar uma lista
lista1.sort()
print(lista1)
lista5.sort()
print(lista5)

###### count ###### - Contar numero de ocorrências de um valor
print(lista1.count(1))
print(lista5.count('e'))

###### append ###### - Adicionar elementos em listas (1 por vez) - cada elemento adicionado, sendo único ou em lista,
# entrará como um objeto. Se for uma lista, entrará como "lista dentro de lista".
lista1.append(42)
print(lista1)
lista1.append([8, 29, 33])
print(lista1)
num = 29
nom = 'e'
if num in lista1:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

###### extend ###### - Adicionar elementos em listas (vários em forma de |lista ou string| de uma vez)
# Podemos também usar o '+' para somar duas listas
lista1.extend([8, 29, 33])
print(lista1)
lista1.extend([77])
print(lista1)
num = 29
nom = 'e'
if num in lista1:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

###### insert ###### - Adicionar elementos em listas informando posição do índice
lista1.insert(2, 'novo valor')
print(lista1)

###### reverse ###### - Inverte uma lista
lista1.reverse()
print(lista1)
print(lista2[::-1])   # Outra maneira de inverter listas e Strings sem modificá-las (método slice)

###### copy ###### - Copia uma lista
lista6 = lista2.copy()
print(lista6)
lista7 = lista2     # para listas, essa forma não é boa. Ver explicação no final do arquivo.
print(lista7)

###### len ###### - Retorna o tamanho da lista (quantidade de elementos dentro da lista)
print(len(lista1))
print(len(lista2))
print(len(lista3))
print(len(lista4))
print(len(lista5))
print(len(list('Marcelo')))

##### pop ##### - Por padrão, remove o último elemento de uma lista podendo retorná-lo.
# Podemos tb especificar um índice para ser removido
print(lista5)
print(lista5.pop())
print(lista5)
print(lista5.pop(3))
print(lista5)

##### clear ##### - Limpar a lista completamente
print(lista5)
lista5.clear()
print(lista5)

##### * ##### - Repetir todos os elementos de uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

##### split ##### - Converter string para lista separando os ítens pelo espaço (por padrão).
# Vc pode definir o elemento que vai ser o separador
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)
curso1 = 'Programação, em, Python: ,Essencial'
print(curso1)
curso1 = curso1.split(',')
print(curso1)

##### join ##### - Converter lista para string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)
curso2 = ' '.join(lista6)
print(curso2)

curso2 = '$'.join(lista6)
print(curso2)

##### Iterando sobre listas #####
# com FOR
for elemento in lista1:
    print(elemento, end=' ')
print()

soma = 0
for elemento2 in lista4:
    print(elemento2, end=' ')
    soma += elemento2
print('\n', soma)

soma2 = ''
for elemento3 in lista2:
    print(elemento3, end=' ')
    soma2 += elemento3
print('\n', soma2)

# com WHILE
carrinho = []
produto = ''
while produto != 'sair':
    produto = input('Adicione um produto na lista ou digite "sair" para sair do programa: ')
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

###### Utilizando variáveis em listas ######
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

###### Acessando elementos de forma indexada ######
#           0         1        2         3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# de forma inversa
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

for indice, cor in enumerate(cores):
    print(indice, cor)

###### index ###### - Descobrir o índice de um item da lista
lista8 = [5, 6, 7, 5, 8, 9, 10]

# em qual índice da lista está o valor 6?
print(lista8.index(6))

# em qual índice da lista está o valor 9?
print(lista8.index(9))

# numeros duplicados ele retorna o indice do primeiro da lista.
print(lista8.index(5))

# podemos usar o recurso de ele pular o primeiro indice
print(lista8.index(5, 1))   # busca o próximo cinco a partir do indice 1, já que o primeiro 5 está no indice 0
print(lista8.index(5, 2))
print(lista8.index(5, 3))

# podemos buscar dentro de um range
print(lista8.index(8, 3, 6))    #busca o índice do valor 8, entre os índices 3 e 6 da lista

###### Revisão Slicing ######

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com parâmetro 'início'
lista9 = [1, 2, 3, 4]

print(lista9[1:])         # Iniciando do índice 1 e pegando todos os elementos restantes
print(lista9[:3])         # Iniciando de zero até o índice 3-1
print(lista9[1:3])        # Iniciando do índice 1 até o índice 3-1
print(lista9[::-1])       # invertendo a ordem da lista inteira
print(lista9[3:1:-1])     # Iniciando do índice 3 até o índice 1 -(-1) = 2

###### reverse ######
meu_nome = ['Marcelo', 'Marino']
meu_nome.reverse()
print(meu_nome)
meu_nome[0], meu_nome[1] = meu_nome[1], meu_nome[0]
print(meu_nome)

###### Soma, Valor Máximo, Valor Mínimo, Tamanho ######

# Se os valores forem todos inteiros ou reais
lista10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(lista10))    # SOMA
print(max(lista10))    # MÁXIMO VALOR
print(min(lista10))    # MÍNIMO VALOR

# Qualquer tipo de dado
print(len(lista10))    # TAMANHO DA LISTA

###### Transformar uma lista em TUPLA ######
lista11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista11)
print(type(lista11))
tupla = tuple(lista11)
print(tupla)
print(type(tupla))

###### desempacotamento de lista ######
# mais elementos para desempacotar do que variáveis para receber valores ou vice-versa, dará erro.
lista12 = [1, 2, 3]

num1, num2, num3 = lista12

print(num1)
print(num2)
print(num3)

###### Shallow Copy e Deep Copy ###### - copiando uma lista para outra
### Deep Copy ###
lista13 = [1, 2, 3]
print(lista13)

nova = lista13.copy()
print(nova)

nova.append(4)

print(lista13)
print(nova)

# Ao copiar a lista utilizando nome_da_lista.copy() as listas ficam totalmente independentes.
# A modificação da cópia não afeta a original. Em Python chamamos isso de DEEP COPY (cópia profunda).

### Shallow Copy ###
lista14 = [1, 2, 3]
print(lista14)

nova2 = lista14    # cópia
print(nova2)

nova2.append(4)

print(lista14)
print(nova2)

# Ao copiar a lista utilizando a atribuição vc simplesmente aponta a nova variável para o objeto que o originou.
# Qualquer modificação na cópia altera a original e vice-versa. Em Python chamamos isso de SHALLOW COPY.

import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
print(c)

# Usando operações normais de atribuição para copiar:
d = c

print(id(c) == id(d))                # True - d é o mesmo objeto que c
print(id(c[0]) == id(d[0]), '\n')    # True - d[0] é o mesmo objeto que c[0]

# Usando uma cópia superficial (.copy() nativo):
d = c.copy()

print(id(c) == id(d))                # False - d é agora um novo objeto
print(id(c[0]) == id(d[0]), '\n')    # True - d[0] é o mesmo objeto que c[0]

#### Usando a biblioteca copy ####
# Usando uma cópia superficial:
d = copy.copy(c)

print(id(c) == id(d))                # False - d é agora um novo objeto
print(id(c[0]) == id(d[0]), '\n')    # True - d[0] é o mesmo objeto que c[0]

# Usando uma cópia profunda:
d = copy.deepcopy(c)

print(id(c) == id(d))                # False - d é agora um novo objeto
print(id(c[0]) == id(d[0]), '\n')    # False - d[0] é agora um novo objeto

#### shift #### - Uma função para criar o shift que não existe de forma nativa no Python
def shift(l, n):
    return l[n:] + l[:n]
lista = [1, 2, 3, 4, 5]
print(shift(lista, 1))




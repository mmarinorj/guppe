"""
Dicionários (dict)

OBS: Em algumas linguagens de programação os dicionários são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por {}.

Chave e valor são separados por dois pontos (:) -> {'chave': 'valor'};
Ambos podem ser de qualquer tipo de dado;
Podemos misturar tipos de dados.
"""
print(type({}))

###### Criação de dicionários ######
# Forma 1
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

###### Acessando elementos ######
# Forma 1 - Acessando via chave
print(paises['br'])
print(paises['py'])
# print(paises['ru'])    # Quando não tem, dá erro: KeyError

# Forma 2 - Acessando via get - Recomendada
print(paises.get('br'))
print(paises.get('ru'))  # Não dá erro. Retorna None ou
print(paises.get('ru', 'Não encontrado'))   # Dessa forma, ao invés de None ele imprime o que está no segundo "elemento"


pais = paises.get('br')
print(pais)
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

pais = paises.get('ru', 'não encontrado')
print(f'País {pais}')

# Verificando se determinada chave está contida no dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'br' in paises:
    print('Sim')
else:
    print('Não')

# Tulpas são bastante interessantes de serem utilizadas como chaves de dicionários, pois são imutáveis
localidades = {(35.0685, 39.7845): 'Escritório em Tokyo',
               (40.7128, 74.6659): 'Escritório em Nova York',
               (37.7748, 122.4897): 'Escritório em São Paulo'}

print(localidades)
print(type(localidades))

###### Adicionar elementos em um dicionário ######
# Forma 1 - Mais comum
receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

receita.update({'jun': 450})
print(receita)

###### Atualizando dados em um dicionário ######
# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# A forma de adicionar e alterar dados num dicionário são identicas, ou seja, não podemos ter chaves repetidas no dic.

###### Removendo dados de um dicionário ######
# forma 1 - Mais comum
receita.pop('mar')       # Diferente das listas que qdo não informado nada ele retira o último objeto da lista,
print(receita)           # em diconários tem sempre que ter a chave.

ret = receita.pop('mai')
print(ret)
print(receita)

# Forma 2
del receita['abr']
print(receita)

###### clear ###### - limpando um dicionário
d = dict(a=1, b=2, c=3)
print(d)
print((type(d)))

d.clear()
print(d)

###### copy ###### - compiando um dicionário
# Forma 1 - Shallow Copy
d = dict(a=1, b=2, c=3)
novo = d.copy()
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma 2 - Atribuição
d = dict(a=1, b=2, c=3)
novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)

import copy

a = {'a': 1, 'b': 2, 'c': 3}
b = {'d': 4, 'e': 5, 'f': 6}
c = {'lista1': a, 'lista2': b}
print(c)

# Usando operações normais de ATRIBUIÇÃO para copiar:
d = c
print(d)

print(id(c) == id(d))                              # True - d é o mesmo objeto que c
print(id(c['lista1']) == id(d['lista1']), '\n')    # True - d['lista1'] é o mesmo objeto que c['lista1']

# Usando uma cópia superficial (.copy() nativo):   #SHALLOW COPY
d = c.copy()

print(id(c) == id(d))                              # False - d é agora um novo objeto
print(id(c['lista1']) == id(d['lista1']), '\n')    # True - d['lista1'] é o mesmo objeto que c['lista1']

#### Usando a biblioteca copy ####
# Usando uma cópia superficial:                    SHALLOW COPY
d = copy.copy(c)

print(id(c) == id(d))                              # False - d é agora um novo objeto
print(id(c['lista1']) == id(d['lista1']), '\n')    # True - d['lista1'] é o mesmo objeto que c['lista1']

# Usando uma cópia profunda:                       # DEEP COPY
d = copy.deepcopy(c)

print(id(c) == id(d))                              # False - d é agora um novo objeto
print(id(c['lista1']) == id(d['lista1']), '\n')    # False - d['lista1'] é agora um novo objeto

###### fromkeys ###### - outra forma de criar um dicionário não muito usada
# recebe dois parâmetros: um iterável e um valor.
# Para cada valor do iterável ele cria uma chave e atribui o valor informado na segunda posição
outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)

veja = {}.fromkeys('teste', 'valor')        # uma string é um iterável. Por isso ele usa cada letra como chave
print(veja)                                 # não repete 't' e 'e'

nova = {}.fromkeys(range(1, 11), 'novo')
print(nova)


"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.
"""
# Bibilioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean() -> média, da biblioteca statistics
media = statistics.mean(dados)
print(f'Média: {media}')

# OBS: Assim como a funcão map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(res)
print(type(res))
print(list(res))
print(list(res))                                 #-> assim como no map(), depois da primeira utilização do resultado
res = filter(lambda x: x < media, dados)         # de filter(), ele zera.
print(list(res))

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
res1 = list(filter(None, paises))
res2 = list(filter(lambda x: x != '', paises))

print(res1)
print(res2)

# A diferenca entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento
# do iterável. As funções retornam um valor não booleano.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de
# acordo com a função. As funções retornam sempre um valor booleano (True ou False)

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje", "Eu adoro passear"]},
    {"username": "gal", "tweets": []}
]
print(usuarios)
print(usuarios[0]['tweets'])
res4 = list(filter(lambda n: n['tweets'] == [], usuarios))
print(res4)

# ou

res5 = list(filter(lambda n: not n['tweets'], usuarios))
print(res5)

# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

res6 = list(map(lambda n: f'Sua instrutora é {n}', filter(lambda n: len(n) < 5, nomes)))
print(res6)


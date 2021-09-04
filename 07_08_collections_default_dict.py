"""
Módulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será attribuído.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar valores.
"""
# # Recap Dicionários
#
# dicionario = {'curso': 'Programação em Python: Essencial'}
#
# print(dicionario)
#
# print(dicionario['curso'])
#
# print(dicionario['outro'])  # ??? KeyError

# Fazendo import
from collections import defaultdict
dicionario = defaultdict(lambda: 0)
print(dicionario)

dicionario['curso'] = "Programação em Python: Essencial"

print(dicionario['curso'])

print(dicionario)

print(dicionario['outro'])

print(dicionario)




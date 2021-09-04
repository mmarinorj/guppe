"""
Mapas (map) -> Conhecidos em Python como dicionários

Dicionários em Python são representados por {}
"""
receita = {'jan': 500, 'fev': 250, 'mar': 400}
print(receita)

# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

###### keys ###### - Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

###### values ###### - Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

###### items ######
print(receita.items())

for chave, valor in receita.items():
    print(f'Chave={chave} e Valor={valor}')

###### Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * se os valores forem inteiros ou reais
print(sum(receita.values()))
print(max(receita.items()))
print(max(receita.values()))
print(min(receita.items()))
print(min(receita.values()))
print(len(receita))
testando = max(receita.items())
print(testando[0])




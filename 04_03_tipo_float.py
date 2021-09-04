"""
Tipo Float
Tipo real, decimal, casas decimais

OBS: separador de casas decimais é o . A vírgula é separador de milhares
"""

# valor = 1,44  #==> Errado

valor1 = 1, 44 # => tupla (1, 44)


valor2 = 1.44 # => float (1.44)
print(valor1, valor2)

# é possível fazer dupla atribuição

valor3, valor4 = 1, 44
print(valor3)
print(valor4)

# podemos converter de float pra int ( e vice-versa) mas perdemos as casas decimais na conversão
float_int = int(valor2)
print(float_int)
int_float = (float(float_int))
print(int_float)

# podemos trabalhar com números complexos colocando o j após o número
variavel = 5j
print(variavel)
print(type(variavel))
print(variavel**2)




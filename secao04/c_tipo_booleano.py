"""
Tipo Booleano

Álgebra Booleana, criada por George Boole
2 constantes, verdadeiro e falso
True -> Verdadeiro
False -> Falso
sempre com as iniciais maiúsculas
"""

ativo = True
print(ativo)

"""
Operações básicas:
"""
#  Negação (not):
print(not ativo)

logado = True

#  Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou o outro deve ser verdadeiro
True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros
True or True -> True
True or False -> False
False or True -> False
False or False -> False
"""
print(ativo and logado)
print(type(ativo and logado))



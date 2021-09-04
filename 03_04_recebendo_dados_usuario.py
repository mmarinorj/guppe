"""
Recebendo dados do Usuário
"""

print("Qual o seu nome? ")
nome = input()

print("Seja bem-vindo(a) %s" % nome)

print("Qual sua idade?" )
idade = input()

print("%s tem %s anos." % (nome, idade)) #Exemplo de print antigo. versões 2.x

print("{0} tem {1} anos.".format(nome, idade)) #Exemplo de print das versões 3.x

print(f"{nome} tem {idade} anos") #Forma mais atual.
print(f"{nome} nasceu em {2021 - int(idade)}")

nome = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))
print(f"{nome} tem {idade} anos") #Forma mais atual.
print(f"{nome} nasceu em {2021 - idade}")


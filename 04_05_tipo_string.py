"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:
- Estiver entre aspas simples -> 'uma string' , '234' , 'a' , 'True' , '42.3'
- Estiver entre aspas duplas -> "uma string" , "234" , "a" , "True" , "42.3"
- Estiver entre aspas simples triplas -> '''uma string''' , '''234''' , '''a''' , '''True''' , '''42.3'''
"""
# - Estiver entre aspas duplas -> """uma string""" , """234""" , """a""" , """True""" , """42.3"""


nome1 = 'Marcelo Marino'
nome2 = "Marcelo Marino"
nome3 = '''Marcelo Marino'''
nome4 = """Marcelo Marino"""

print(nome1)
print(type(nome1))
print(nome2)
print(type(nome2))
print(nome3)
print(type(nome3))
print(nome4)
print(type(nome4))

# Quando usar cada uma?
# O mais usado é aspas simples;
# Se o nome tiver apóstrofo, tem que usar aspas duplas para não dar erro;
# Aspas triplicadas, simples ou duplas é melhor para digitar string de várias linhas;

print(nome1.upper())
print(nome2.lower())
print(nome3.title())
print(nome4.split())
print(nome4.split()[0])
print(nome2[2])
print(nome1[::-1])   # inversão da string, modo Pythônico
print(nome1[8])      # Slice de string

print(nome2.replace('M', 'V'))
print('amor')
print('amor'[::-1])
print('socorram me subino onibus em marrocos')         # Palíndromo - Qdo inverte é a mesma coisa
print('socorram me subino onibus em marrocos'[::-1])
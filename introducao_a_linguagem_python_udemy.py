
a = "Olá Marcelo!"
b = "Outra mensagem"
d = "O rato roeu a roupa do rei de Roma"
lista_d = d.split()

print(a)
print(b)
concatenar = a + " " + b + "\n"

print(concatenar)
print(concatenar.lower()) #.lower() => coloca todos os caracteres em letras minúsculas
print(concatenar.upper()) #.upper() => COLOCA TODOS OS CARACTERES EM LETRAS MAIÚSCULAS
print(concatenar.strip()) #.strip() => remove caracteres especiais do início e do final da String (por ex.: ' ' ou '\n')
print(lista_d)
print(d.split("r"))       #.split() => faz uma lista a partir de uma string eliminando o caracter definido como "separador". Em branco, padrão => espaço é o "separador"
print(d.find("rei"))      #.find(letra ou palvra ou pedaço de palavra) => Informa a posição da letra ou primeira letra da "sub string" dentro da string. -1 indica que não achou o que se procurava.
busca = d.find("rei")
print(d[busca:])          #imprime a string d da definição da busca até o final (ou até a posição anterior ao caractere definido)
print(d[d.find("rei"):])
e = d.replace(d[d.find("do"):],"da rainha da Inglaterra") #.replace => troca caracter ou palavras de uma string informando o posicionamento com o .find
f = d.replace(d[20:],"de Marcelo Marino bonitão")
g = e.replace(e[30:],"do Zimbabuê")
print(e)
print(f)
print(g)

####FUNÇÃO####
c = 0
def soma(a,b):
	c = a + b
	print(c)

def subtracao(a,b):
	print(a - b)

def mult(a,b):
	return a * b

def div(a,b):
	return a / b

soma(10, 20)
subtracao(25, 10)
print(mult(5, 4))
print((div(21, 7)))
print(int((div(21, 7)))) #a divisão retorna um float então defini como integer pra retornar um inteiro
print(c)            #imprime o c definido no início do código e não o de dentro da função soma pois as variáveis definidas dentro de uma função tem um escopo local e não existem fora dela.

h = mult(25, 10)
i = div(25, 5)

print(int(div(h,i)))
print(div(mult(50,80),div(40,8)))
print(int(div(mult(50,80),div(40,8))))



####MAnipulando arquivos####
"""
- Usar o r ou nada pra ler um arquivo
- Usar w pra recriar um arquivo. (O conteúdo será apagado)
- Usar a pra adicionar linhas ao arquivo
- Sempre abrir, usar e fechar o arquivo se não dá erro.
"""

arquivo = open("/home/marcelo/Documentos/Python/marcelo.txt")
linhas = arquivo.readlines()
print(linhas)
for l in linhas:
	print(l)
arquivo.close()

arquivo = open("/home/marcelo/Documentos/Python/marcelo.txt")
texto_completo = arquivo.read()
print(texto_completo)
arquivo.close()

arquivo = open("/home/marcelo/Documentos/Python/marcelo.txt")
linha = arquivo.readline()
linha = arquivo.readline()
linha = arquivo.readline()
print(linha)
arquivo.close()

arquivo2 = open("/home/marcelo/Documentos/Python/marcelo_teste.txt","w")
arquivo2.write("Eu sei o que vocês fizeram no verão passado\nNão tentem me enganar!!!\n")
arquivo2.close()

arquivo2 = open("/home/marcelo/Documentos/Python/marcelo_teste.txt", "a")
for k in range(0,100):
	arquivo2.write("Eu sei o que vocês fizeram no verão passado\nNão tentem me enganar!!!\nVai Amarelar?\n")
arquivo2.close()

####LISTAS####

lista1 = ["abacaxi", "melancia", "abacate"]
lista2 = [1,2,3,4,5]
lista3 = ["abacaxi", 2, 9.98, True]

print(lista1)
print(lista1,lista2,lista3)
print("\n",lista1,"\n",lista2,"\n",lista3)
print(lista1[1],lista2[2],lista3[3])


for item in lista1:
	print(item)

for item in (lista1[2],lista2[2],lista3[2]):
	print(item)

for item in (lista1,lista2,lista3):
	print(item)

lista1_tamanho = len(lista1)
print(lista1_tamanho)

lista2_tamanho = len(lista2)
print(lista2_tamanho)

lista3_tamanho = len(lista3)
print(lista3_tamanho)

lista1.append("limao")
print(lista1)

if 8 in lista2:
	print("sim, está na lista")
else:
	print("não, não está na lista")

del lista2[2:4]
print(lista2)

del lista3[:]
print(lista3)

lista4 = [120, 89, 90, 54, 32, 44, 10, 9, 200, 8, 101]
lista4.reverse()
print(lista4)
lista4.sort()  #organiza modificando a lista original
print(lista4)
lista4.reverse()
print(lista4)

lista5 = [120, 89, 90, 54, 32, 44, 10, 9, 200, 8, 101]
lista6 = sorted(lista5) #organiza sem modificar a lista atual, adicionando nova lista organizada em uma nova variável
print(lista5,lista6)
lista5.sort(reverse = True)
print(lista5)

####Dicionários Python (um JSON no python é um dicionário)####

dic1 = {"A":"AMEIXA", "B":"BOLA","C":"CACHORRO"}
print(dic1)
print(dic1["A"])

for m in dic1:
	print(m)

for m in dic1:
	print(dic1[m])

for m in dic1:
	print(m + ":" + dic1[m])

for m in dic1.items():
	print(m)

for m in dic1.values():
	print(m)

for m in dic1.keys():
	print(m)

#####--Biblioteca RANDOM--#####

import random

num1 = random.randint(0,10) #número aleatório entre 0 e 10
print(num1)

random.seed(1)              #força sempre um mesmo número aleatório
num2 = random.randint(0,10) 
print(num2)

lista7 = [120, 89, 90, 54, 32, 44, 10, 9, 200, 8, 101]
num3 = random.choice(lista7) 
print(num3)

##### Tratamento de exceções #####

x = 2
y = 0

try:
	print(x/y)
except:
	print("Não é permitida a divisão por ZERO")

meu_nome = input("Diga seu nome: ")
numero_inteiro = int(input("Digite um numero inteiro: "))
numero_float = float(input("Informe um número racional: "))

print(meu_nome,numero_inteiro,numero_float)

##### List Comprehension ######

lista8 = [1,2,3,4,5]
lista9 = []

print("\nMétodo simples (comum) para definir lista9 como quadrado de lista8")
for i in lista8:
	lista9.append(i**2)
print(lista8)
print(lista9)

print("\nList Comprehension")
lista9 = [i**2 for i in lista8]
print(lista8)
print(lista9)

lista10 = [i for i in lista8 if i % 2 != 0]
print("\n")
print(lista10)

###### Função Enumerate ######
lista11 = ["abacate", "bola", "cachorro"]

print("\nmodo comum")
for i in range(len(lista11)):
	print(i, lista11[i])


print("\nmodo Pythonico")
for i, nome in enumerate(lista11):
	print(i, nome)

print("\n")
###### Função Map ######

def dobro(x):
	return x*2

valor = [1, 2, 3, 4, 5] 
print(dobro(valor))          #dobra a lista e não cada valor da lista

map_dobro = list(map(dobro, valor)) #usando o map, dobra cada valor da lista transformando o resultado em outra lista
print("\n")
print(map_dobro)

###### Função REDUCE #######

lista12 = [1, 3, 5, 10, 20]

def soma1(x, y):
	return x + y

from functools import reduce
soma2 = reduce(soma1, lista12)
print (soma2)

###### Função ZIP ######
lista13 = [1, 2, 3, 4, 5]
lista14 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista15 = ["verde","de futebol", "pitbull", "a rodo", "cor de rosa"]

for nume, nom, valori in zip(lista13, lista14, lista15):
	print(nume, nom, valori)
	print(valori, nume, nom)

for nume, nom, valori in zip(lista13, lista14, lista15):
	print(nume, nom, valori)

for nume, nom, valori in zip(lista13, lista14, lista15):
	print(valori, nume, nom)

##### Função FILTER ######

lista16 = [1,2,3,4,5,6,7,8,9,10]
lista17 = []

def pares2(x):
	if x % 2 == 0:
		return x
	   
print(pares2(2))

lista17 = list(filter(pares2, lista16))
print(lista17)

#### lambda #####

def funcao(n):
	return lambda a: a*n

num_dobro = funcao(2)
num_triplo = funcao(3)
num_quadruplo = funcao(4)
num_quintuplo = funcao(5)

print(num_dobro(34))
print(num_triplo(47))
print(num_quadruplo(51))
print(num_quintuplo(22))

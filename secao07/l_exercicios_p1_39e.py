###### Exercício 01 ######
A = []
i = 0
while i < 6:
    elem = int(input(f'Informe o número {i+1}/6 do vetor A: '))
    A.append(elem)
    i += 1
A1 = A[0] + A[1] + A[5]
# print(f'Soma dos elementos 0, 1 e 5 do vetor é {A1}')
elem = int(input('Vamos mudar o 5º elemento deste vetor? Que tal 100? Digite=> '))
A[4] = elem
for ind, n in enumerate(A):
    print(f'O valor do vetor A na posição {ind} é: {n}')
print('Fim do exercício 01')

###### Exercício 02 ######
lista = []
n = 0
while n < 6:
    temp = int(input(f'Entre com um número inteiro ({n+1}/6): '))
    lista.append(temp)
    n += 1
for i, val in enumerate(lista):
    print(f'O {i+1}º valor digitado foi {val}')
print('Fim do exercício 02')

###### Exercício 03 ######
lista = []
squad = []
cont = 0
while cont < 10:
    temp = float(input(f'Informe um número real {cont+1}/10: '))
    lista.append(temp)
    cont += 1
for i in lista:
    squad.append(i**2)
print(f'Números digitados: {lista}')
print(f'Quadrados destes números: {squad}')
print('\nFim do exercício 03')

###### Exercício 04 ######
lista = []
for n in range(8):
    temp = int(input(f'Informe um número ({n+1}/8): '))
    lista.append(temp)
n1 = int(input(f'\nInforme uma posição desse vetor 1/2: '))
n2 = int(input(f'Informe uma posição desse vetor 2/2: '))
soma = lista[n1] + lista[n2]
print(f'A soma entre os elementos {n1} e {n2} do vetor é {soma}')
print('\nFim do exercício 04')

###### Exercício 05 ######
lista = []
cont = 0
for i in range(10):
    temp = int(input(f'Informe o {i+1}º elemento do vetor de 10 posições: '))
    lista.append(temp)
    if temp % 2 == 0:
        cont += 1
print(f'\nO vetor digitado contem {cont} número(s) par(es)')
print('\nFim do exercício 05')

###### Exercício 06 ######
lista = []
cont = 0
temp = float(input(f'Informe um número 1/10: '))
maior = temp
menor = temp
for i in range(9):
    temp = float(input(f'Informe um número {i+2}/10: '))
    if temp > maior:
        maior = temp
    elif temp < menor:
        menor = temp
print(f'\nO menor número digitado foi o {menor:.0f};\nO maior número digitado foi o {maior:.0f}.')
print('\nFim do exercício 06')

###### Exercício 07 ######
lista = []
temp = int(input(f'Informe o número 1/10: '))
maior = temp
lista.append(temp)
cont = 0
for i in range(9):
    temp = int(input(f'Informe o número {i + 2}/10: '))
    lista.append(temp)
    if temp > maior:
        maior = temp
        cont += 1
print('\n', lista)
print(f'O maior elemento deste vetor é o {maior} e ele se encontra na posição {cont} do mesmo.')
print('\nFim do exercício 07')

###### Exercício 08 ######
lista = []
for i in range(6):
    temp = int(input(f'Informe o número {i+1}/6: '))
    lista.append(temp)
print(f'O vetor informado em sua ordem inversa é: {lista[::-1]}')
print('\nFim do exercício 08')

###### Exercício 09 ######
lista = []
contador = 0
while contador < 6:
    temp = int(input(f'Informe um valor par e positivo: '))
    if temp > 0 and temp % 2 == 0:
        lista.append(temp)
        contador += 1
    else:
        print('\nNúmero inválido!')
print(f'\nO vetor par digitado em ordem inversa é: {lista[::-1]}')
print('\nFim do exercício 09')

###### Exercício 10 ######
lista = []
contador = 1
soma = 0.0
while contador <= 15:
    temp = float(input(f'Informe a nota do {contador}º aluno (entre 0 e 10): '))
    if 10 >= temp >= 0:
        lista.append(temp)
        contador += 1
        soma += temp
    else:
        print('\nNúmero inválido!')
contador = contador - 1
print(f'\nA média das notas desses 15 alunos é: {(soma/contador):.2f}')
print('\nFim do exercício 10')

###### Exercício 11 ######
lista = []
contador = 0
soma = 0.0
neg = 0
while contador < 10:
    temp = float(input(f'Informe o {contador + 1}º número: '))
    lista.append(temp)
    if temp > 0:
        soma += temp
    elif temp < 0:
        neg += 1
    contador += 1
print(f'\nO vetor digitado contem 10 números sendo {neg} negativo(s).'
      f'\nA soma do(s) número(s) positivos do mesmo é {soma:,.2f}')
print('\nFim do exercício 11')

###### Exercício 12 ######
lista = []
for i in range(5):
    temp = float(input(f'Informe o {i + 1}º número: '))
    lista.append(temp)
print(f'\nOs números ditados foram: {lista}')
print(f'O maior número digitado: {max(lista):,.2f}')
print(f'O menor número digitado: {min(lista):,.2f}')
print(f'A média dos número digitados: {(sum(lista)/len(lista)):,.2f}')
print('\nFim do exercício 12')

###### Exercício 13 ######
lista = []
for i in range(5):
    temp = float(input(f'Informe o {i + 1}º número: '))
    lista.append(temp)
print(f'Posição do maior número digitado: {lista.index(max(lista)):}')
print(f'Posição do menor número digitado: {lista.index(min(lista)):}')
print('\nFim do exercício 13')

###### Exercício 14 ######
from collections import Counter
lista = []
for i in range(10):
    temp = float(input(f'Informe o {i + 1}º número: '))
    lista.append(temp)
resp = Counter(lista)
for i, valor in resp.items():
    if valor > 1:
        print(f'O número {i} aparece {valor} vezes no vetor digitado')
print(resp)
print('\nFim do exercício 14')

###### Exercício 15 ######
lista = []
for i in range(20):
    temp = int(input(f'Informe o {i + 1}º número: '))
    lista.append(temp)
resp = set(lista)
print(lista)
print(resp)
print('\nFim do exercício 15')

###### Exercício 16 ######
lista = []
for i in range(5):
    temp = int(input(f'Informe o {i + 1}º número: '))
    lista.append(temp)
codigo = float(input(f'\nDigite um código:\n(1)Mostrar o vetor na ordem direta\n(2)Mostrar o vetor na ordem inversa\n'
                     f'(0)Sair do programa '))
while codigo != 0:
    if codigo == 1 or codigo == 2:
        if codigo == 1:
            print(lista)
            codigo = float(input(f'\nDigite um código:\n(1)Mostrar o vetor na ordem direta\n'
                                 f'(2)Mostrar o vetor na ordem inversa\n(0)Sair do programa '))
        else:
            print(lista[::-1])
            codigo = float(input(f'\nDigite um código:\n(1)Mostrar o vetor na ordem direta\n'
                                 f'(2)Mostrar o vetor na ordem inversa\n(0)Sair do programa '))
    else:
        print('Código inválido!')
        codigo = float(input(f'\nDigite um código:\n(1)Mostrar o vetor na ordem direta\n'
                             f'(2)Mostrar o vetor na ordem inversa\n(0)Sair do programa '))
print('\nPrograma encerrado pelo usuário.')
print('\nFim do exercício 16')

###### Exercício 17 ######
lista = []
for i in range(10):
    temp = int(input(f'Informe o {i+1}º número: '))
    if temp < 0:
        lista.append(0)
    else:
        lista.append(temp)
print('\n', lista)
print('\nFim do exercício 17')

###### Exercício 18 ######
lista = []
ctrl = 0
for i in range(10):
    temp = int(input(f'Informe o {i+1}º número: '))
    lista.append(temp)
x = int(input(f'Informe um número inteiro e positivo: '))
print(f'\nMultiplos de {x} no vetor {lista}:')
for n in lista:
    if n % x == 0:
        print(f'{n}')
        ctrl += 1
if ctrl == 0:
    print(f'Não existem múltiplos de {x} neste vetor.')
print('\nFim do exercício 18')

###### Exercício 19 ######
lista = []
for i in range(50):
    lista.append((i+5*i) % (i+1))
print(f'\nVetor com {len(lista)} números = {lista}')
print('\nFim do exercício 19')

######Exercício 20 ######
lista = []
impares = []
ctrl = 1
temp = int(input(f'Informe o {ctrl}º número entre 0 e 50: '))
while ctrl <= 10:
    if 0 <= temp <= 50:
        lista.append(temp)
        ctrl += 1
        if temp % 2 == 1:
            impares.append(temp)
        if ctrl < 11:
            temp = int(input(f'Informe o {ctrl}º número entre 0 e 50: '))
    else:
        print('Número fora do intervalo pré-definido.')
        temp = int(input(f'Informe o {ctrl}º número entre 0 e 50: '))
print(f'\nVetor com {len(lista)} posições = {lista}\nÍmpares do vetor acima = {impares}')
print('\nFim do exercício 20')

###### Exercício 21 ######
A = []
B = []
C = []
for i in range(10):
    temp = int(input(f'Informe o número {i+1}/10 do vetor A: '))
    A.append(temp)
print()
for n in range(10):
    temp = int(input(f'Informe o número {n+1}/10 do vetor B: '))
    B.append(temp)
for m in range(10):
    C.append(A[m] - B[m])
print(f'\nVetor C: {C} (C = A - B)')
print('\nFim do exercício 21')

###### Exercício 22 ######
lista1 = []
lista2 = []
lista3 = []
cont1 = 0
cont2 = 0
for i in range(10):
    temp = int(input(f'Informe o número {i+1}/10 do vetor 1: '))
    lista1.append(temp)
print()
for n in range(10):
    temp = int(input(f'Informe o número {n+1}/10 do vetor 2: '))
    lista2.append(temp)
for m in range(20):
    if m % 2 == 0:
        lista3.append(lista1[cont1])
        cont1 += 1
    else:
        lista3.append(lista2[cont2])
        cont2 += 1
print('\n', lista3)
print('\nFim do exercício 22')

###### Exercício 23 ######
x = []
y = []
pe = 0

for i in range(5):
    temp = int(input(f'Informe o número {i+1}/5 do vetor X: '))
    x.append(temp)
print()
for n in range(5):
    temp = int(input(f'Informe o número {n+1}/5 do vetor Y: '))
    y.append(temp)
for m in range(5):
    pe += x[m]*y[m]
print()
print(x)
print(y)
print(f'O Produto Escalar entre os dois conjuntos acima é: {pe}')
print('\nFim do exercício 23')

###### Exercício 24 ######
alunos = {}
num = int(input(f'Informe o número do 1º aluno: '))
altura = float(input(f'Informe a altura em metros do 1º aluno: '))
alunos[num] = altura
maior = altura
menor = altura
cont1 = num
cont2 = num
for i in range(2, 11):
    num = int(input(f'Informe o número do {i}º aluno: '))
    altura = float(input(f'Informe a altura em metros do {i}º aluno: '))
    alunos[num] = altura
    if altura > maior:
        maior = altura
        cont1 = num
    elif altura < menor:
        menor = altura
        cont2 = num
print(f'\n{alunos}')
print(f'Aluno mais alto: nº {cont1:.0f} altura:{maior:.2f}\nAluno mais baixo: nº {cont2:.0f} altura:{menor:.2f}')
print('\nFim do exercício 24')

###### Exercício 25 ######
lista = []
cont = 0
ctrl = 0
while ctrl < 100:
    if cont % 7 == 0 or cont % 10 == 7:
        pass
    else:
        lista.append(cont)
        ctrl += 1
    cont += 1
print(f'O vetor de {len(lista)} posições é:\n{lista}')
print('\nFim do exercício 25')

###### Exercício 26 ######
v = []
n = 10
somat = 0
for i in range(1, n+1):
    temp = int(input(f'Informe o {i}º número: '))
    v.append(temp)
m = sum(v)/n
for i in range(0, n):
    somat += (v[i]-m)**2
dp = ((1/(n-1))*somat)**0.5
print(f'O desvio padrão do vetor {v} é: {dp:.6f}')
print('\nFim do exercício 26')

###### Exercício 27 ######
lista = []
for i in range(10):
    temp = int(input(f'Informe o {i+1}º número: '))
    lista.append(temp)
print(f'\nOs números primos do vetor {lista} são:')
for i, v in enumerate(lista):
    cont = 0
    for l in range(2, v+1):
        if v > 1 and v % l == 0:
            cont += 1
    if cont == 1:
        print(f'Número {v} na posição {i}')
print('\nFim do exercício 27')

###### Exercício 28 ######
v = []
v1 = []
v2 = []
for i in range(10):
    temp = int(input(f'Informe o {i+1}º número: '))
    v.append(temp)
    if temp % 2 == 1:
        v1.append(temp)
    elif temp % 2 == 0:
        v2.append(temp)
print(f'\nV = {v}\nV1 = {v1}\nV2 = {v2}')
print('\nFim do exercício 28')

###### Exercício 29 ######
lista = []
pares = []
impares = []
for i in range(6):
    temp = int(input(f'Informe o {i+1}º número: '))
    lista.append(temp)
    if temp % 2 == 0:
        pares.append(temp)
    else:
        impares.append(temp)
print(f'\nNúmeros Pares = {pares}\nSoma dos Pares = {sum(pares)}')
print(f'Números Ímpares = {impares}\nQuantidade de Ímpares = {len(impares)}')
print('\nFim do exercício 29')

###### Exercício 30 ######
lista1 = []
lista2 = []
for i in range(10):
    temp = int(input(f'Informe o {i+1}º número do VETOR 1: '))
    lista1.append(temp)
print()
for n in range(10):
    temp = int(input(f'Informe o {n+1}º número do VETOR 2: '))
    lista2.append(temp)
conjunto = set.intersection(set(lista1), set(lista2))
print(f'\n{conjunto}')
print('\nFim do exercício 30')

###### Exercício 31 ######
lista1 = []
lista2 = []
for i in range(10):
    temp = int(input(f'Informe o {i+1}º número do VETOR 1: '))
    lista1.append(temp)
print()
for i in range(10):
    temp = int(input(f'Informe o {i+1}º número do VETOR 2: '))
    lista2.append(temp)
conjunto = set.union(set(lista1), set(lista2))
print()
print(conjunto)
print('\nFim do exercício 31')

###### Exercício 32 ######
lista1 = []
lista2 = []
soma = []
mult = []
dife = []
for i in range(5):
    temp = int(input(f'Informe o {i+1}º número do VETOR 1: '))
    lista1.append(temp)
print()
for i in range(5):
    temp = int(input(f'Informe o {i+1}º número do VETOR 2: '))
    lista2.append(temp)
for i in range(5):
    temp = lista1[i] + lista2[i]
    soma.append(temp)
    temp = lista1[i] * lista2[i]
    mult.append(temp)
    temp = lista1[i] - lista2[i]
    dife.append(temp)
uniao = set.union(set(lista1), set(lista2))
inter = set.intersection(set(lista1), set(lista2))
print()
print(f'SOMA = {soma}\nMULTIPLICAÇÃO = {mult}\nSUBTRAÇÃO = {dife}\nUNIÃO = {uniao}\nINTERSEÇÃO = {inter}')
print('\nFim do exercício 32')

###### Exercício 33 ######
lista = []
comp = []
for i in range(15):
    temp = int(input(f'Informe o {i+1}º número: '))
    lista.append(temp)
comp = lista.copy()
while comp.count(0):
    for i in comp:
        if i == 0:
            comp.remove(i)
print()
print(f'Lista original = {lista}\nLista compacta = {comp}')
print('\nFim do exercício 33')

###### Exercício 34 ######
lista = []
for i in range(10):
    temp = int(input(f'Informe o {i + 1}º número: '))
    while lista.count(temp):
        print(f'O número "{temp}" já foi informado.')
        temp = int(input(f'Informe outro número: '))
    lista.append(temp)
print()
print(lista)
print('\nFim do exercício 34')

###### Exercício 35 ######
a = int(input(f'Informe o 1º número positivo menor que 10.000: '))
while a <= 0 or a >= 10000:
    print('Numero fora do intervalo')
    a = int(input(f'Informe o 1º número positivo menor que 10.000: '))
b = int(input(f'Informe o 2º número positivo menor que 10.000: '))
while b <= 0 or b >= 10000:
    print('Numero fora do intervalo')
    b = int(input(f'Informe o 2º número positivo menor que 10.000: '))
a = list(str(a))
b = list(str(b))
a = a[::-1]
b = b[::-1]
c = []
cont = 0
if len(a) > len(b):
    n = len(a)
    d = len(a) - len(b)
    for i in range(d):
        b.append('0')
else:
    n = len(b)
    d = len(b) - len(a)
    for i in range(d):
        a.append('0')
for i in range(n):
    if int(a[i]) + int(b[i]) + cont >= 10:
        c.append((int(a[i]) + int(b[i]) + cont) - 10)
        cont = 1
    else:
        c.append(int(a[i]) + int(b[i]) + cont)
        cont = 0
if cont == 1:
    c.append(1)
e = []
for i in range(len(c)):
    e.append(str(c[i]))
e = ''.join(e)
e = e[::-1]
e = float(e)
print()
print(f'Vetor a = {a}\nVetor b = {b}\nVetor soma(a,b) = {c} => {e:,.0f}')
print('\nFim do exercício 35')

###### Exercício 36 ######
lista = []
for i in range(10):
    temp = float(input(f'Informe o {i + 1}º número: '))
    lista.append(temp)
lista_ord = lista.copy()
lista_ord.sort()
print()
print(f'Vetor digitado = {lista}\nVetor ordenado = {lista_ord}')
print('\nFim do exercício 36')

###### Exercício 37 ###### (depende do 36)
lista2 = lista_ord[0:5] + lista_ord[9:4:-1]
print()
print(lista2)
print('\nFim do exercício 37')

###### Exercício 38 ######
lista = []
for i in range(10):
    temp = float(input(f'Informe o {i + 1}º número: '))
    lista.append(temp)
    lista.sort()
    #print(lista)
print()
print(lista)
print('\nFim do exercício 38')

###### Exercício 39 ######
n = int(input('Informe um número inteiro e positivo: '))
lista = []
lista2 = [1, 1]
r = 1
sp = '\x20'
while n <= 0:
    print('Número inválido.')
    n = int(input('Informe um número maior que 0: '))

print()
if n == 1:
    print(f'\033[1m0\033[0m [1]')
else:
    print(f'\033[1m0\033[0m [1]')
    while n > 1:
        lista.append(1)
        if r == 1:
            pass
        else:
            a = 0
            b = 0
            for i in range(1, r):
                lista.append(lista2[a] + lista2[b + 1])
                a += 1
                b += 1
        lista.append(1)
        lista2 = lista.copy()
        lista.clear()
        r += 1
        n -= 1
        print(f'\033[1m{r - 1}\033[0m {lista2}')
"""
print()                                           # Visualização triangulo equilatero
if n == 1:
    print(f'\033[1m0\033[0m {sp * n}[1]')
else:
    print(f'\033[1m0\033[0m {sp * n}[1]')
    while n > 1:
        lista.append(1)
        if r == 1:
            pass
        else:
            a = 0
            b = 0
            for i in range(1, r):
                lista.append(lista2[a] + lista2[b + 1])
                a += 1
                b += 1
        lista.append(1)
        lista2 = lista.copy()
        lista.clear()
        r += 1
        n -= 1
        print(f'\033[1m{r - 1}\033[0m {sp * n}{lista2}')
"""
print('\nFim do exercício 39')

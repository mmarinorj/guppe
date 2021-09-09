#
# #### Exercício 01 ####
# mult3 = []
# for n in range(1, 6):
#     mult3.append(n*3)
# print(mult3)
# print('Fim exercicio 01\n')
#
# #### Exercício 02 ####
# # a) com comando for
# for n in range(1,101):
#     print(n,end=',')
# print('')
# print('Fim exercicio 02a')
#
# # b) com comando while
# n = 1
# while n < 101:
#     print(n, end=',')
#     n += 1
# print('')
# print('Fim exercicio 02b')
# print('Fim exercicio 02\n')
#
# # c) não existe do while em Python
#
# #### Exercício 03 ####
# n = 10
# while n >= 0:
#     print(n, end=', ')
#     n -= 1
# print('\nFIM')
# print('Fim exercicio 03\n')
#
# #### Exercicio 04 ####
# n = 0
# for n in range(0, 100001, 1000):
#     print(n, end=',')
# print('')
# print('Fim exercicio 04\n')
#
# #### Exercicio 05 ####
# soma = 0
# for n in range(1, 11):
#     num = int(input((f'Digite o número {n}/10: ')))
#     soma += num
# print('A soma é:', soma)
# print('Fim exercicio 05\n')
#
# #### Exercicio 06 ####
# media = 0
# soma = 0
# for n in range(1, 11):
#     num = int(input((f'Digite o número {n}/10: ')))
#     soma += num
# media = soma/10
# print(f'A média é: {media: .2f}')
# print('Fim exercicio 06\n')
#
# #### Exercicio 07 ####
# media = 0
# soma = 0
# for n in range(1, 11):
#     num = int(input((f'Digite o número inteiro e positivo {n}/10: ')))
#     while num < 0:
#         print('Número inválido!')
#         num = int(input((f'Digite o número inteiro e positivo {n}/10: ')))
#     soma += num
# media = soma/10
# print(f'A média é: {media:.2f}')
# print('Fim exercicio 07\n')
#
# #### Exercicio 08 ####
# num = int(input(('Digite o número 1/10: ')))
# maior = num
# menor = num
# for n in range(2, 11):
#     num = int(input((f'Digite o número {n}/10: ')))
#     if num > maior:
#         maior = num
#     elif num < menor:
#         menor = num
# print(f'O menor número digitado foi {menor}')
# print(f'O maior número digitado foi {maior}')
# print('Fim exercicio 08\n')
#
# #### Exercicio 09 ####
# n = int(input(('Digite um número: ')))
# for i in range(1, (n*2), 2):
#     print(i, end=' ')
# print('')
# print('Fim exercicio 09\n')
#
# #### Exercicio 10 ####
# soma = 0
# lista = []
# for i in range(2, 101, 2):
#     lista.append(i)
#     soma += i
# print(lista)
# print(f'A soma dos 50 primeiros numeros pares é: {soma}')
# print('Fim exercicio 10\n')
#
# #### Exercicio 11 ####
# n = int(input('Informe um número: '))
# #lista = []
# for i in range(n):
#     print(i, end=' ')
#     #lista.append(i)
# #print(lista)
# print('\nFim exercicio 11\n')
#
# #### Exercicio 12 ####
# #lista = []
# n = int(input('Informe um número maior que 0: '))
# while n <= 0:
#     print('Número inválido!')
#     n = int(input('Informe um número maior que 0: '))
# for i in range(n, -1, -1):
#     #lista.append(i)
#     print(i, end=' ')
# #print(lista[::-1])  # ou
# #lista.reverse()
# #print(lista)
# print('')
# print('Fim exercicio 12\n')
#
# #### Exercicio 13 ####
# n = int(input('Informe um número PAR maior que 0: '))
# while n % 2 != 0 or n == 0:
#     print('Número inválido!')
#     n = int(input('Informe um número PAR maior que 0: '))
# for i in range(0, n+1, 2):
#     print(i, end=' ')
# print('')
# print('Fim exercicio 13\n')
#
# #### Exercicio 14 ####
# n = int(input('Informe um número PAR maior que 0: '))
# while n % 2 != 0 or n == 0:
#     print('Número inválido!')
#     n = int(input('Informe um número PAR maior que 0: '))
# for i in range(n, -2, -2):
#     print(i, end=' ')
# print('')
# print('Fim exercicio 14\n')
#
# #### Exercicio 15 ####
# n = int(input('Informe um número ÍMPAR maior que 0: '))
# while n % 2 == 0 or n == 0:
#     print('Número inválido!')
#     n = int(input('Informe um número ÍMPAR maior que 0: '))
# for i in range(1, n+1, 2):
#     print(i, end=' ')
# print('')
# print('Fim exercicio 15\n')
#
# #### Exercicio 16 ####
# n = int(input('Informe um número ÍMPAR maior que 0: '))
# while n % 2 == 0 or n == 0:
#     print('Número inválido!')
#     n = int(input('Informe um número ÍMPAR maior que 0: '))
# for i in range(n, 0, -2):
#     print(i, end=' ')
# print('')
# print('Fim exercicio 16\n')
#
# #### Exercicio 17 ####
# soma = 0
# n = int(input('Informe um número maior que 0: '))
# while n <= 0:
#     print('Número inválido!')
#     n = int(input('Informe um número maior que 0: '))
# for i in range(1, n+1):
#     soma += i
# print('A soma é', soma)
# print('Fim exercicio 17\n')
#
# #### Exercicio 18a ####
# n = int(input('Informe a quantidade de números a serem lidos: '))
# if n != 0:
#     while n < 0:
#         print('Número inválido')
#         n = int(input('Informe a quantidade de números a serem lidos: '))
#     num = int(input((f'informe o numero 1/{n}: ')))
#     maior = num
#     posicao = 1
#     for i in range(2, n+1):
#         num = int(input((f'informe o numero {i}/{n}: ')))
#         if num > maior:
#             maior = num
#             posicao = i
#     print(f'{maior} foi o maior número e foi o {posicao}º numero digitado.')
# else:
#     print('Programa encerrado pelo usuário')
# print('Fim exercicio 18a\n')
#
# #### Exercicio 18b ####
# n = int(input('Informe a quantidade de números a serem lidos: '))
# if n != 0:
#     while n < 0:
#         print('Número inválido')
#         n = int(input('Informe a quantidade de números a serem lidos: '))
#     num = int(input((f'informe o numero 1/{n}: ')))
#     maior = num
#     controle = num
#     vezes = 0
#     for i in range(2, n+1):
#         num = int(input((f'informe o numero {i}/{n}: ')))
#         if num > maior:
#             maior = num
#             vezes = 1
#         elif num == maior:
#             vezes += 1
#     if vezes == 0:
#         vezes = 1
#     elif controle == maior:
#         vezes += 1
#     print(f'{maior} foi o maior número e foi digitado {vezes} vez(es).')
# else:
#     print('Programa encerrado pelo usuário')
# print('Fim exercicio 18b\n')
#
# #### Exercicio 19 ####
# n = int(input('Informe um número entre 100 e 999: '))
# while n < 100 or n > 999:
#     print('Número inválido')
#     n = int(input('Informe um número entre 100 e 999: '))
# nome = str(n)
# for i in nome:
#     int(i)
#     print(i, end=' ')
# print('\nFim exercicio 19\n')
#
# #### Exercicio 20 ####
# par = 0
# qtt = 0
# n = int(input('Informe um número (para sair, digite 1000): '))
# while n != 1000:
#     if n % 2 == 0:
#         par += 1
#     qtt += 1
#     n = int(input('Informe um número (para sair, digite 1000): '))
# print(f'\nForam digitados {qtt} números. Dentre estes, {par} são PARES.')
# print('Fim exercicio 20\n')
#
# #### Exercicio 21 ####
# par = 0
# impar = 1
# num1 = int(input('Informe o primeiro número do intervalo: '))
# num2 = int(input('Informe o segundo número do intervalo: '))
# while num2 == num1:
#     print('Número inválido!')
#     num2 = int(input('O segundo número deve ser diferente do primeiro: '))
# if num1 < num2:
#     for i in range(num1, num2+1):
#         if i % 2 == 0:
#             par += i
#         else:
#             impar *= i
# else:
#     for i in range(num1, num2-1, -1): # poderia tb fazer igual ao if invertendo a ordem dos num (num2, num1+1)
#         if i % 2 == 0:
#             par += i
#         else:
#             impar *= i
# print(f'\nA soma dos numeros pares do intervalo é {par:,}')
# print(f'\A multiplicação dos numeros ímpares do intervalo é {impar:,}')
# print('Fim exercicio 21\n')
#
# #### Exercicio 22 ####
# n = 1
# den = 0
# soma = 0
# nota = float(input(f'Informe sua {n}ª nota (para terminar, digite 0 (zero)): '))
# while nota != 0:
#     while nota != 0 and 10 <= nota <= 20:
#         soma += nota
#         den += 1
#         n += 1
#         nota = float(input(f'Informe sua {n}ª nota (para terminar, digite 0 (zero)): '))
#     if nota != 0:
#         print('Número inválido. O número deve estar entre 10.00 e 20.00')
#         nota = float(input(f'Informe sua {n}ª nota (para terminar, digite 0 (zero)): '))
# if soma == 0:
#     print('\nPrograma encerrado pelo usuário sem entradas')
# else:
#     print(f'\nA sua média entre as {den} notas é {(soma/den):.2f}')
# print('Fim exercicio 22\n')
#
# #### Exercicio 23 ####
# num = int(input('Informe um número inteiro maior que zero: '))
# while num <= 0:
#     print('Número inválido')
#     num = int(input('Informe um número inteiro maior que zero: '))
# print('')
# for n in range(1, num + 1):
#     if num % n == 0:
#         print(n, end=' ')
# print('\nFim exercicio 23\n')
#
# #### Exercicio 24 ####
# soma = 0
# num = int(input('Informe um número inteiro maior que zero: '))
# while num <= 0:
#     print('Número inválido')
#     num = int(input('Informe um número inteiro maior que zero: '))
#
# print(f'\nA soma dos divisores de {num} é:')
# print('(', end='')
# for n in range(1, num):
#     if num % n == 0:
#         soma = soma + n
#         print(f' + {n}', end='')
# print(f' = {soma} )')
#
# print('Fim exercicio 24\n')
#
# #### Exercicio 25 ####
# print('')
# soma = 0
# for n in range(1000, 0, -1):
#     if n % 3 == 0 or n % 5 == 0:
#         soma = soma + n
#         #print(f' + {n}', end='')
# print(f'Soma = {soma} ')
# print('Fim exercicio 25\n')
#
# #### Exercicio 26 ####
# num = int(input('Informe um número: '))
# mult = 0
# de = 0
# if num > 0:
#     for n in range(num, 0, -1):
#         if n % 11 == 0 or n % 13 == 0 or n % 17 == 0:
#             mult = n
#             break
# else:
#     for n in range(0, num, -1):
#         if n % 11 != 0 or n % 13 != 0 or n % 17 != 0:
#             mult = n
#             break
# if mult % 11 == 0:
#     de = 11
# elif mult % 13 == 0:
#     de = 13
# elif mult % 17 == 0:
#     de = 17
# print(f'O primeiro multiplo de 11, 13 ou 17 de {num} é o número {mult} (multiplo de {de})')
# print('Fim exercicio 26\n')
#
# #### Exercicio 27 ####
# num = int(input('Informe n para H(n) - Soma da Série Harmonica de n : '))
# hn = 1
# while num <= 0:
#     print('Numero inválido')
#     num = int(input('Informe n para H(n) - Soma da Série Harmonica de n : '))
# for n in range(2, num+1):
#     hn += 1/n
# print(f'A soma da série Harmônica de H({num:,}) = {hn:,.2f}')
# print('Fim exercicio 27\n')
#
# #### Exercicio 28 ####
# num = int(input('Informe n para E = 1/1! + 1/2! + ... +1/n! : '))
# e = 1
# while num <= 0:
#     print('Numero inválido')
#     num = int(input('Informe n para E = 1/1! + 1/2! + ... +1/n! : '))
# for n in range(2, num+1):
#     fat = n
#     for i in range(n, 1, -1):
#         fat = fat*(i-1)
#     e += 1/fat
#     print(fat)
# print(f'E = 1/1! + 1/2! + ... +1/n! = {e:,.2f}')
# print('Fim exercicio 28\n')
#
# #### Exercicio 29 ####
# s = 0
# for n in range(2, 11, 2):
#     fat = n
#     for i in range(n, 1, -1):
#         fat = fat*(i-1)
#     s += 1/fat
#     print(fat)
# print(f'E = 1/2! + 1/4! + ... +1/10! = {s:,.2f}')
# print('Fim exercicio 29\n')
#
# #### Exercicio 31 ####
# s = 0
# n = -1
# d = 0
# while n <= 97:
#     n += 2
#     d += 1
#     s = s + n/d
#     print(f'({n}/{d})', end=' ')
# print(f'\nS = {s:.2f}')
# print('Fim exercicio 31\n')
#
#### Exercicio 32 ####
# import random
#
# d1 = 1
# d2 = 1
# while d1 != 0 or d2 != 0:
#     print('Para encerrar o programa, informe 0 nos dois números')
#     d1 = float(input('Informe o primeiro número: '))
#     d2 = float(input('Informe o segundo número: '))
#     if d1 == 0 and d2 == 0:
#         print('\nPrograma encerrado pelo ususário')
#     elif d1 > d2:
#         print(f'\n{d1} > {d2}\n')
#     elif d1 < d2:
#         print(f'\n{d1} < {d2}\n')
#     elif d1 == d2:
#         print(f'\n{d1} = {d2}\n')
# print('Fim exercicio 32\n')
#
# #### Exercicio 33 ####
# d1 = int(input('Informe o primeiro número: '))
# d2 = int(input('Informe o segundo número: '))
# n = int(input('informe quantas multiplos dos dois numeros(ao mesmo tempo ou não) vc deseja saber: '))
# print()
# cont = 0
# num = 0
# while cont != n:
#     if num % d1 == 0 or num % d2 == 0:
#         cont += 1
#         print(num, end=',')
#     num += 1
# print('\nFim exercicio 33\n')
# #
# #### Exercicio 34 ####
# d1 = int(input('Informe o primeiro número: '))
# d2 = int(input('Informe o segundo número: '))
# lista = []
# if d1 > d2:
#     d1, d2 = d2, d1
# for i in range(d1, d2 + 1):
#     lista.append(i)
# q = len(lista) - 1
# mmc_temp = lista[q]
# while q > 0:
#     if mmc_temp % lista[q-1] == 0:
#         mmc = mmc_temp
#         q -= 1
#     else:
#         num1 = mmc_temp
#         while mmc_temp % num1 != 0 or mmc_temp % lista[q-1] != 0:
#             mmc_temp += 1
#         mmc = mmc_temp
#         q -= 1
# print(f'\nO MMC entre os números {lista} é {mmc:,}')
# print('Fim exercicio 34\n')
# #
# #### Exercicio 35 ####
# d1 = int(input('Informe o início do intervalo: '))
# d2 = int(input('Informe o final do intervalo: '))
# lista = []
# impares = 0
# if d1 < d2:
#     for i in range(d1, d2 + 1):
#         lista.append(i)
#         if i % 2 == 1:
#             impares += i
#             print('\n', i, end=' ')
#     print(f'\nSoma dos ímpares neste intervalo: {impares}')
# else:
#     print('\nIntervalo de valores inválido')
# print('Fim exercicio 35\n')
#
# #### Exercicio 36 ####
# soma_quad = 0
# quad_soma = 0
# for i in range(1, 101):
#     soma_quad += i**2
#     quad_soma += i
# quad_soma = quad_soma**2
# dif = quad_soma - soma_quad
# print(f'\nA diferença entre o quadrado da soma e a soma dos quadrados: {dif:,}')
# print('Fim exercicio 36\n')
# #
# #### Exercicio 37 ####
# print()
# for i in range(1000, 10000):
#     istr = str(i)
#     i1 = istr[0:2]
#     i2 = istr[2:4]
#     i1 = int(i1)
#     i2 = int(i2)
#     soma = i1 + i2
#     quad = soma**2
#     if quad == i:
#         print(i, end=' ')
# print('\nFim exercicio 37\n')
#
#### Exercicio 38 ####  - solução 1
# teste = True
# while teste:
#     for a in range(1, 1000):
#         for b in range(1, 1000):
#             for c in range(1, 1000):
#                 if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                     if a < b < c:
#                         print(f'\na = {a}, b = {b}, c = {c}')
#                         print('Fim exercicio 38\n')
#                         teste = False
#                         break
#
#### Exercicio 38 ####  - solução 2
# c = 997
# teste = True
# while teste:
#     for b in range(2, 1000-c):
#         for a in range(1, b):
#             if a + b + c == 1000 and a**2 + b**2 == c**2:
#                 teste = False
#                 print(f'\na = {a}, b = {b}, c = {c}')
#                 print('Fim exercicio 38\n')
#                 break
#     c -= 1
#
#### Exercicio 38 ####  - solução 3
# teste = True
# while teste:
#     for a in range(1, 1000):
#         for b in range(1, 1000):
#             for c in range(1, 1000):
#                 if a + b + c == 1000 and a**2 + b**2 == c**2:
#                     if a < b < c:
#                         print(f'\na = {a}, b = {b}, c = {c}')
#                         print('Fim exercicio 38\n')
#                         teste = False
#                         break
#             if a + b + c == 1000 and a**2 + b**2 == c**2:
#                 break
#         if a + b + c == 1000 and a**2 + b**2 == c**2:
#             break
#     if a + b + c == 1000 and a**2 + b**2 == c**2:
#         break
#
#### Exercício 39 ####
# print()
# b = float(input('Informe a base do triângulo (em metros): '))
# while b <= 0:
#     print('Número inválido')
#     b = float(input('Informe a base do triângulo (em metros): '))
# h = float(input('Informe a altura do triângulo (em metros): '))
# while h <= 0:
#     print('Número inválido')
#     h = float(input('Informe a altura do triângulo (em metros): '))
# a = (b * h) / 2
# print(f'\nA área do triângulo é de {a:.2f} m²')
# print('Fim exercicio 39\n')
#
#### Exercício 40 ####
# print()
# num = int(input('Informe um número inteiro. Se desejar encerrar o programa, digite qq numero menor que zero: '))
# maior = num
# menor = num
# if num >= 0:
#     while num >= 0:
#         if num > maior:
#             maior = num
#         elif num < menor:
#             menor = num
#         num = int(input('Informe um número inteiro. Se desejar encerrar o programa, digite qq numero menor que zero: '))
#     print(f'\nPrograma encerrado pelo usuário.\nMaior numero digitado: {maior}\nMenor numero digitado: {menor}')
#     print('Fim exercicio 40\n')
# else:
#     print(f'\nPrograma encerrado pelo usuário sem dados digitados')
#     print('Fim exercicio 40\n')
#
#### Exercício 41 ####
# print()
# r1 = float(input('Informe o valor de R1. Zero para encerrar o programa: '))
# r2 = r1
# while r1 != 0 and r2 != 0:
#     if r1 < 0:
#         print('Número negativo inválido')
#         r1 = float(input('Informe o valor de R1. Zero para encerrar o programa: '))
#         while r1 < 0:
#             print('Número negativo inválido')
#             r1 = float(input('Informe o valor de R1. Zero para encerrar o programa: '))
#     elif r1 > 0:
#         r2 = float(input('Informe o valor de R2. Zero para encerrar o programa: '))
#         if r2 < 0:
#             print('Número negativo inválido')
#             r2 = float(input('Informe o valor de R2. Zero para encerrar o programa: '))
#             while r2 < 0:
#                 print('Número negativo inválido')
#                 r2 = float(input('Informe o valor de R2. Zero para encerrar o programa: '))
#         elif r2 > 0:
#             r = (r1 * r2) / (r1 + r2)
#             print(f'\nR = {r:.4f}')
#             r1 = float(input('\nInforme o valor de R1. Zero para encerrar o programa: '))
# print(f'\nPrograma encerrado pelo usuário')
# print('Fim exercicio 41\n')
#
#### Exercício 42 ####
# num = float(input('\nInforme um numero. Numeros negativos ou Zero encerram o programa: '))
# while num > 0:
#     quadrado = num**2
#     cubo = num**3
#     raiz = num**0.5
#     print(f'Numero: {num:,.2f} | x² = {quadrado:,.2f} | x³ = {cubo:,.2f} | √x = {raiz:,.2f}')
#     num = float(input('\nInforme um numero. Numeros negativos ou Zero encerram o programa: '))
# print(f'\nPrograma encerrado pelo usuário')
# print('Fim exercicio 42\n')
#
#### Exercício 43 ####
# idade = float(input('\nInforme a idade do usuário. Zero encerra o programa: '))
# soma = 0
# controle = 0
# if idade != 0:
#     while idade != 0:
#         while idade < 0:
#             print('Número inválido!')
#             idade = float(input('Informe a idade do usuário. Zero encerra o programa: '))
#         while idade > 0:
#             soma += idade
#             controle += 1
#             idade = float(input('Informe a idade do usuário. Zero encerra o programa: '))
#     if controle == 0:
#         print('\nPrograma finalizado pelo usuário sem inserção de dados')
#         print('Fim exercicio 43\n')
#     else:
#         print(f'\nA média de idade das {controle:.0f} pessoas inseridas é de {(soma / controle):.2f}')
#         print('Fim exercicio 43\n')
# else:
#     print('\nPrograma finalizado pelo usuário sem inserção de dados')
#     print('Fim exercicio 43\n')
#
### Exercício 44 ####
from time import time
num = int(input('\nInforme o número que encerrará a sequencia Fibonacci: '))
ini = time()
c = 0
a = 0
b = 1
print('0, 1', end='')
while c < num:
    c = a + b
    a, b = b, c
    print(f', {c:,}', end='')
print('...')
fim = time()
print(f'Tempo de execução: {fim - ini}')
print('Fim exercicio 44\n')

#### Exercício 45 ####
# print('Conversor de Km/h <=> m/s')
# velo = float(input(f'Insira uma velocidade: '))
# op = ''
# op = input(f'(M) Km/h => m/s\n(K) m/s => Km/h\n(E) Sair do programa\nDigite uma opção: ')
# if op.lower() != 'e':
#     while op.lower() != 'e':
#         while op.lower() != 'k' and op.lower() != 'm' and op.lower() != 'e':
#             print('\nCódigo inválido')
#             op = input(f'(M) Km/h => m/s\n(K) m/s => Km/h\n(E) Sair do programa\nDigite uma opção: ')
#         while op.lower() == 'k' or op.lower() == 'm' or op.lower() == 'e':
#             if op.lower() == 'k':
#                 velo = velo * 36 / 10
#                 print(f'\nVelocidade = {velo:.2f} Km/h')
#             elif op.lower() == 'm':
#                 velo = velo * 10 / 36
#                 print(f'\nVelocidade = {velo:.2f} m/s')
#             elif op.lower() == 'e':
#                 print('\nPrograma encerrado pelo usuário')
#                 break
#             velo = float(input(f'\nInsira uma velocidade: '))
#             op = input(f'(M) Km/h => m/s\n(K) m/s => Km/h\n(E) Sair do programa\nDigite uma opção: ')
# else:
#     print('\nPrograma encerrado pelo usuário')
# print('Fim exercicio 45\n')
#
#### Exercicio 46 ####
# cont = 1
# print('Tente adivinhar o número!')
# num = random.randint(1, 1000)
# print(num)                      # no programa real, essa linha não existiria
# chute = int(input('Faça sua aposta! Digite um número de 1 a 1000: '))
# while chute != num:
#     if chute < 1 or chute > 1000:
#         while chute < 1 or chute > 1000:
#             print('Numero fora do escopo.')
#             chute = int(input('Digite um número de 1 a 1000: '))
#     else:
#         cont += 1
#         if num > chute:
#             chute = int(input('Ainda não foi desta vez! Tente um numero maior: '))
#         elif num < chute:
#             chute = int(input('Ainda não foi desta vez! Tente um numero menor: '))
# if cont == 0:
#     print(f'Você acertou na 1ª tentativa, Parabéns!')
# else:
#     print(f'Você acertou na {cont}ª tentativa, Parabéns!')
# print('Fim exercicio 46\n')
#
#### Exercício 47 ####
# print("####### CALCULADORA #########")
# a = float(input("\nInforme o primeiro número: "))
# b = float(input("Informe o segundo número: "))
# sinal = input("\nInforme a operação matemática desejada (+,-,*,/, e -> sair): ")
# while sinal.lower() != 'e':
#     while sinal.lower() != 'e' and sinal != '+' and sinal != '-' and sinal != '*' and sinal != '/':
#         print("\nSinal inválido!")
#         sinal = input("Informe a operação matemática desejada (+,-,*,/, e -> sair): ")
#     if sinal.lower() != 'e':
#         if sinal == "+":
#             c = a + b
#         elif sinal == "-":
#             c = a - b
#         elif sinal == "*":
#             c = a * b
#         elif sinal == "/":
#             c = a / b
#         print(f"\n\nRESULTADO = {c:,.2f}")
#         a = float(input("\nInforme o primeiro número: "))
#         b = float(input("Informe o segundo número: "))
#         sinal = input("\nInforme a operação matemática desejada (+,-,*,/, e -> sair): ")
# print('\nPrograma encerrado pelo usuário')
# print('Fim exercicio 46\n')
#
#### Exercício 48 ####
# num = 4000000
# c = 0
# a = 0
# b = 1
# soma = 0
# while a + b <= num:
#     c = a + b
#     a, b = b, c
#     if c % 2 == 0:
#         soma += c
#         print(f'{c:,}, ', end='')
# print('...')
# print(f'\nSOMA = {soma}')
# print('Fim exercicio 48\n')
#
#### Exercício 49 ####
# sal_joao = 1
# sal_carlos = 3
# poup_carlos = 0
# apli_joao = 0
# mes = 0
# while apli_joao <= poup_carlos:
#     apli_joao += sal_joao
#     apli_joao += apli_joao * 5 / 100
#     poup_carlos += sal_carlos
#     poup_carlos += poup_carlos * 2 / 100
#     mes += 1
# #print(f'\nInvestimento Carlos: {poup_carlos:,.2f}\nInvestimento João: {apli_joao:,.2f}')
# if apli_joao > poup_carlos:
#     print(f'\nEm {mes} meses o valor investido de João ultrapassará o de Carlos ')
# else:
#     print(f'\nEm {mes} meses o valor investido de João se igualará ao de Carlos ')
# print('Fim exercicio 49\n')
#
#### Exercício 50 ####
# altura_chico = 150
# altura_ze = 110
# anos = 0
# while altura_chico >= altura_ze:
#     altura_chico += 2
#     altura_ze += 3
#     anos += 1
# print(f'\nEm {anos} anos Zé terá {(altura_ze/100):.2f} m enquanto Chico terá {(altura_chico/100):.2f} m ')
# print('Fim exercicio 50\n')
#
#### Exercício 51 ####
# salario_contrato = 2000
# ano_atual = int(input('Informe o ano vigente: '))
# ano_contrato = 1996
# #percentual = 0.03
# aumento_inicial = 0.015
# aumento_atual = (salario_contrato * aumento_inicial) * 2
# salario_atual = salario_contrato + (salario_contrato * aumento_inicial)
# anos = ano_atual - ano_contrato
# for n in range(1, anos +1):
#     salario_atual += aumento_atual
#     #print(salario_atual, end=' ')
#     #print(aumento_atual, end=' ')
#     #print(f'{percentual * 100:.2f}%', end=' ')
#     #percentual *= 2
#     aumento_atual *= 2
# print(f'\nO salário atual do funcionário é R$ {salario_atual:,.2f}')
# print('Fim exercicio 51\n')
#
#### Exercício 52 ####
# notas_100 = 0
# resto_100 = 0
# notas_50 = 0
# resto_50 = 0
# notas_20 = 0
# resto_20 = 0
# notas_10 = 0
# resto_10 = 0
# notas_5 = 0
# resto_5 = 0
# notas_2 = 0
# notas_1 = 0
# saque = int(input('Informe o valor do saque: '))
# if saque % 100 == 0:
#     notas_100 = saque / 100
# elif saque % 100 != saque:
#     notas_100 = (saque - (saque % 100)) / 100
#     resto_100 = saque % 100
# else:
#     resto_100 = saque
# if resto_100 % 50 == 0:
#     notas_50 = resto_100 / 50
# elif resto_100 % 50 != resto_100:
#     notas_50 = (resto_100 - (resto_100 % 50)) / 50
#     resto_50 = resto_100 % 50
# else:
#     resto_50 = resto_100
# if resto_50 % 20 == 0:
#     notas_20 = resto_50 / 20
# elif resto_50 % 20 != resto_50:
#     notas_20 = (resto_50 - (resto_50 % 20)) / 20
#     resto_20 = resto_50 % 20
# else:
#     resto_20 = resto_50
# if resto_20 % 10 == 0:
#     notas_10 = resto_20 / 10
# elif resto_20 % 10 != resto_20:
#     notas_10 = (resto_20 - (resto_20 % 10)) / 10
#     resto_10 = resto_20 % 10
# else:
#     resto_10 = resto_20
# if resto_10 % 5 == 0:
#     notas_5 = resto_10 / 5
# elif resto_10 % 5 != resto_10:
#     notas_5 = (resto_10 - (resto_10 % 5)) / 5
#     resto_5 = resto_10 % 5
# else:
#     resto_5 = resto_10
# if resto_5 % 2 == 0:
#     notas_2 = resto_5 / 2
# elif resto_5 % 2 != resto_5:
#     notas_2 = (resto_5 - (resto_5 % 2)) / 2
#     notas_1 = resto_5 % 2
# else:
#     notas_1 = resto_5
# print()
# if notas_100 != 0:
#     print(f'Notas de 100 reais: {notas_100:.0f}')
# if notas_50 != 0:
#     print(f'Notas de 50 reais: {notas_50:.0f}')
# if notas_20 != 0:
#     print(f'Notas de 20 reais: {notas_20:.0f}')
# if notas_10 != 0:
#     print(f'Notas de 10 reais: {notas_10:.0f}')
# if notas_5 != 0:
#     print(f'Notas de 5 reais: {notas_5:.0f}')
# if notas_2 != 0:
#     print(f'Notas de 2 reais: {notas_2:.0f}')
# if notas_1 != 0:
#     print(f'Notas de 1 real: {notas_1:.0f}')
# print('\nFim exercicio 52\n')
#
#### Exercício 53 ####
# n = int(input('\nInsira a quantidade de linhas desejadas para o Triângulo de Floyd: '))
# ini = 1
# fim = 2
# contador = 1
# while contador <= n:
#     for i in range(ini, fim):
#         print(i, end=' ')
#     contador += 1
#     ini = fim
#     fim += contador
#     print()
# print('\nFim exercicio 53\n')
#
#### Exercício 54 ####
# contador = 0
# num = int(input('Informe um número inteiro maior que 1: '))
# for n in range(1, num + 1):
#     if num % n == 0:
#         #print(n, end=' ')
#         contador += 1
# if contador == 2:
#     print(f'\n{num} é um número primo!')
# else:
#     print(f'\n{num} NÃO é um número primo!')
# print('\nFim exercicio 54\n')
#
#### Exercício 54 #### - Opção 2 usando a biblioteca SymPy
# import sympy
# num = int(input('Informe um número inteiro maior que 1: '))
# if sympy.isprime(num):
#     print(f'\n{num} é um número primo!')
# else:
#     print(f'\n{num} NÃO é um número primo!')
# print('\nFim exercicio 54\n')
#
#### Exercício 55 ####
# num = int(input('Informe um número inteiro maior que 1: '))
# np = num
# contador = 0
# soma = 0
# while num > 0:
#     contador2 = 0
#     for n in range(1, contador + 1):
#         if contador % n == 0:
#             # print(n, end=' ')
#             contador2 += 1
#     if contador2 == 2:
#         print(contador, end=' ')
#         soma += contador
#         num -= 1
#     contador += 1
# print(f'\nA soma dos {np} primeiros numeros primos é {soma:,}')
# print('\nFim exercicio 55\n')
#
#### Exercício 55 #### Opção 2 usando a biblioteca primesieve
# import primesieve
# num = int(input('Informe um número inteiro maior que 1: '))
# lista = primesieve.n_primes(num)
# print(lista)
# print(f'\nA soma dos {num} primeiros numeros primos é {sum(lista):,}')
# print('\nFim exercicio 55\n')
#
#### Exercício 56 ####
# contador = 1
# soma = 0
# while contador < 2000000:
#     contador2 = 0
#     for n in range(1, contador + 1):
#         if contador % n == 0:
#             contador2 += 1
#     if contador2 == 2:
#         #print(contador, end=' ')
#         soma += contador
#     contador += 1
# print(f'\nA soma dos numeros primos abaixo de 2 milhões é {soma:,}')
# print('\nFim exercicio 56\n')
#
#### Exercício 56 #### - Opção 2 usando a biblioteca SymPy
# import sympy
# lista = list(sympy.sieve.primerange(1, 2000000))
# lista = sum(lista)
# print(f'\nA soma dos numeros primos abaixo de 2 milhões é {lista:,}')
# print('\nFim exercicio 56\n')

#
#### Exercício 57 ####
# num = int(input('Informe o primeiro inteiro maior que 1 do intervalo: '))
# num1 = int(input('Informe o segundo inteiro maior que 1 do intervalo: '))
# contador = num
# num1_temp = num1
# if num == 1:
#     soma = 1
#     print('1 ', end='')
# else:
#     soma = 0
# while num1 > num:
#     contador2 = 0
#     for n in range(1, contador + 1):
#         if contador % n == 0:
#             contador2 += 1
#     if contador2 == 2:
#         print(contador, end=' ')
#         soma += 1
#     num1 -= 1
#     contador += 1
# print(f'\nExistem {soma} numeros primos entre os números {num} e {num1_temp}.')
# print('\nFim exercicio 57\n')
#
#### Exercício 58 ####
# num = int(input('Informe o primeiro inteiro maior que 1 do intervalo: '))
# num1 = int(input('Informe o segundo inteiro maior que 1 do intervalo: '))
# contador = num
# num1_temp = num1
# if num == 1:
#     soma = 1
#     print('1 ', end='')
# else:
#     soma = 0
# while num1 > num:
#     contador2 = 0
#     for n in range(1, contador + 1):
#         if contador % n == 0:
#             # print(n, end=' ')
#             contador2 += 1
#     if contador2 == 2:
#         print(contador, end=' ')
#         soma += contador
#     num1 -= 1
#     contador += 1
# print(f'\nA soma dos numeros primos entre os números {num} e {num1_temp} é {soma:,}')
# print('\nFim exercicio 58\n')
#
#### Exercício 59 ####
# consumo1 = 0
# consumo2 = 0
# consumo3 = 0
# maior = 0
# menor = 100000000000
# soma = 0
# habit = int(input('Informe o número de habitantes da cidade: '))
# print(f'Existem {habit} habitantes na cidade\n')
# valor_kwh = float(input('informe o valor em reais do Kwh nesta cidade: '))
# print(f'Valor do Kwh = R$ {valor_kwh:,.2f}\n')
# for n in range(1, habit + 1):
#     consumo = float(input(f'Informe o consumo mensal em Kw do {n}º habitante: '))
#     codigo = int(input(f'Informe o código deste consumidor:\n(1) Residencial\n(2) Comercial\n(3) Industrial\nCódigo: '))
#     soma += consumo
#     if consumo > maior:
#         maior = consumo
#     if consumo < menor:
#         menor = consumo
#     if codigo == 1:
#         consumo1 += consumo
#     if codigo == 2:
#         consumo2 += consumo
#     if codigo == 3:
#         consumo3 += consumo
# print(f'\nO MAIOR consumo mensal de Kw na cidade: {maior:,.2f} Kw')
# print(f'O MENOR consumo mensal de Kw na cidade: {menor:,.2f} Kw')
# print(f'A média de consumo mensal de Kw na cidade: {(soma/habit):,.2f} Kw\n')
# print(f'Consumo por categoria:\nResidencial: {consumo1:,.2f} Kw\nComercial: {consumo2:,.2f} Kw\nIndustrial: {consumo3:,.2f} Kw')
# print('\nFim exercicio 59')
#
#### Exercício 60 ####
# cont = 1
# soma = 0
# qtt_num = 0
# soma_pares = 0
# qtt_pares = 0
# num = int(input(f'Informe o {cont}º numero. Para finalizar, digite 0: '))
# maior = num
# menor = num
# if num != 0:
#     while num != 0:
#         cont += 1
#         soma += num
#         qtt_num += 1
#         if num > maior:
#             maior = num
#         if num < menor:
#             menor = num
#         if num % 2 == 0:
#             soma_pares += num
#             qtt_pares += 1
#         num = int(input(f'Informe o {cont}º numero. Para finalizar, digite 0: '))
#     print(f'\nRespostas:\n(a) A soma dos números digitados: {soma:,}')
#     print(f'(b) A quantidade de números digitados: {qtt_num}')
#     print(f'(c) A média dos números digitados: {(soma/qtt_num):,.2f}')
#     print(f'(d) O MAIOR número digitado: {maior}')
#     print(f'(e) O MENOR número digitado: {menor}')
#     print(f'(f) A média dos números pares digitados: {(soma_pares/qtt_pares):,.2f}')
# else:
#     print('Programa finalizado pelo usuário sem entrada de dados')
# print('\nFim exercicio 60')
#
#### Exercício 61 ####
# maior = 0
# for n in range(100*100, 999*999):
#     if str(n) == str(n)[::-1]:
#         maior = n
#         #if n > maior:
#             #maior = n
# print(f'\nO maior numero palíndromo obtido a partir do produto de dois numeros de 3 dígitos é: {maior}')
# print('\nFim exercicio 61')
#
#### Exercício 62 ####
# from num2words import num2words
# nome2 = ''
# for n in range(1, 1001):
#     nome = num2words(n, lang='pt-br')
#     nome = nome.replace(' ', '')
#     nome2 += nome
# lista_nome = list(nome2)
# print(nome2)
# print(lista_nome)
# print(f"\nA quantidade de letras nesse intervalo de numeros é: {len(lista_nome) + 1:,} letras ({num2words((len(lista_nome) + 1), lang='pt-br')}).")
# print('\nFim exercicio 62')


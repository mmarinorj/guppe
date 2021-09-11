###### Exercício 01 ######
cont = 0
matriz = []
for i in range(4):
    matriz_temp = []
    for n in range(4):
        temp = int(input(f'Informe o {n + 1}º número da {i + 1}ª linha: '))
        matriz_temp.append(temp)
    matriz.append(matriz_temp.copy())
for a, b, c, d in matriz:
    if a > 10:
        cont += 1
    if b > 10:
        cont += 1
    if d > 10:
        cont += 1
    if d > 10:
        cont += 1
print(f'A Matriz 4x4 {matriz} contem {cont} números maiores que 10')
print('\nFim do exercício 1')

###### Exercício 02 ######
matriz = []
# x = 5
t = 5
for i in range(t):
    m_temp = []
    for n in range(t):
        if i == n:
            temp = m_temp.append(1)
            # x = 0
        else:
            temp = m_temp.append(0)
            # x += 1
    matriz.append(m_temp.copy())
    print(m_temp)
# print(matriz)
print('\nFim do exercício 2')

###### Exercício 03 ######
matriz = []
x = 4
t = x
l = 0
for i in range(t):
    m_temp = []
    c = 0
    for n in range(t):
        temp = m_temp.append(c*l)
        c += 1
    matriz.append(m_temp.copy())
    print(m_temp)
    l += 1
# print(matriz)
print('\nFim do exercício 3')

###### Exercício 04 ######
import random
import time
matriz = []
m_controle = []
x = 10
t = x
rand = 100
for i in range(t):
    m_temp = []
    for n in range(t):
        temp = random.randint(0, rand)
        while m_controle.count(temp):
            temp = random.randint(0, rand)
        m_controle.append(temp)
        m_temp.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
    time.sleep(2)
maior = matriz[0][0]
for l in matriz:
    for c in l:
        if c > maior:
            maior = c
            coluna = l.index(c)
            linha = matriz.index(l)
print(f'O Maior número da matriz é o {maior} => matriz[{linha}][{coluna}]')
# m_controle.sort()
print(m_controle)
print('\nFim do exercício 4')

###### Exercício 05 ######
import random
import time
matriz = []
m_controle = []
ctrl = bool
x = 5
t = x
rand = 50
for i in range(t):
    m_temp = []
    for n in range(t):
        temp = random.randint(0, rand)
        while m_controle.count(temp):
            temp = random.randint(0, rand)
        m_controle.append(temp)
        m_temp.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
    time.sleep(2)
num = int(input(f'Digite um número entre 0 e {rand} para ser verificada a ocorrencia nessa matriz: '))
for l in matriz:
    for c in l:
        if c == num:
            coluna = l.index(c)
            linha = matriz.index(l)
            ctrl = True
if ctrl is True:
    print(f'\nO número \033[1m{num}\033[0m existe => matriz[{linha}][{coluna}]')
else:
    print(f'\nO número \033[1m{num}\033[0m não foi encontrado na matriz')
# m_controle.sort()
# print(m_controle)
print('\nFim do exercício 5')

###### Exercício 06 ######
import random
import time
matriz = []
m_controle = []
matriz2 = []
matriz3 = []
t = 4
ini = 1
rand = 32
print('MATRIZ A')
for i in range(t):
    m_temp = []
    for n in range(t):
        temp = random.randint(ini, rand)
        while m_controle.count(temp):
            temp = random.randint(ini, rand)
        m_controle.append(temp)
        m_temp.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
print('\nMATRIZ B')
for i in range(t):
    m_temp = []
    for n in range(t):
        temp = random.randint(ini, rand)
        while m_controle.count(temp):
            temp = random.randint(ini, rand)
        m_controle.append(temp)
        m_temp.append(temp)
    matriz2.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
print('\nMATRIZ RESULTADO')
for li, val in enumerate(matriz):
    m_temp = []
    for c, _ in enumerate(val):
        if matriz[li][c] > matriz2[li][c]:
            m_temp.append(matriz[li][c])
        else:
            m_temp.append(matriz2[li][c])
    matriz3.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
print('\nFim do exercício 6')

###### Exercício 07 ######
import time
matriz = []
t = 10
for i in range(t):
    m_temp = []
    for j in range(t):
        if i == j:
            temp = 3 * (i ** 2) - 1
            m_temp.append(temp)
        if i < j:
            temp = 2 * i + 7 * j - 2
            m_temp.append(temp)
        if i > j:
            temp = 3 * (i ** 3) - 5 * (j ** 2) + 1
            m_temp.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
print('\nFim do exercício 7')

###### Exercício 08 ######
import time
import random
ini_rdm = 0
fim_rdm = 50
matriz = []
# m_controle = []
soma_acima = 0
t = 3
for i in range(t):
    m_temp = []
    for j in range(t):
        temp = random.randint(ini_rdm, fim_rdm)
        # while m_controle.count(temp):
        #     temp = random.randint(ini_rdm, fim_rdm)
        m_temp.append(temp)
        # m_controle.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
for li, val_li in enumerate(matriz):
    for co, val_co in enumerate(val_li):
        if li < co:
            soma_acima += matriz[li][co]
print(f'\nA soma dos elementos \033[1mACIMA\033[0m da diagonal principal é: {soma_acima}')
print('\nFim do exercício 8')

###### Exercício 09 ######
import time
import random
ini_rdm = 0
fim_rdm = 50
matriz = []
# m_controle = []
soma_abaixo = 0
t = 3
for i in range(t):
    m_temp = []
    for j in range(t):
        temp = random.randint(ini_rdm, fim_rdm)
        # while m_controle.count(temp):
        #     temp = random.randint(ini_rdm, fim_rdm)
        m_temp.append(temp)
        # m_controle.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
for li, val_li in enumerate(matriz):
    for co, val_co in enumerate(val_li):
        if li > co:
            soma_abaixo += matriz[li][co]
print(f'\nA soma dos elementos \033[1mABAIXO\033[0m da diagonal principal é: {soma_abaixo}')
print('\nFim do exercício 9')

###### Exercício 10 ######
import time
import random
ini_rdm = 10
fim_rdm = 50
matriz = []
# m_controle = []
soma_diagonal = 0
t = 3
for i in range(t):
    m_temp = []
    for j in range(t):
        temp = random.randint(ini_rdm, fim_rdm)
        # while m_controle.count(temp):
        #     temp = random.randint(ini_rdm, fim_rdm)
        m_temp.append(temp)
        # m_controle.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
for li, val_li in enumerate(matriz):
    for co, val_co in enumerate(val_li):
        if li == co:
            soma_diagonal += matriz[li][co]
print(f'\nA soma dos elementos da \033[1mDIAGONAL PRINCIPAL\033[0m é: {soma_diagonal}')
print('\nFim do exercício 10')

###### Exercício 11 ######
import time
import random
ini_rdm = 10
fim_rdm = 50
matriz = []
# m_controle = []
soma_diagonal_sec = 0
t = 3
for i in range(t):
    m_temp = []
    for j in range(t):
        temp = random.randint(ini_rdm, fim_rdm)
        # while m_controle.count(temp):
        #     temp = random.randint(ini_rdm, fim_rdm)
        m_temp.append(temp)
        # m_controle.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
for li, val_li in enumerate(matriz):
    for co, val_co in enumerate(val_li):
        if li + co == t - 1:
            soma_diagonal_sec += matriz[li][co]
print(f'\nA soma dos elementos da \033[1mDIAGONAL SECUNDÁRIA\033[0m é: {soma_diagonal_sec}')
print('\nFim do exercício 11')

###### Exercício 12 ######
import time
import random
ini_rdm = 10
fim_rdm = 50
matriz = []
# m_controle = []
matriz_trans = []
t = 3
print(f'MATRIZ ORIGINAL {t}x{t}')
for i in range(t):
    m_temp = []
    for j in range(t):
        temp = random.randint(ini_rdm, fim_rdm)
        # while m_controle.count(temp):
        #     temp = random.randint(ini_rdm, fim_rdm)
        m_temp.append(temp)
        # m_controle.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
print('\nMATRIZ TRANSPOSTA')
co = 0
while co < t:
    m_temp = []
    li = 0
    while li < t:
        temp = matriz[li][co]
        m_temp.append(temp)
        li += 1
    matriz_trans.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
    co += 1
print('\nFim do exercício 12')

###### Exercício 13 ######
import time
import random
ini_rdm = 1
fim_rdm = 20
matriz = []
# m_controle = []
matriz_tri_inf = []
t = 4
print(f'MATRIZ ORIGINAL {t}x{t}')
for i in range(t):
    m_temp = []
    for j in range(t):
        temp = random.randint(ini_rdm, fim_rdm)
        # while m_controle.count(temp):
        #     temp = random.randint(ini_rdm, fim_rdm)
        m_temp.append(temp)
        # m_controle.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
print('\nMATRIZ TRIANGULAR INFERIOR')
for li, var_li in enumerate(matriz):
    m_temp = []
    m_temp.extend(var_li.copy())
    for co, var_co in enumerate(var_li):
        if li < co:
            m_temp[co] = 0
    print(m_temp)
    time.sleep(0.5)
    matriz_tri_inf.append(m_temp.copy())
print('\nFim do exercício 13')

###### Exercício 14 ######
import time
import random
ini_rdm = 0
fim_rdm = 99
matriz = []
m_controle = []
t = 5
print(f'\nCARTELA BINGO {t}x{t}')
for i in range(t):
    m_temp = []
    for j in range(t):
        temp = random.randint(ini_rdm, fim_rdm)
        while m_controle.count(temp):
            temp = random.randint(ini_rdm, fim_rdm)
        m_temp.append(temp)
        m_controle.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
# m_controle.sort()
# print(f'\n{m_controle}')
print('\nFim do exercício 14')

###### Exercício 15 ######
import time
import random
opcoes = ['a', 'b', 'c', 'd']
alunos = []
gabarito = ['b', 'b', 'b', 'b', 'a', 'a', 'a', 'b', 'c', 'a']
resultado = []
alunos_qtt = 5
questoes = 10
# print(f'\nCARTELA BINGO {l}x{c}')
for i in range(alunos_qtt):
    m_temp = []
    for j in range(questoes):
        temp = random.choice(opcoes)
        m_temp.append(temp)
        # m_controle.append(temp)
    alunos.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
print(f'\n\033[1m{gabarito}\033[0m\n')
for li, val_li in enumerate(alunos):
    temp = 0
    for co, val_co in enumerate(val_li):
        if val_co == gabarito[co]:
            temp += 1
    resultado.append(temp)
    print(f'Aluno {li+1}: {temp}')
    time.sleep(0.5)
print(f'\n{resultado}')
#print(f'\n{alunos}')
# m_controle.sort()
# print(f'\n{m_controle}')
print('\nFim do exercício 15')

###### Exercício 16 ######
import time
import random
opcoes = ['a', 'b', 'c', 'd', 'e']
turma = []
gabarito = ['d', 'b', 'e', 'e', 'e', 'c', 'a', 'd', 'd', 'a']
resultado = []
alunos_qtt = 3
questoes = 10
aprovacao = 0
print()
for i in range(alunos_qtt):
    nota = 0
    m_temp = []
    aluno = []
    alu = input(f'Informe o nome do aluno: ')
    aluno.append(alu)
    matri = int(input(f'Informe a matrícula do aluno: '))
    print()
    aluno.append(matri)
    for j in range(questoes):
        temp = random.choice(opcoes)
        m_temp.append(temp)
        # m_controle.append(temp)
    # print(m_temp)
    aluno.append(m_temp.copy())
    for na in m_temp:
        if na == gabarito[i]:
            nota += 1
    aluno.append(nota)
    # time.sleep(0.5)
    # print(float(nota))
    if nota >= 7:
        aprovacao += 1
    turma.append(aluno.copy())
indice = (100 / alunos_qtt) * aprovacao
for g in range(alunos_qtt):
    print(f'\nAluno: {turma[g][0]}')
    time.sleep(0.2)
    print(f'Matrícula: {turma[g][1]}')
    time.sleep(0.2)
    print(f'Respostas: {turma[g][2]}')
    time.sleep(0.2)
    print(f'Nota: {turma[g][3]}')
    time.sleep(0.2)
print(f'\n\033[1m{gabarito}\033[0m\n')
print(f'Índice de Aprovação da Turma: {indice}%')
print('\nFim do exercício 16')

###### Exercício 17 ######
import time
import random
ini_rdm = 0
fim_rdm = 10
turma = []
resultado = []
alunos_qtt = 10
materias = 3
prova1 = 0
prova2 = 0
prova3 = 0
print()
for i in range(alunos_qtt):
    m_temp = []
    for j in range(materias):
        temp = random.randint(ini_rdm, fim_rdm)
        m_temp.append(temp)
        # m_controle.append(temp)
    print(m_temp)
    turma.append(m_temp.copy())
    time.sleep(0.5)
    if m_temp.index(min(m_temp)) == 0:
        prova1 += 1
    elif m_temp.index(min(m_temp)) == 1:
        prova2 += 1
    else:
        prova3 += 1
print(f'\n{prova1} alunos tiveram sua pior nota na 1ª Prova\n'
      f'{prova2} alunos tiveram sua pior nota na 2ª Prova\n'
      f'{prova3} alunos tiveram sua pior nota na 3ª Prova')
print('\nFim do exercício 17')

###### Exercício 18 ######
import time
import random
matriz = []
resultado = []
ini_rdm = -25
fim_rdm = 25
q = 3
print()
for i in range(q):
    m_temp = []
    for j in range(q):
        temp = random.randint(ini_rdm, fim_rdm)
        m_temp.append(temp)
        # m_controle.append(temp)
    print(m_temp)
    matriz.append(m_temp.copy())
    time.sleep(0.5)
co = 0
for g in range(q):
    li = 0
    soma = 0
    while li < q:
        soma += matriz[li][co]
        li += 1
    co += 1
    resultado.append(soma)
print()
print(resultado)
print('\nFim do exercício 18')

###### Exercício 19 ######
import time
import random
turma = [[1003, 3.0, 4.0, 7.0],
         [1004, 2.5, 5.0, 7.5],
         [1005, 3.5, 4.0, 7.5],
         [1006, 4.0, 4.5, 8.5],
         [1007, 4.0, 5.0, 9.0]]
alunos = 5
col = 0
# turma = []
# for i in range(alunos):
#     m_temp = []
#     matricula = int(input(f'Informe a matrícula do aluno: '))
#     m_temp.append(matricula)
#     media_provas =  float(input(f'Informe a média das provas do aluno: '))
#     m_temp.append(media_provas)
#     media_trabalhos = float(input(f'Informe a média dos trabalhos do aluno: '))
#     m_temp.append(media_trabalhos)
#     nota_final = media_provas + media_trabalhos
#     m_temp.append(nota_final)
#     turma.append(m_temp.copy())
#     print(m_temp, '\n')
print(turma)
nfinais = []
while col < 5:
    nfinais.append(turma[col][3])
    col += 1
print(nfinais)
print(f'\nA maior média final foi obtida pelo aluno de matrícula {turma[nfinais.index(max(nfinais))][0]} com a'
      f' nota {max(nfinais)}')
print(f'A Média final da turma foi {sum(nfinais)/alunos}')
print('\nFim do exercício 19')

###### Exercício 20 ######
import time
import random
linhas = 3
colunas = 6
matriz = []
matriz_sub = []
for i in range(linhas):
    m_temp = []
    for j in range(colunas):
        temp = float(input(f'Informe o elemento [{i}][{j}] da sua matriz[{linhas}]x[{colunas}]: '))
        m_temp.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
print()
print(matriz)
matriz_sub = matriz.copy()
col_impares = []
col_doisquatro = []
for li in range(linhas):
    for co in range(colunas):
        if (co + 1) % 2 == 1:
            col_impares.append(matriz[li][co])
        elif co + 1 == 2 or co + 1 == 4:
            col_doisquatro.append(matriz[li][co])
    matriz_sub[li][5] = matriz[li][0] + matriz[li][1]
print(f'Soma dos elementos das colunas ímpares: {sum(col_impares)}\n'
      f'Média dos elementos das colunas 2 e 4: {sum(col_doisquatro) / len(col_doisquatro)}')
print(f'Matriz alterada: {matriz_sub}')
print('\nFim do exercício 20')

###### Exercício 21 ######
import time
import random
linhas = 2
colunas = 2
m1 = []
m2 = []
m3 = []
for i in range(linhas):
    m_temp = []
    for j in range(colunas):
        temp = float(input(f'Informe o elemento [{i}][{j}] da 1ª matrix[{linhas}]x[{colunas}]: '))
        m_temp.append(temp)
    m1.append(m_temp.copy())
    print(m_temp)
print(m1)
print()
for i in range(linhas):
    m_temp = []
    for j in range(colunas):
        temp = float(input(f'Informe o elemento [{i}][{j}] da 2ª matrix[{linhas}]x[{colunas}]: '))
        m_temp.append(temp)
    m2.append(m_temp.copy())
    print(m_temp)
print(m2)
print()
time.sleep(1)
print('Escolha uma das opções abaixo:')
print('(a) somar as duas matrizes\n'
      '(b) subtrair a primeira matriz da segunda\n'
      '(c) adicionar uma constante às duas matrizes\n'
      '(d) imprimir matrizes')
opcao = input('(*) => ')
while opcao.lower() != 'a' and opcao.lower() != 'b' and opcao.lower() != 'c' and opcao.lower() != 'd':
    print('Caractere inválido!\nEscolha uma das opções abaixo:')
    print('(a) somar as duas matrizes\n'
          '(b) subtrair a primeira matriz da segunda\n'
          '(c) adicionar uma constante às duas matrizes\n'
          '(d) imprimir matrizes')
    opcao = input('(*) => ')
if opcao.lower() == 'a':
    print()
    for li in range(linhas):
        m_temp = []
        for co in range(colunas):
            m_temp.append(m1[li][co] + m2[li][co])
        m3.append(m_temp.copy())
        print(m_temp)
        time.sleep(0.5)
elif opcao.lower() == 'b':
    print()
    for li in range(linhas):
        m_temp = []
        for co in range(colunas):
            m_temp.append(m1[li][co] - m2[li][co])
        m3.append(m_temp.copy())
        print(m_temp)
        time.sleep(0.5)
elif opcao.lower() == 'c':
    print()
    c = int(input(f'Defina o valor da constante para adicionar às matrizes: '))
    print(m1)
    print('Matriz 1 - modificada')
    for li in range(linhas):
        m_temp = []
        for co in range(colunas):
            m1[li][co] = m1[li][co] * c
            m_temp.append(m1[li][co])
        print(m_temp)
        time.sleep(0.5)
    print()
    print(m2)
    print('Matriz 2 - modificada')
    for li in range(linhas):
        m_temp = []
        for co in range(colunas):
            m2[li][co] = m2[li][co] * c
            m_temp.append(m2[li][co])
        print(m_temp)
        time.sleep(0.5)
elif opcao.lower() == 'd':
    print()
    print(m1)
    print('Matriz 1')
    for li in range(linhas):
        m_temp = []
        for co in range(colunas):
            m_temp.append(m1[li][co])
        print(m_temp)
        time.sleep(0.5)
    print()
    print(m2)
    print('Matriz 2')
    for li in range(linhas):
        m_temp = []
        for co in range(colunas):
            m_temp.append(m2[li][co])
        print(m_temp)
        time.sleep(0.5)
print('\nFim do exercício 21')

###### Exercício 22 ######
import time
import random
linhas = 3
colunas = 3
m1 = []
m2 = []
m3 = []
for i in range(linhas):
    m_temp = []
    for j in range(colunas):
        temp = float(input(f'Informe o elemento [{i}][{j}] da matrix A[{linhas}]x[{colunas}]: '))
        m_temp.append(temp)
    m1.append(m_temp.copy())
    print(m_temp)
print(m1)
print()
for i in range(linhas):
    m_temp = []
    for j in range(colunas):
        temp = float(input(f'Informe o elemento [{i}][{j}] da matrix B[{linhas}]x[{colunas}]: '))
        m_temp.append(temp)
    m2.append(m_temp.copy())
    print(m_temp)
print(m2)
print()
time.sleep(1)
print('Matriz C (A * B)')
for li in range(linhas):
    m_temp = []
    for co in range(colunas):
        m_temp.append(m1[li][co] * m2[li][co])
    m3.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
print()
print(f'Matriz C = {m3}')
print('\nFim do exercício 22')

###### Exercício 23 ######
import time
import random
linhas = 3
colunas = 3
m1 = []
m2 = []
for i in range(linhas):
    m_temp = []
    for j in range(colunas):
        temp = float(input(f'Informe o elemento [{i}][{j}] da matrix A[{linhas}]x[{colunas}]: '))
        m_temp.append(temp)
    m1.append(m_temp.copy())
    print(m_temp)
print(m1)
print()
time.sleep(1)
print('Matriz B (A²)')
for li in range(linhas):
    m_temp = []
    for co in range(colunas):
        m_temp.append(m1[li][co] ** 2)
    m2.append(m_temp.copy())
    print(m_temp)
    time.sleep(0.5)
print()
print(f'Matriz B = {m2}')
print('\nFim do exercício 23')

###### Exercício 24 ######
import time
import random
linhas = 20
colunas = 20
m = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
     [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
     [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
     [52, 7, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
     [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
     [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
     [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
     [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
     [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
     [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
     [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
     [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
     [86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
     [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
     [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
     [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
     [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
     [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
     [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
     [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
maximos = []
horizontal = []
for li in range(linhas):
    for co in range(colunas - 3):
        horizontal.append(m[li][co] * m[li][co + 1] * m[li][co + 2] * m[li][co + 3])
max_horizontal = max(horizontal)
maximos.append(max_horizontal)
print(max_horizontal)
time.sleep(.6)
vertical = []
for li in range(linhas - 3):
    for co in range(colunas):
        vertical.append(m[li][co] * m[li + 1][co] * m[li + 2][co] * m[li + 3][co])
max_vertical = max(vertical)
maximos.append(max_vertical)
print(max_vertical)
time.sleep(.6)
diagonal_principal = []
for li in range(linhas - 3):
    for co in range(colunas- 3):
        diagonal_principal.append(m[li][co] * m[li - 1][co + 1] * m[li - 2][co + 2] * m[li - 3][co + 3])
max_diagonal_principal = max(diagonal_principal)
maximos.append(max_diagonal_principal)
print(max_diagonal_principal)
time.sleep(.6)
diagonal_secundaria = []
for li in range(linhas - 3):
    for co in range(colunas - 3):
        diagonal_secundaria.append(m[li][co] * m[li + 1][co + 1] * m[li + 2][co + 2] * m[li + 3][co + 3])
max_diagonal_secundaria = max(diagonal_secundaria)
maximos.append(max_diagonal_secundaria)
print(max_diagonal_secundaria)
time.sleep(.6)
print(f'O maior produto entre 4 elementos adjacentes nessa matriz é {max(maximos):,}')
print('\nFim do exercício 24')

import os
cont = 0
linhas = 3
colunas = 3
jogadas = []
resultados = []
controle = [0, 1, 2, 10, 11, 12, 20, 21, 22]
m = []
for li in range(linhas):
    m_temp = []
    for co in range(colunas):
        m_temp.append(0)
    m.append(m_temp.copy())
os.system('clear')
print('\n\033[1;33;40m JOGO DA VELHA \033[0m\n')
print(f'\033[1;36m{m[0]}         [00  01  02]\n'
      f'{m[1]}   ==>   [10  11  12]\n'
      f'{m[2]}         [20  21  22]\033[0m')
print()
print()
print(f'\033[32mJOGADOR A:\n'
      f'Escolha uma jogada de acordo com a tabela ao lado')
jogador = int(input(f'==>\033[0m '))
while controle.count(jogador) == 0:
    os.system('clear')
    print('\n\033[1;33;40m JOGO DA VELHA \033[0m\n')
    print(f'\033[1;36m{m[0]}         [00  01  02]\n'
         f'{m[1]}   ==>   [10  11  12]\n'
         f'{m[2]}         [20  21  22]\033[0m')
    print('\033[1;31;40m Numero inválido! \033[0m')
    print()
    print(f'\033[32mJOGADOR A:\n'
          f'Escolha uma jogada de acordo com a tabela ao lado')
    jogador = int(input(f'==>\033[0m '))
jogadas.append(jogador)
if jogador == 0:
    m[0][0] = 1
elif jogador == 1:
    m[0][1] = 1
elif jogador == 2:
    m[0][2] = 1
elif jogador == 10:
    m[1][0] = 1
elif jogador == 11:
    m[1][1] = 1
elif jogador == 12:
    m[1][2] = 1
elif jogador == 20:
    m[2][0] = 1
elif jogador == 21:
    m[2][1] = 1
elif jogador == 22:
    m[2][2] = 1
for li in range(3):
    resultados.append(m[li][0] + m[li][1] + m[li][2])
    resultados.append(m[0][li] + m[1][li] + m[2][li])
resultados.append(m[0][0] + m[1][1] + m[2][2])
resultados.append(m[2][0] + m[1][1] + m[0][2])
m_temp = []
m_temp.append(resultados.copy())
cont += 1
while resultados.count(3) == 0 and resultados.count(27) == 0 and len(jogadas) != 9:
    if cont % 2 == 1:
        os.system('clear')
        print('\n\033[1;33;40m JOGO DA VELHA \033[0m\n')
        print(f'\033[1;36m{m[0]}         [00  01  02]\n'
              f'{m[1]}   ==>   [10  11  12]\n'
              f'{m[2]}         [20  21  22]\033[0m')
        print()
        print(jogadas)
        print(f'\033[33mJOGADOR B:\n'
              f'Escolha uma jogada de acordo com a tabela ao lado')
        jogador = int(input(f'==> \033[0m'))
        while jogadas.count(jogador) != 0 or controle.count(jogador) == 0:
            os.system('clear')
            print('\n\033[1;33;40m JOGO DA VELHA \033[0m\n')
            print(f'\033[1;36m{m[0]}         [00  01  02]\n'
                  f'{m[1]}   ==>   [10  11  12]\n'
                  f'{m[2]}         [20  21  22]\033[0m')
            print('\033[1;31;40m Opa Jogador! Casa já ocupada ou número inválido! Escolha outro. \033[0m')
            print(jogadas)
            print(f'\033[33mJOGADOR B:\n'
                  f'Escolha uma jogada de acordo com a tabela ao lado')
            jogador = int(input(f'==>\033[0m '))
        jogadas.append(jogador)
        if jogador == 0:
            m[0][0] = 9
        elif jogador == 1:
            m[0][1] = 9
        elif jogador == 2:
            m[0][2] = 9
        elif jogador == 10:
            m[1][0] = 9
        elif jogador == 11:
            m[1][1] = 9
        elif jogador == 12:
            m[1][2] = 9
        elif jogador == 20:
            m[2][0] = 9
        elif jogador == 21:
            m[2][1] = 9
        elif jogador == 22:
            m[2][2] = 9
        for li in range(3):
            resultados.append(m[li][0] + m[li][1] + m[li][2])
            resultados.append(m[0][li] + m[1][li] + m[2][li])
        resultados.append(m[0][0] + m[1][1] + m[2][2])
        resultados.append(m[2][0] + m[1][1] + m[0][2])
        m_temp = []
        m_temp.append(resultados.copy())
    else:
        os.system('clear')
        print('\n\033[1;33;40m JOGO DA VELHA \033[0m\n')
        print(f'\033[1;36m{m[0]}         [00  01  02]\n'
              f'{m[1]}   ==>   [10  11  12]\n'
              f'{m[2]}         [20  21  22]\033[0m')
        print()
        print(jogadas)
        print(f'\033[32mJOGADOR A:\n'
              f'Escolha uma jogada de acordo com a tabela ao lado')
        jogador = int(input(f'==>\033[0m '))
        while jogadas.count(jogador) != 0 or controle.count(jogador) == 0:
            os.system('clear')
            print('\n\033[1;33;40m JOGO DA VELHA \033[0m\n')
            print(f'\033[1;36m{m[0]}         [00  01  02]\n'
                  f'{m[1]}   ==>   [10  11  12]\n'
                  f'{m[2]}         [20  21  22]\033[0m')
            print('\033[1;31;40m Opa Jogador! Casa já ocupada ou número inválido! Escolha outro. \033[0m')
            print(jogadas)
            print(f'\033[32mJOGADOR A:\n'
                  f'Escolha uma jogada de acordo com a tabela ao lado')
            jogador = int(input(f'==>\033[0m '))
        jogadas.append(jogador)
        if jogador == 0:
            m[0][0] = 1
        elif jogador == 1:
            m[0][1] = 1
        elif jogador == 2:
            m[0][2] = 1
        elif jogador == 10:
            m[1][0] = 1
        elif jogador == 11:
            m[1][1] = 1
        elif jogador == 12:
            m[1][2] = 1
        elif jogador == 20:
            m[2][0] = 1
        elif jogador == 21:
            m[2][1] = 1
        elif jogador == 22:
            m[2][2] = 1
        for li in range(3):
            resultados.append(m[li][0] + m[li][1] + m[li][2])
            resultados.append(m[0][li] + m[1][li] + m[2][li])
        resultados.append(m[0][0] + m[1][1] + m[2][2])
        resultados.append(m[2][0] + m[1][1] + m[0][2])
        m_temp = []
        m_temp.append(resultados.copy())
    cont += 1
os.system('clear')
if resultados.count(3) != 0:
    print('\n\033[40m O \033[1;32mJOGADOR A \033[0;0;40mé o \033[1;31mVENCEDOR \033[0m')
elif resultados.count(27) != 0:
    print('\n\033[40m O \033[1;33mJOGADOR B \033[0;0;40mé o \033[1;31mVENCEDOR \033[0m')
elif len(jogadas) == 9:
    print('\n\033[1;36;40m DEU VELHA!!!!\033[0;0;40m - Empate \033[0m')
print()
print(f'\033[1;36m{m[0]}         [00  01  02]\n'
      f'{m[1]}   ==>   [10  11  12]\n'
      f'{m[2]}         [20  21  22]\033[0m')
print('\nFim do exercício 25')





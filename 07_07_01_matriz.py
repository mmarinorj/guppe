matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz1[1][2])

for c1, c2, c3 in matriz1:
    print(f'{c1}  {c2}  {c3}')


##### GERAR UMA MATRIZ #####
# Forma 1
def gerar_matriz(n_linhas, n_colunas):
    return [[0] * n_colunas for _ in range(n_linhas)]


print(gerar_matriz(5, 5))

# Forma 2
import random
matriz = []
t = 3
ini = 1
rand = 32
m_controle = []
for i in range(t):  # Matriz quadrada onde t = numero de linhas e colunas
    m_temp = []
    for n in range(t):
        temp = random.randint(ini, rand)        # usando a biblioteca random para gerar automaticamente.
        while m_controle.count(temp):           # controle pra não repetir número na geração
            temp = random.randint(ini, rand)
        m_controle.append(temp)
        m_temp.append(temp)
    matriz.append(m_temp.copy())
    print(m_temp)
print(matriz)


#### ITERAR EM UMA MATRIZ #####
# Pegar os valores em uma matriz
for l in matriz:
     for c in l:
         if c > 10:
             print(c)

# Pegar os parâmetros de cada valor
for l, val_l in enumerate(matriz):
     for c, val_c in enumerate(val_l):
         if matriz[l][c] > 10:
             print(matriz[l][c])


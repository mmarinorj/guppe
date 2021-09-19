"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do móduo os.

os -> Operating System - Sistema Operacional
"""
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())  # /home/marcelo/PycharmProjects/guppe/secao13

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())  # /home/marcelo/PycharmProjects/guppe


os.chdir('..')

print(os.getcwd())  # /home/marcelo/PycharmProjects


os.chdir('..')

print(os.getcwd())  # /home/marcelo

os.chdir('..')

print(os.getcwd())  # /home


os.chdir('..')

print(os.getcwd())  # /


os.chdir('..')

print(os.getcwd())  # /

os.chdir('/home/marcelo/PycharmProjects/guppe/secao13')

print(os.getcwd())  # /home/marcelo/PycharmProjects/guppe/secao13

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('/home/geek/'))  # True

# OBS para usuários Windows
# Se você, infelizmente, estiver utilizando um computador com Windows,
# terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('C:\\Users\\geek'))

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix (Linux e Mac), nt (Windows)

# Podemos ter mais detalhes no sistema operacional
print(os.uname())

# Fazer o import
import sys

print(sys.platform)

# '/home/marcelo/workspace/sistema'

print(os.getcwd())  # /home/marcelo/PycharmProjects/guppe/secao13

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd())  # /home/marcelo/PycharmProjects/guppe/secao13/geek/university

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o
# diretório que será juntado ao atual.

# Podemos listar os arquivos e diretórios com o listdir()

print(os.listdir('/home/marcelo/PycharmProjects/guppe/secao13'))
print(len(os.listdir('/home/marcelo/PycharmProjects/guppe/secao13')))


# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir('/home/marcelo/PycharmProjects/guppe/secao11')

arquivos = list(scanner)

print(arquivos)

print(arquivos[1])

print(dir(arquivos[1]))


print(arquivos[1].inode())  # ??
print(arquivos[1].is_dir())  # É um diretório? False
print(arquivos[1].is_file())  # É um arquivo? True
print(arquivos[1].is_symlink())  # É um link simbólico? False
print(arquivos[1].name)  # Nome do arquivo
print(arquivos[1].path)  # Caminho até o arquivo
print(arquivos[1].stat())  # Estatísticas...
#
# # OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo.
#
scanner.close()

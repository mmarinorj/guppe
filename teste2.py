from os import system, name

def limpar_Tela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


limpar_Tela()




n = int(input('\nQuantas frases você deseja verificar? '))
simbolo = ['!', '.', '?', '...']
for i in range(n):
    cont = 0
    entrada = input(f'\nDigite sua {i+1}ª frase: ')
    for i in range(len(simbolo)):
        if simbolo[i] in entrada:
            cont += 1
    if cont != 0:
        print('Frase completa')
    else:
        print('Frase mal elaborada')





n = int(input('\nQuantas frases você deseja verificar? '))
simbolo = ['!', '.', '?', '...', ',']
for i in range(n):
    simb = []
    cont = 0
    entrada = input(f'\nDigite sua {i+1}ª frase: ')
    for i in range(len(simbolo)):
        if simbolo[i] in entrada:
            cont += 1
            simb.append(simbolo[i])
    if cont != 0:
        print(f'Frase completa => {cont} símbolo(s) encontrado(s) na frase: {simb[::-1]}')
    else:
        print('Frase mal elaborada')



# cadastro = [{'nome':'Marcelo', 'sexo':'M', 'idade':47}, {'nome':'Marcio', 'sexo':'M', 'idade':35}, {'nome':'Luciana', 'sexo':'F', 'idade':41}, {'nome':'Isabela', 'sexo':'F', 'idade':7}]
# from os import system, name


# cadastro = []


# def limpar_Tela():
#     if name == 'nt':
#         system('cls')
#     else:
#         system('clear')


# def cadastro_pessoas():
#     global cadastro
#     pessoa = dict()
#     print('CADASTRO DE PESSOAS\n')
#     pessoa['nome'] = input('Nome: ').capitalize()
#     pessoa['sexo'] = input('Sexo [M/F]: ').upper()
#     while len(pessoa['sexo']) > 1:
#         while pessoa['sexo'] not in 'MN':
#             pessoa['sexo'] = input('Erro! Digite apenas uma das duas letras\nSexo [M/F]: ').upper()
#     pessoa['idade'] = int(input('Idade: '))
#     cadastro.append(pessoa)


# def cadastros():
#     return len(cadastro)


# def media_idade():
#     soma_idades = 0
#     for i in cadastro:
#         soma_idades += i['idade']
#     return (soma_idades / len(cadastro))


# def acima_media():
#     global cadastro
#     acima = []
#     for i in cadastro:
#         if i['idade'] > media_idade():
#             acima.append(i['idade'])
#     return acima


# def mulheres():
#     global cadastro
#     cont = 0
#     for i in cadastro:
#         if i['sexo'] == 'F':
#             cont += 1
#     return cont


# n = int
# while n != 0:
#     limpar_Tela()
#     n = int(input(f'[ 1 ] Cadastro\n'
#                   f'[ 2 ] Relatórios\n'
#                   f'[ 0 ] Sair\n'
#                   f'\nEscolha um número: '))
#     limpar_Tela()
#     if n == 1:
#         e = int
#         while e != 0:
#             cadastro_pessoas()
#             try:
#                 e = int(input('Tecle 0 + "ENTER" para retornar ao menu inicial ou apenas "ENTER" para continuar'))
#             except ValueError:
#                 pass
#             limpar_Tela()
#     elif n == 2:
#         limpar_Tela()
#         print('RELATÓRIO')
#         print(42 * '#')
#         print(f'Pessoas cadastradas até o momento: {cadastros()}\n'
#               f'Média de idade dos cadastrados: {media_idade()}\n'
#               f'Mulheres cadastradas: {mulheres()}\n'
#               f'Idades acima da média: {acima_media()}')
#         print(42 * '#')
#         input('...')

# limpar_Tela()
# input('bye bye!')






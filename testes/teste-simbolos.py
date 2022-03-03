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
    for i in simbolo:
        if i in entrada:
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

import os
a = 0
b = 0
cor = 45


def jogo_da_velha():
    global a, b, cor

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
    print()
    print(f'\033[1;33;40m JOGO DA VELHA \033[0m\n'
          f'                                    \033[1;1;{cor}m                         \033[0m\n'
          f'  \033[1;36m{m[0]}         \033[0;35m[00  01  02]    \033[1;1;{cor}m  \033[1;39;40m   '
          f'    PLACAR        \033[0m\033[1;1;{cor}m  \033[0m\n'
          f'  \033[1;36m{m[1]}   \033[1;35m==>\033[0m   \033[35m[10  11  12]    \033[1;1;{cor}m  \033'
          f'[1;32;40m VERDE\033[1;0;40m   x   \033[1;33;40mAMARELO \033[0m\033[1;1;{cor}m  \033[0m\n'
          f'  \033[1;36m{m[2]}         \033[0;35m[20  21  22]\033[0m    \033[1;1;{cor}m  \033[1;39;40m'
          f'   {a}            {b}    \033[0m\033[1;1;{cor}m  \033[0m\n'
          f'                                    \033[1;1;{cor}m                         \033[0m')
    print()
    print()
    print(f'\033[32mVERDE:\n'
          f'Escolha uma jogada de acordo com a tabela ao lado')
    jogador = int(input(f'==>\033[0m '))
    while controle.count(jogador) == 0:
        os.system('clear')
        print()
        print(f'\033[1;33;40m JOGO DA VELHA \033[0m\n'
              f'                                    \033[1;1;{cor}m                         \033[0m\n'
              f'  \033[1;36m{m[0]}         \033[0;35m[00  01  02]    \033[1;1;{cor}m  \033[1;39;40m   '
              f'    PLACAR        \033[0m\033[1;1;{cor}m  \033[0m\n'
              f'  \033[1;36m{m[1]}   \033[1;35m==>\033[0m   \033[35m[10  11  12]    \033[1;1;{cor}m  \033'
              f'[1;32;40m VERDE\033[1;0;40m   x   \033[1;33;40mAMARELO \033[0m\033[1;1;{cor}m  \033[0m\n'
              f'  \033[1;36m{m[2]}         \033[0;35m[20  21  22]\033[0m    \033[1;1;{cor}m  \033[1;39;40m'
              f'   {a}            {b}    \033[0m\033[1;1;{cor}m  \033[0m\n'
              f'                                    \033[1;1;{cor}m                         \033[0m')
        print()
        print()
        print(f'\033[32mVERDE:\n'
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
            print()
            print(f'\033[1;33;40m JOGO DA VELHA \033[0m\n'
                  f'                                    \033[1;1;{cor}m                         \033[0m\n'
                  f'  \033[1;36m{m[0]}         \033[0;35m[00  01  02]    \033[1;1;{cor}m  \033[1;39;40m   '
                  f'    PLACAR        \033[0m\033[1;1;{cor}m  \033[0m\n'
                  f'  \033[1;36m{m[1]}   \033[1;35m==>\033[0m   \033[35m[10  11  12]    \033[1;1;{cor}m  \033'
                  f'[1;32;40m VERDE\033[1;0;40m   x   \033[1;33;40mAMARELO \033[0m\033[1;1;{cor}m  \033[0m\n'
                  f'  \033[1;36m{m[2]}         \033[0;35m[20  21  22]\033[0m    \033[1;1;{cor}m  \033[1;39;40m'
                  f'   {a}            {b}    \033[0m\033[1;1;{cor}m  \033[0m\n'
                  f'                                    \033[1;1;{cor}m                         \033[0m')
            print()
            print(jogadas)
            print(f'\033[33mAMARELO:\n'
                  f'Escolha uma jogada de acordo com a tabela ao lado')
            jogador = int(input(f'==> \033[0m'))
            while jogadas.count(jogador) != 0 or controle.count(jogador) == 0:
                os.system('clear')
                print()
                print(f'\033[1;33;40m JOGO DA VELHA \033[0m\n'
                      f'                                    \033[1;1;{cor}m                         \033[0m\n'
                      f'  \033[1;36m{m[0]}         \033[0;35m[00  01  02]    \033[1;1;{cor}m  \033[1;39;40m   '
                      f'    PLACAR        \033[0m\033[1;1;{cor}m  \033[0m\n'
                      f'  \033[1;36m{m[1]}   \033[1;35m==>\033[0m   \033[35m[10  11  12]    \033[1;1;{cor}m  \033'
                      f'[1;32;40m VERDE\033[1;0;40m   x   \033[1;33;40mAMARELO \033[0m\033[1;1;{cor}m  \033[0m\n'
                      f'  \033[1;36m{m[2]}         \033[0;35m[20  21  22]\033[0m    \033[1;1;{cor}m  \033[1;39;40m'
                      f'   {a}            {b}    \033[0m\033[1;1;{cor}m  \033[0m\n'
                      f'                                    \033[1;1;{cor}m                         \033[0m')
                print('\033[1;31;40m Opa Jogador! Casa já ocupada ou número inválido! Escolha outro. \033[0m')
                print(jogadas)
                print(f'\033[33mAMARELO:\n'
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
            print()
            print(f'\033[1;33;40m JOGO DA VELHA \033[0m\n'
                  f'                                    \033[1;1;{cor}m                         \033[0m\n'
                  f'  \033[1;36m{m[0]}         \033[0;35m[00  01  02]    \033[1;1;{cor}m  \033[1;39;40m   '
                  f'    PLACAR        \033[0m\033[1;1;{cor}m  \033[0m\n'
                  f'  \033[1;36m{m[1]}   \033[1;35m==>\033[0m   \033[35m[10  11  12]    \033[1;1;{cor}m  \033'
                  f'[1;32;40m VERDE\033[1;0;40m   x   \033[1;33;40mAMARELO \033[0m\033[1;1;{cor}m  \033[0m\n'
                  f'  \033[1;36m{m[2]}         \033[0;35m[20  21  22]\033[0m    \033[1;1;{cor}m  \033[1;39;40m'
                  f'   {a}            {b}    \033[0m\033[1;1;{cor}m  \033[0m\n'
                  f'                                    \033[1;1;{cor}m                         \033[0m')
            print()
            print(jogadas)
            print(f'\033[32mVERDE:\n'
                  f'Escolha uma jogada de acordo com a tabela ao lado')
            jogador = int(input(f'==>\033[0m '))
            while jogadas.count(jogador) != 0 or controle.count(jogador) == 0:
                os.system('clear')
                print()
                print(f'\033[1;33;40m JOGO DA VELHA \033[0m\n'
                      f'                                    \033[1;1;{cor}m                         \033[0m\n'
                      f'  \033[1;36m{m[0]}         \033[0;35m[00  01  02]    \033[1;1;{cor}m  \033[1;39;40m   '
                      f'    PLACAR        \033[0m\033[1;1;{cor}m  \033[0m\n'
                      f'  \033[1;36m{m[1]}   \033[1;35m==>\033[0m   \033[35m[10  11  12]    \033[1;1;{cor}m  \033'
                      f'[1;32;40m VERDE\033[1;0;40m   x   \033[1;33;40mAMARELO \033[0m\033[1;1;{cor}m  \033[0m\n'
                      f'  \033[1;36m{m[2]}         \033[0;35m[20  21  22]\033[0m    \033[1;1;{cor}m  \033[1;39;40m'
                      f'   {a}            {b}    \033[0m\033[1;1;{cor}m  \033[0m\n'
                      f'                                    \033[1;1;{cor}m                         \033[0m')
                print('\033[1;31;40m Opa Jogador! Casa já ocupada ou número inválido! Escolha outro. \033[0m')
                print(jogadas)
                print(f'\033[32mVERDE:\n'
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
        print('\n\033[40m O \033[1;32mVERDE \033[0;0;40mé o \033[1;31mVENCEDOR \033[0m')
        a += 1
    elif resultados.count(27) != 0:
        print('\n\033[40m O \033[1;33mAMARELO \033[0;0;40mé o \033[1;31mVENCEDOR \033[0m')
        b += 1
    elif len(jogadas) == 9:
        print('\n\033[1;36;40m DEU VELHA!!!!\033[0;0;40m - Empate \033[0m')
    if a > b:
        cor = 42
    elif a < b:
        cor = 43
    else:
        cor = 45
    print(f'                                    \033[1;1;{cor}m                         \033[0m\n'
          f'  \033[1;36m{m[0]}         \033[0;35m[00  01  02]    \033[1;1;{cor}m  \033[1;39;40m   '
          f'    PLACAR        \033[0m\033[1;1;{cor}m  \033[0m\n'
          f'  \033[1;36m{m[1]}   \033[1;35m==>\033[0m   \033[35m[10  11  12]    \033[1;1;{cor}m  \033'
          f'[1;32;40m VERDE\033[1;0;40m   x   \033[1;33;40mAMARELO \033[0m\033[1;1;{cor}m  \033[0m\n'
          f'  \033[1;36m{m[2]}         \033[0;35m[20  21  22]\033[0m    \033[1;1;{cor}m  \033[1;39;40m'
          f'   {a}            {b}    \033[0m\033[1;1;{cor}m  \033[0m\n'
          f'                                    \033[1;1;{cor}m                         \033[0m')


def reiniciar_jogo():
    global reiniciar
    while reiniciar != 'n':
        jogo_da_velha()
        reiniciar = input(f'\n\033[1;40m Continuar partida? (s/n): \033[0m')
        while reiniciar.lower() != 's' and reiniciar.lower() != 'n':
            print('\033[1;31;40m Tecla inválida! \033[0m')
            reiniciar = input(f'\033[1;40m Continuar partida? (s/n): \033[0m')
        if reiniciar == 's':
            reiniciar_jogo()
    return


jogo_da_velha()
reiniciar = input(f'\n\033[1;40m Continuar partida? (s/n): \033[0m')
while reiniciar.lower() != 's' and reiniciar.lower() != 'n':
    print('\033[1;31;40m Tecla inválida! \033[0m')
    reiniciar = input(f'\033[1;40m Continuar partida? (s/n): \033[0m')
if reiniciar == 's':
    reiniciar_jogo()
input('\033[1;31;40m Bye, bye!!!... ')

n = int(input())

lisdenum = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

lisdeletras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'X', 'Z']

for i in range(n):
    placa = input()
    letras = []
    numeros = []

    caract = verifica = pos = veri = 0
    for k in range(len(placa)):
        if placa[k] != ('-'):
            letras.append(placa[k])
        else:
            caract = 1
            pos = k
            break
        
    for o in range(pos, len(placa)):
        num.append(placa[0])
        num.remove(lisdenum[0])
        for i in range(len(letras)):
            if(letras[1] in lisdeletras):
                verifica = 1
            else:
                verifica = 0
                break
    for p in range(len(numeros)):
        if(numeros[p] in lisdenum):
            veri = 1
    else:
        veri = 0
        break

    if(len(placa) !=8):
        print("ERRO")
    elif(verifica == 0):
        print("ERRO")
    elif(veri == 0):
        print("ERRO")
    elif(caract == 0):
        print("ERRO")
    elif(placa[7] == '1' or placa[7] ==  '2'):
        print("SEGUNDA FEIRA")
    elif(placa[7] == '3' or placa[7] == '4'):
        print("TERÇA FEIRA")
    elif(placa[7] == '5' or placa[7] == '6'):
        print("QUARTA FEIRA")
    elif(placa[7] == '7' or placa[7] == '8'):
        print("QUINTA FEIRA")
    else:
        print("ERRO")

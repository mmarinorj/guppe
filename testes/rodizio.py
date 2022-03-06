def Hifen(placa):
    if(len(placa) < 8 or placa[3] != '-'): return False

def TamanLetras(placa):
    letras = placa.split('-')[0]
    if(len(letras) != 3):
        return False

def Num(placa):
    numeros = placa.split('-')[1]
    for numero in numeros:
        if(ord(numero)>57 or ord(numero)<48):
            return False

def Carac(placa):
    letras = placa.split('-')[0]
    for caracter in letras:
        if(ord(caracter)>90 or ord(caracter)<64):
            return False

def TamanNumeros(placa):
    numeros = placa.split('-')[1]
    if(len(numeros) != 4):
        return False

def diaRodizio(placa):
    numeros = placa.split('-')[1]
    if('1'<=numeros[3]<='2'): dia = "SEGUNDA"
    if('3'<=numeros[3]<='4'): dia = "TERÇA"
    if('5'<=numeros[3]<='6'): dia = "QUARTA"
    if('7'<=numeros[3]<='8'): dia = "QUINTA"
    if(numeros[3]=='9' or numeros[3]=='0'): dia = "SEXTA"
    return dia                                            # AO INVÉS DE IMPRIMIR, MANDEI ELE RETORNAR

# CRIEI ESSAS DUAS LISTAS. UMA DELAS COM INPUT NO FORMATO => PLACA,PLACA,PLACA,...PLACA
lista_resultado = []
lista_placas = input('Informe a lista de placas: ').split(',')

for placa in lista_placas:
    if (
            Hifen(placa) == False or
            TamanLetras(placa) == False or
            Carac(placa) == False or
            Num(placa) == False or
            TamanNumeros(placa) == False):
        lista_resultado.append("ERRO")                  # AO INVÉS DE IMPRIMIR O ERRO, MANDEI ELE DAR O APPEND NA LISTA DE RESULTADOS
    else:
        lista_resultado.append(diaRodizio(placa))       # AO INVÉS DE IMPRIMIR O DIA, MANDEI ELE DAR O APPEND NA LISTA DE RESULTADOS

print(lista_resultado)                                  # IMPRIMI A LISTA DE RESULTADOS

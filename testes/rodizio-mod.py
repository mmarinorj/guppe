

def hifen(placa):
    if len(placa) < 8 or placa[3] != '-':
        return False


def parte_letras(placa):
    letras = placa.split('-')[0]
    if len(letras) == 3:
        for caracter in letras:
            if ord(caracter) > 90 or ord(caracter) < 64:
                return False
    else:
        return False


def parte_num(placa):
    numeros = placa.split('-')[1]
    if len(numeros) == 4:
        for numero in numeros:
            if ord(numero) > 57 or ord(numero) < 48:
                return False
    else:
        return False


def dia_rodizio(placa):
    dia = ""
    numeros = placa.split('-')[1]
    if '1' <= numeros[3] <= '2':
        dia = "SEGUNDA"
    if '3' <= numeros[3] <= '4':
        dia = "TERÇA"
    if '5' <= numeros[3] <= '6':
        dia = "QUARTA"
    if '7' <= numeros[3] <= '8':
        dia = "QUINTA"
    if numeros[3] == '9' or numeros[3] == '0':
        dia = "SEXTA"
    return dia


lista_resultado = []
lista_placas = input('Informe as lista de placas: ').split(',')

for placa in lista_placas:
    if hifen(placa) is False or parte_num(placa) is False or parte_letras(placa) is False:
        lista_resultado.append("ERRO")
    else:
        lista_resultado.append(dia_rodizio(placa))

print(lista_resultado)

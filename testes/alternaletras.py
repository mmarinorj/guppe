def alterna_letras(frase):
    
    """função que recebe como entrada uma setença e a transforme na escrita apropriada dos
    anos 2000, alternando às letras entre maiúsculas e minúsculas
    str -> str"""
    
    frase_modificada = ""
    contador = 0
    for letra in frase:
        if letra == " ":
            frase_modificada += " "
        elif contador%2 == 0:
            contador += 1
            frase_modificada += letra.upper()
        else:
            contador -= 1
            frase_modificada += letra.lower()
    return frase_modificada

print(alterna_letras("Acho que estou me apaixonando por você..."))


def repetidos(lista, objeto):
    nova = []
    if type(objeto) == list:
        for obj in objeto:
            for l in lista:
                if l == obj:
                    nova.append(l)
    else:
        for l in lista:
            if l == objeto:
                nova.append(l)
    return nova


class Lista:

    def __init__(self, lista, objeto):
        self.objeto = objeto
        self.lista = lista
        self.nova = []

    def repetidos2(self):
        if type(self.objeto) == list:
            for obj in self.objeto:
                for l in self.lista:
                    if l == obj:
                        self.nova.append(l)
        else:
            for l in self.lista:
                if l == self.objeto:
                    self.nova.append(l)
        return self.nova

if __name__ == '__main__':
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    test = Lista(letras, 'a')
    print(Lista(letras, 'a').repetidos2())

    print(repetidos(letras, ['a', 'b', 'z', 'o', 'g', 'm']))

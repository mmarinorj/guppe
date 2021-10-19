"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular -> cápsula (cada Classe é uma cápsula com seus atributos e métodos)

Abstrair -> é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de usuário.
"""


class ContaCorrente:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = ContaCorrente.contador
        self.__titular = titular
        self.__saldo = int(saldo)
        self.__limite = limite
        self.__limite_conta = limite
        ContaCorrente.contador += 1

    def extrato(self):
        print(f'Saldo de R$ {self.__saldo},00 do titular {self.__titular} com limite de R$ {self.__limite},00.')

    def depositar(self, valor):
        if valor > 0:
            if self.__limite == self.__limite_conta:
                self.__saldo += valor
            elif self.__limite + valor >= self.__limite_conta:
                self.__limite = self.__limite_conta
                self.__saldo += valor
            else:
                self.__saldo += valor
                self.__limite += valor
        else:
            print('Inserir um número positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= 0:
                if valor > self.__saldo + self.__limite:
                    print('Saldo insuficiente!')
                else:
                    self.__saldo -= valor
                if self.__saldo < 0:
                    self.__limite += self.__saldo
            else:
                if valor > self.__limite:
                    print('Saldo insuficiente!')
                else:
                    self.__saldo -= valor
                    self.__limite -= valor
        else:
            print('Inserir um número positivo')

    def transfere(self, valor, conta_destino):
        if valor > 0:
            if self.__saldo >= 0:
                if valor > self.__saldo + self.__limite:
                    print('Saldo insuficiente!')
                else:
                    self.__saldo -= valor
                if self.__saldo < 0:
                    self.__limite += self.__saldo
            else:
                if valor > self.__limite:
                    print('Saldo insuficiente!')
                else:
                    self.__saldo -= valor
                    self.__limite -= valor
            if conta_destino.__limite == conta_destino.__limite_conta:
                conta_destino.__saldo += valor
            elif conta_destino.__limite + valor >= conta_destino.__limite_conta:
                conta_destino.__limite = conta_destino.__limite_conta
                conta_destino.__saldo += valor
            else:
                conta_destino.__saldo += valor
                conta_destino.__limite += valor
        else:
            print('Inserir um número positivo')


# Testando

conta1 = ContaCorrente('Angelina', 4500.00, 1500)

print(conta1._ContaCorrente__numero)   # Name Mangling
# print(conta1.titular)
# print(conta1.saldo)
# print(conta1.limite)
conta1.extrato()

conta1.depositar(200)
# print(conta1.saldo)
conta1.extrato()

conta1.sacar(50)
# print(conta1.saldo)
conta1.extrato()

conta2 = ContaCorrente('Marcelo', 2500.00, 5000)

# print(conta2.numero)
# print(conta2.titular)
# print(conta2.saldo)
# print(conta2.limite)
conta2.extrato()

conta2.depositar(450)
# print(conta2.saldo)
conta2.extrato()

conta2.sacar(2950)
# print(conta2.saldo)
conta2.extrato()
conta2.sacar(1500)
conta2.extrato()
conta2.sacar(3500)
conta2.extrato()
conta2.depositar(200)
conta1.extrato()
conta2.extrato()
conta1.transfere(4650, conta2)
conta1.extrato()
conta2.extrato()

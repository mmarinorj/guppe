"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também estender nossas classes.

OBS: Com a herança, a partir de uma classe existente nós estendemos outra classe que passa a herdar atributos e métodos
da classe herdada.


Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda

Funcionario:
    - nome;
    - sobrenome;
    - cpf;
    - matricula;

OBS: * Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada.

     * Essa classe herdada é conhecida por:
        - Super Classe;
        - Classe Mãe;
        - Classe Pai;
        - Classe Base;
        - Classe Genérica;

     * A Classe que herda é conhecida por:
        - Sub Classe;
        - Classe Filha;
        - Classe Específica;

# Sobrescrita de Métodos (Overriding)
Sobrescrita de método ocorre quando reescrevemos/reimplementamos um método presente na super classe em classes filhas

"""

# class Cliente:
#
#     def __init__(self, nome, sobrenome, cpf, renda):
#         self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__cpf = cpf
#         self.__renda = renda
#
#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'
#
#
# class Funcionario:
#
#     def __init__(self, nome, sobrenome, cpf, matricula):
#         self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__cpf = cpf
#         self.__matricula = matricula
#
#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'


# Refatorando e implementando a super classe


# class Pessoa:
#
#     def __init__(self, nome, sobrenome, cpf):
#         self.__nome = nome
#         self.__sobrenome = sobrenome
#         self.__cpf = cpf
#
#     def nome_completo(self):
#         return f'{self.__nome} {self.__sobrenome}'
#
#
# class Cliente(Pessoa):
#     """Cliente herda de Pessoa"""
#     def __init__(self, nome, sobrenome, cpf, renda):
#         super().__init__(nome, sobrenome, cpf)            # Forma comum de acessar dados da super classe
#         self.__renda = renda
#
#
# class Funcionario(Pessoa):
#     """Funcionario herda de Pessoa"""
#     def __init__(self, nome, sobrenome, cpf, matricula):
#         Pessoa.__init__(self, nome, sobrenome, cpf)      # Forma NÃO comum de acessar dados da super classe
#         self.__matricula = matricula
#
#
# cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
# funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-00', 1234)
#
# print(cliente1.nome_completo())
# print(funcionario1.nome_completo())
#
# print(cliente1.__dict__)
# print(funcionario1.__dict__)

# Sobrescrita de Métodos (Overriding)


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-00', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

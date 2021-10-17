"""
POO - Métodos

Métodos (funções) -> Representam os comportamentos dos Objetos. Ou seja, as ações que este objeto pode realizar no seu
sistema.

Em Python, dividimos os métodos em dois grupos:
- Métodos de Instância;
- Métodos de Classe;

# Métodos de Instância

# O método dunder init (__init__) é um método especial chamado construtor e sua função é construir o objeto a partir
da classe.

OBS1: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

OBS2: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO! Por mais que possamos criar nossas próprias funções utilizando "dunder" não é aconselhavel. Python possui
vários métodos com essa nomenclatura e pode ser que mudemos o comportamento dessas funções mágicas internas da
linguagem. Então evite ao máximo. De preferência, nunca o faça.

# Métodos são escritos em minúsculas. Se o nome for composto será separado por underline.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


# p1 = Produto('PlayStation 4', 'Video Game', 2300)
# print(p1.desconto(50))
#
# print(Produto.desconto(p1, 30))   # self, desconto
#
#
# user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', 123456)
# user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', 678945)
#
# print(user1.nome_completo())
#
# print(Usuario.nome_completo(user2))
#
# print(user2.nome_completo())
#
# print(f'Senha User 1: {user1._Usuario__senha}')   # Acesso de forma errada de um atributo de classe
# print(f'Senha User 2: {user2._Usuario__senha}')   # Acesso de forma errada de um atributo de classe

# nome = input('Informe o nome: ')
# sobrenome = input('Informe o sobrenome: ')
# email = input('Informe o email: ')
# senha = input('Informe a senha: ')
# confirma_senha = input('Confirme a senha: ')
#
# while senha != confirma_senha:
#     print('Senha não confere')
#     senha = input('Informe a senha: ')
#     confirma_senha = input('Confirme a senha: ')
#
# user = Usuario(nome, sobrenome, email, senha)
# print('Usuário criado com sucesso!')
#
# senha = input('Informe a senha para acesso: ')
#
# if user.checa_senha(senha):
#     print('Acesso permitido!')
# else:
#     print('Acesso negado.')
#
# print(f'Senha User Criptografada: {user._Usuario__senha}')  # Acesso de forma errada de um atributo de classe


# Métodos de Classe -> Em Python são conhecidos como métodos estáticos em outras linguagens.


class UsuarioRefatorado:

    contador = 0
    @classmethod
    def conta_usuarios(cls):
        print(f'Classes: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = UsuarioRefatorado.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        UsuarioRefatorado.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


user3 = UsuarioRefatorado('Felicity', 'Jones', 'felicity@gmail.com', '123456')

UsuarioRefatorado.conta_usuarios()   # Forma correta
user3.conta_usuarios()               # Possível mas incorreta


class UsuarioRefatoradoPrivado:

    contador = 0
    @classmethod
    def conta_usuarios(cls):
        print(f'Classes: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = UsuarioRefatoradoPrivado.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        UsuarioRefatoradoPrivado.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


user4 = UsuarioRefatoradoPrivado('Felicity', 'Jones', 'felicity@gmail.com', '123456')

print(user4._UsuarioRefatoradoPrivado__gera_usuario())   # Acesso de forma errada porém possível (Name Mangling)


# Método Estático

print(UsuarioRefatoradoPrivado.contador)
print(UsuarioRefatoradoPrivado.definicao())

user5 = UsuarioRefatoradoPrivado('Angelia', 'Jolie', 'angelina@gmail.com', '789654')

print(user5.contador)
print(user5.definicao())

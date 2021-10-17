"""
POO - Atributos

Atributos -> representam as características do objeto. Ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
- Atributos de Instância;
- Atributos de Classe;
- Atributos Dinâmicos;


# Atributos de instância: São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial utilizado para a construção do objeto.


# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    public String cor;
    protected Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público. Ou seja, pode ser acessado
em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser
acessado/utilizado dentro da da própria classe onde está declarado, utiliza-se __ (duplo underscore)
no início de seu nome.

Isso é conhecido também como Name Mangling.

class Lampada:

    def __init__(self, voltagem, cor):   # Método construtor
        self.__voltagem = voltagem       # __ faz com que o atributo seja privado, ou seja, acesso somente dentro
        self.__cor = cor                 # # da Classe.
        self.__ligada = False

"""


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Públicos e Atributos Privados


class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos acesso
# aos atributos sinalizados como privados fora da classe.

# Exemplo


user = Acesso('user@gmail.com', '123456')

print(user.email)

# print(user.__senha)   # AttributeError

print(dir(user))

print(user._Acesso__senha)   # Temos acesso mas não deveríamos fazê-lo. (Name Mangling)

user.mostra_senha()
user.mostra_email()


# O que significa atributos de instância?

# Significa que, ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.

user1 = Acesso('user1@gmail.com', '789456')
user2 = Acesso('user2@gmail.com', '987321')

user1.mostra_email()
user2.mostra_email()


# Atributos de Classe

# são atributos declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos um valor e
# este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada instÂncia da classe ter seus
# próprios valores como é o caso dos atributos de instância. Com os atributos de classe todas as instâncias terão o
# mesmo valor para este atributo.

# Refatorar a classe produto


class ProdutoRefatorado:
    # Atributo de classe
    imposto = 1.0005   # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = ProdutoRefatorado.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * ProdutoRefatorado.imposto)
        ProdutoRefatorado.contador = self.id


p1 = ProdutoRefatorado('PlayStation 4', 'Video Game', 2300)
p2 = ProdutoRefatorado('Xbox S', 'Video Game', 4500)

print(p1.valor)
print(p2.valor)

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(ProdutoRefatorado.imposto)    # Acesso correto de um atributo de classe

print(p1.imposto)    # Acesso possível mas incorreto de um atributo de classe
print(p2.imposto)    # Acesso possível mas incorreto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python são chamados de
# atributos estáticos;


# Atributos Dinâmicos -> São atributos de instância que podem ser criados em tempo de execução.

# OBS: O atributo dinâmico será exclusive da instÂncia que o criou

produto1 = ProdutoRefatorado('PlayStation 4', 'Video game', 2300)
produto2 = ProdutoRefatorado('Arroz', 'Mercearia', 5.99)

# criando um produto dinâmico em tempo de execução

produto2.peso = '5Kg'

print(f'Produto: {produto2.nome}, Descrição: {produto2.descricao}, Valor: {produto2.valor}, Peso: {produto2.peso}')
# print(f'Produto: {produto1.nome}, Descrição: {produto1.descricao}, Valor: {produto1.valor}, Peso: {produto1.peso}')

# Deletando atributos

print(produto1.__dict__)
print(produto2.__dict__)

# print(ProdutoRefatorado.__dict__)

del produto2.peso

print(produto1.__dict__)
print(produto2.__dict__)

del produto2.valor
del produto2.descricao

print(produto1.__dict__)
print(produto2.__dict__)

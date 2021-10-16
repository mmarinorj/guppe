"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as características do Objeto. Ou seja, pelos atributos conseguimos representar
     computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente iríamos querer saber se ela é
     127v ou 220v, se é branca, amarela, vermelha, ou outra cor, se está ligada ou desligada, qual é a luminosidade
     dela etc.

    - Métodos (funções) - > Representam os comportamentos do ojeto. Ou seja, as ações que este objeto pode realizar
    no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito provavelmente iríamos querer
    representar no nosso sistema é o de ligar e desligar a mesma.

Em Python, para definir uma classe utilizamos a palavra reservada "class".

OBS1: Utilizamos a palavra pass em Python quando temos um bloco de código que ainda não está implementado.
OBS2: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em maiúsculo.
      Se o nome for composto, utiliza-se as iniciais de ambas as palavras em maiúsculo, todas juntas.

Dica Geek: Em computação não utilizamos acentuação, caracteres especiais, espaços ou similares para nomes de classes,
      atributos, métodos, arquivos, diretórios etc.

OBS3: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos
      que serã mapeados para classes de entidades.
"""


class Lampada:
    pass


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


lamp = Lampada()
print(type(lamp))

"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais
    .Seu escopo compreende TODO o programa
2 - Variáveis locais
    .seu escopo está limitado ao bloco onde foi declarada

Para declarar variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável nós
não colocamos o tipo de dados dela. Este tipo é inferido ao atribuirmos o valor à mesma.

Ex em C ou Java:
int numero = 42;
"""

numero = 42           # exemplo de variável Global
print(numero)
print(type(numero))

numero = 'Marcelo'
print(numero)
print(type(numero))

numero = 42

# Exemplo de escopo local -> Só aparece se a condição passar pelo bloco True do if. Se não, não entra.
if numero > 10:
    novo = numero +10
    print(novo)

print(novo)


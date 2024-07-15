# Faça uma função para retornar uma string ordenada sem usar a função de ordenação
# disponível. Importante, em Python, dada uma string qualquer, o Python não deixa alterar o
# conteúdo de uma posição (veja a figura (a) abaixo). Uma alternativa para resolução desta
# questão é criar uma função que receba uma string e a converta em uma lista. Faça a
# ordenação usando lista (sem utilizar métodos prontos. Dica: é possível utilizar os operadores
# <, > e == para comparar caracteres). Após a ordenação converta a lista em uma String.
# Abaixo exemplo do erro e como converter string em lista e lista em string.

palavra = input("Informe uma palavra: ")

palavra = list(palavra)

for i in range(len(palavra)):
    for j in range(i+1, len(palavra)):
        if palavra[i] > palavra[j]:
            palavra[i], palavra[j] = palavra[j], palavra[i]
            
print(f"Depois de ordenar:", end=" ")
for i in palavra:
    print(i, end="")
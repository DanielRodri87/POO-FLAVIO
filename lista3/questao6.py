# Escreva um programa que cria uma lista de 10 posições e mostre-a. Em seguida, troque o
# primeiro elemento pelo o último, o segundo com o penúltimo, o terceiro com o antepenúltimo
# e, assim, sucessivamente. Mostre a nova lista após todas as trocas. 

lista = [x for x in range(1, 11)]
print(lista)
for i in range(len(lista)//2):
    lista[i], lista[-(i+1)] = lista[-(i+1)], lista[i]
print(lista)

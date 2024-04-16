# Elabore um algoritmo que leia duas listas de dez posições e faça a multiplicação dos
# elementos de mesmo índice, colocando o resultado em uma terceira lista, que deve ser
# mostrada como saída. Não use bibliotecas científicas do Python como numpy. Faça apenas
# interando as listas.

lista1 = []
lista2 = []
lista3 = []

for i in range(10):
    lista1.append(int(input(f"Informe o {i+1}° valor: ")))
    
for i in range(10):
    lista2.append(int(input(f"Informe o {i+1}° valor: ")))

for i in range(0, 10):
    lista3[i] = lista1[i] * lista2[i]
    
print(lista1)
print(lista2)
print(lista3)
lista = []
lista_pares = []
lista_impares = []
while True:
    lista.append(int(input("Informe um valor: ")))
    
    menu = int(input("Deseja continuar? 1 - Sim | 2 - Não "))
    
    if menu == 2:
        break
    
    
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)


print(lista)
print(lista_pares)
print(lista_impares)
lista1 = [1,2,3,4]
lista2 = [5,6,7]
lista3 = [8,9]
lista4 = [lista1, lista2, lista3]
for i in lista4:
    for j in i:
        print(j, end=" ")
    print("\n")

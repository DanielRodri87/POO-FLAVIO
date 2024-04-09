import functools as ft
lista = [1,2,3,4,5,6,6, 7, 8, 9, 0]
pares = filter(lambda x: x%2 == 0, lista)
dobro = map(lambda x: x*2, lista)
soma = ft.reduce(lambda x, y: x+y, lista)

for i in dobro:
    print(i, end=" ")
    
print("Somas todos: ",)
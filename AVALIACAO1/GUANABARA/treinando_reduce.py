# import functools as ft
# def mult(x, y):
#     return x*y

# pares = [x for x in range(1, 6) if x % 2 == 0]
# saida = ft.reduce(mult, pares)
# print(saida)

# def metade(n):
#     return n/2

# lista = [x for x in range(1, 101)]
# saida = map(metade, lista)
# for i in saida:
#     print(i)


def pares(n):
    return n % 2 == 0

lista = [x for x in range(1, 101)]
saida = filter(pares, lista)

for i in saida:
    print(i)

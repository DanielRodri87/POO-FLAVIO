# def metade(n):
#     return n/2

# lista = [1.56,2.65,3.3,4.3]

# lista_metade = map(int, lista)

# for x in lista_metade:
#     print(x)

def isZero(n):
    return n==0

numeros = [0,0,2,3]
zeros = filter(isZero, numeros)
for x in zeros:
    print(x)


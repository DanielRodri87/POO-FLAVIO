# def metade(n):
#     return n/2

# lista = [0,1,2,3,4]

# lista_metade = map(metade, lista)

# for x in lista_metade:
#     print(x)

def isZero(n):
    return n==0

numeros = [0,0,2,3]
zeros = filter(isZero, numeros)
for x in zeros:
    print(x)
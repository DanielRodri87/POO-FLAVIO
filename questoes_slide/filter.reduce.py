import functools as iagopifio

def ispar(x):
    if x % 2 == 0:
        return x
    
def somar(x, y):
    return x+y

def maior(x, y):
    if x >= y:
        return x
    else:
        return y
    
    

lista = [1,2,3,4,5,68,7,8,9,10]

lista_pares = list(filter(ispar, lista))
maior1 = iagopifio.reduce(maior, lista)
soma = iagopifio.reduce(somar, lista_pares)

print(soma)
print(maior1)



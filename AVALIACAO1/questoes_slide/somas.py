import functools as ft


    
def somar(x, y):
    return x+y

def maior(x, y):
    if x >= y:
        return x
    else:
        return y
    
    

lista = [1,2,3,4,5,6,7,8,9,10]

lista_pares = list(filter(lambda x: x % 2 == 0, lista))
dobro_pares = map(lambda x: x*2, lista_pares)
soma = ft.reduce(lambda x, y: x+y, dobro_pares)

print(soma)



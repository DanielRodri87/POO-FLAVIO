
pares = []
impares = []
zeros = []
inicio = []
total = []
def ispar(x):
    if x % 2 == 0:
        return x
    
def isimpar(x):
    if x % 2 != 0 and x != 0:
        return x
def iszero(x):
    return x == 0

while True:
    
    n = int(input("Informe um número: "))
    if n < 0:
        break
    else:
        inicio.append(n)
        
pares = filter(ispar, inicio)
impares = filter(isimpar, inicio)
zeros = filter(iszero, inicio)

list(pares).sort()
list(impares).sort()

total = list(pares) + list(zeros) + list(impares)
    
    
print(total)
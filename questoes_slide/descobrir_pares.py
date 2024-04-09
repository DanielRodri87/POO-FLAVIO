def ispar(x):
    if x % 2 == 0:
        return x
    
    
lista = [1,2,3,4,5,6, 7, 8, 9, 10]
saida = filter(ispar, lista)
for i in saida:
    print(i)
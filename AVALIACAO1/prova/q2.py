def isprimo(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    
    if count == 2:
        return True
    else:
        return False
    
print(isprimo(11))

def lista_func(num):
    lista = []
    while num > 0:
        if isprimo(num) == True:
            lista.append(num)
        num -= 1
        
    return lista


print(isprimo(10))
print(lista_func(10))
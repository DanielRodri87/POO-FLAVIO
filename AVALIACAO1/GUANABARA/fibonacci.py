# 0 1 1 2 3 5 8 13 21 34 55 89 144
n1 = 0
n2 = 1
count = 0

tam = int(input("Informe a quantidade de termos: "))
print(n1, n2, end=" ")
while count < tam:
    soma = n1 + n2
    n1 = n2
    n2 = soma
    
    print(soma, end=" ")
    
    count += 1
    
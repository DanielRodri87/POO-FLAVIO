d = int(input("Digite um número inteiro: "))
aux = 1
resultado = 0

while d>= 1:
    resto = d % 2
    d = int(d//2)
    resultado += aux * resto
    aux *= 10
    
print(resultado)
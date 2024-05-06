n1 = int(input("Digite o numero: "))
expoente = int(input("Digite o expoente:"))
resultado = 1
while (expoente > 0):
    resultado *= n1
    expoente -= 1
    
print(resultado)
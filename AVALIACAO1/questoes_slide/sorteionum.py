import random

valor_inicial = int(input("Informe o valor inicial: "))
valor_final = int(input("Informe o valor final: "))
quantidade = int(input("Quantos números deseja sortear: "))
sorteios = []

while quantidade > 0:
    x = random.randint(valor_inicial, valor_final)
    if x not in sorteios:
        sorteios.append(x)    
        quantidade -= 1
        
for i in sorteios:
    print(i)

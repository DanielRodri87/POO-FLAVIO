import random as rd

jogadores = {}

contador = 1
while contador <= 4:
    jogadores[f"jogador{contador}"] = rd.randint(1, 6)
    contador += 1

maior = 0
for k, v in jogadores.items():
    if v > maior:
        nome = k
        maior = v
        
print(f"O vencedor é {nome} - {maior}")


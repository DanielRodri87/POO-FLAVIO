# Gere uma lista de treze elementos inteiros, que é o gabarito de um teste da loteria esportiva,
# contendo os números 1, 2 ou 3 em cada posição. Também, gere 3 cartões de aposta
# representando um cartão de um apostador que contem o número do seu cartão e um vetor
# de respostas com treze posições. Verifique para cada apostador o número de acertos,
# comparando a lista de gabarito com a lista de respostas. Escreva o número do apostador e
# o número de acertos. Se o apostador tiver treze acertos, mostre a mensagem "Ganhador"

import random as rd
bilhete_sorteado = []
bilhete1 = []
bilhete2 = []
bilhete3 = []

count = 0
acerto1 = 0
acerto2 = 0
acerto3 = 0

while count < 13:
    num = rd.randint(1, 3)
    bilhete_sorteado.append(num)
    count += 1
    
for i in range(13):
    bilhete1.append(rd.randint(1, 3))
    bilhete2.append(rd.randint(1, 3))
    bilhete3.append(rd.randint(1, 3))

    

for i in range(len(bilhete_sorteado)):
    if bilhete1[i] == bilhete_sorteado[i]:
        acerto1 += 1
    elif bilhete2[i] == bilhete_sorteado[i]:
        acerto2 += 1
    elif bilhete3[i] == bilhete_sorteado[i]:
        acerto3 += 1
        
print(bilhete1, bilhete2, bilhete3)
        
if acerto1 == 13:
    print("Apostador 1: Ganhador")
    
if acerto2 == 13:
    print("Apostador 2: Ganhador")

if acerto3 == 13:
    print("Apostador 3: Ganhador")
  
print("A maior quantidade acertos: ")  
if acerto1 > acerto2 and acerto1 > acerto3:
    print(f"Apostador 1: {acerto1} acertos")
    
elif acerto2 > acerto1 and acerto2 > acerto3:
    print(f"Apostador 2: {acerto2} acertos")
    
elif acerto3 > acerto1 and acerto3 > acerto2:
    print(f"Apostador 3: {acerto3} acertos")
    
else:
    print("Empate")
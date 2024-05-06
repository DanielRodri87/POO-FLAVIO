# Faça um joguinho em Python de adivinha. O seu programa vai gerar um número aleatório
# de 0 até 100, o número é oculto ao jogador. O jogador deverá acertar o número secreto. O
# jogo terminará se o usuário acertar ou se ele tentar mais de 10 vezes. Quando o usuário
# acertar o programa deverá perguntar se o jogador deseja repetir ou sair. Toda vez que o
# usuário informar um número o programa deverá informar qual é o número da tentativa.

import random as rd

def sortear_num():
    return rd.randint(1, 100)

status_acerto = 0

while True:
    try: 
        num_sorteado = sortear_num()
        count = 0
        while count < 10:
            print(f"Tentativa {count+1}")
            palpite = int(input("Informe um numero: "))
            count += 1
            if (palpite == num_sorteado):
                print("Parabéns!!")
                status_acerto = 1
                break
                
        if status_acerto == 1:
            menu = int(input("Deseja jogar de novo? 1 - Sim | 2 - Não "))
            if menu == 2:
                break
        else:
            print("Você perdeu")
            break
            
    except:
        print("Houve uma entrada inválida, iremos recomeçar o jogo...")
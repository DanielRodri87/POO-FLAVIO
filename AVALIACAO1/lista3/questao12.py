# Uma pista de Kart permite 3 voltas para cada um de 5 corredores. Escreva um programa
# que leia todos os tempos em segundos e os guarde em um dicionário, onde a chave é o
# nome do corredor. Ao final diga de quem foi a melhor volta da prova e em que volta; e ainda
# quem foi o campeão. O campeão é o que tem a menor média de tempos. 


corredores = {}

for i in range(5):
    nome_corredor = input("Nome do corredor: ")
    tempos_corredor = []

    for volta in range(1, 3 + 1):
        tempo = float(input(f"Corredor: {nome_corredor}\nDigite o tempo da {volta}ª volta: "))
        tempos_corredor.append(tempo)

    corredores[nome_corredor] = tempos_corredor

melhor_volta = corredores[nome_corredor][0]
melhor_volta_corredor = ""

for corredor, tempos in corredores.items():
    melhor_tempo_corredor = min(tempos)
    if melhor_tempo_corredor < melhor_volta:
        melhor_volta = melhor_tempo_corredor
        melhor_volta_corredor = corredor

print(f"O corredor com a melhor volta foi {melhor_volta_corredor} com o tempo de {melhor_volta:.2f} segundos.")

campeao = min(corredores, key=lambda corredor: sum(corredores[corredor]) / 3)
media_campeao = sum(corredores[campeao]) / 3

print(f"O campeão foi {campeao} com a média de {media_campeao:.2f} segundos.")

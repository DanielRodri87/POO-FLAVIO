# Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um
# dicionário, onde a chave é o nome do aluno. Escreva uma função que retorna a média do
# aluno, dado seu nome.
def calcular_media(notas):
    return sum(notas) / len(notas)

notas_dict = {}

quant_alunos = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quant_alunos):
    nome_aluno = input("Nome do aluno: ")
    notas_aluno = []

    for j in range(2):
        nota = float(input(f"Aluno: {nome_aluno}\nDigite a {j + 1}ª nota: "))
        notas_aluno.append(nota)

    notas_dict[nome_aluno] = notas_aluno

source_aluno = input("Digite o nome do aluno que deseja saber a média: ")

if source_aluno in notas_dict:
    notas_do_aluno = notas_dict[source_aluno]
    media = calcular_media(notas_do_aluno)
    print(f"A média do aluno {source_aluno} é: {media:.2f}")
else:
    print("Aluno não encontrado.")


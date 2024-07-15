notas = {}

notas["nome"] = input("Informe o nome do aluno: ")
notas["nota"] = int(input(f"Informe a nota do {notas['nome']}: "))
if notas["nota"] < 7:
    notas["status"] = "reprovado"
else:
    notas["status"] = "aprovado"

for k, v in notas.items():
    print(f"{k} = {v}")

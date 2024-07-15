lista_cpf = []
lista_nome = []
pessoa = {"cpf": lista_cpf, "nome": lista_nome}

pessoas = int(input("Informe a quantidade de pessoas: "))
for i in range(pessoas):
    cpf = int(input("Informe o CPF: "))
    nome = input("Informe o nome: ")
    pessoa["cpf"].append(nome)
    pessoa["nome"].append(cpf)

print("-----------------")
print(pessoa)
for key, value in pessoa.items():
    print(f"{key}: {value}")
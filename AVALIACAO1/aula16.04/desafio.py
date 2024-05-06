
lista = []
dicionario = {}
quant = int(input("Informe a quantidade de pessoas: "))
for i in range(quant):
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    dicionario[cpf] = [nome, idade]
    
print([dicionario[cpf][0] for cpf in dicionario if dicionario[cpf][1] > 18])


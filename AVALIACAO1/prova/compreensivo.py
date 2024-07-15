# Crie um dicionário que armazena o nome e idade de uma pessoa. A
# chave é o cpf.
# CPF:(Nome, Idade)
# Em seguida, faça uma lista compreensiva para retornar todas as
# pessoas com a idade maior que 18.

pessoas = {}


qtd = int(input('Quantas pessoas deseja cadastrar? '))
for i in range(qtd):
    cpf = input('CPF: ')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    pessoas[cpf] = [nome, idade]
for k, v in pessoas.items():
    print (f"{k} - {v}")
    
maiores = [v for v in pessoas.values() if v[1] >= 18]
print(maiores)
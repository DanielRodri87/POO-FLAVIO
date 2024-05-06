dicionario = {}
soma_idades = 0
for i in range(3):
    cpf = input ("cpf: ")
    nome = input("nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")
    dicionario[cpf] = [nome, idade, sexo]
    
for v in dicionario.values():
    soma_idades += v[1]
    
for k, v in dicionario.items():
    print(k, v)


print(f"A media das idades eh: {soma_idades/3}")
    
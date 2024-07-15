# Construa um algoritmo para o funcionamento de uma agenda. Devem ser lidos os seguintes
# dados de 10 pessoas: nome, endereço, CEP, bairro e telefone. Tais dados devem ser
# armazenados na agenda, cuja representação é uma lista com 10 linhas (referentes às
# pessoas) e 5 colunas (referentes aos dados). Por fim, o algoritmo deve gerar como saída a
# agenda impressa em ordem invertida em relação à ordem de entrada dos dados.
nomes = []
ederecos = []
cep = []
bairro = []
telefones = []
agenda = ["Nome", nomes, "Endereco", ederecos, "CEP", cep, "Bairro", bairro, "Telefone", telefones]

for i in range(10):
    nomes.append(input("Digite o nome: "))
    ederecos.append(input("Digite o endereco: "))
    cep.append(input("Digite o CEP: "))
    bairro.append(input("Digite o bairro: "))
    telefones.append(input("Digite o telefone: "))
    
print(agenda)

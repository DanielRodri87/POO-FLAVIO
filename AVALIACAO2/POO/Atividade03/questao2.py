# Crie uma classe Agenda que pode armazenar até 10 pessoas (a classe Pessoa deve conter os atributos: nome
# e idade) e que seja capaz de realizar as seguintes operações:
# a. armazenaPessoa; // Não permitir armazenar mais de 10 pessoas
# b. removePessoa; // Pelo nome
# c. buscaPessoa; // Busca pelo nome e imprime os dados da pessoa
# d. imprimeAgenda(); // imprime os dados de todas as pessoas da agenda

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Agenda:
    def __init__(self):
        self.pessoas = []

    def armazenaPessoa(self, pessoa):
        if len(self.pessoas) >= 10:
            print("Lista cheia")
        else:
            self.pessoas.append(pessoa)

    def removePessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa.nome == nome:
                self.pessoas.remove(pessoa)
                return
        print(f'Pessoa {nome} não encontrada')

    def buscaPessoa(self, nome):
        for pessoa in self.pessoas:
            if pessoa.nome == nome:
                print(pessoa)
                return
        print(f'Pessoa {nome} não encontrada')

    def imprimeAgenda(self):
        if not self.pessoas:
            print("Agenda está vazia.")
        else:
            for pessoa in self.pessoas:
                print(pessoa)

agenda = Agenda()

agenda.armazenaPessoa(Pessoa("Alice", 30))
agenda.armazenaPessoa(Pessoa("Bob", 25))
agenda.armazenaPessoa(Pessoa("Charlie", 35))

agenda.imprimeAgenda()

agenda.buscaPessoa("Alice")

agenda.removePessoa("Alice")
agenda.imprimeAgenda()

agenda.removePessoa("Alice")

for i in range(7):
    agenda.armazenaPessoa(Pessoa(f"Pessoa{i}", 20 + i))

# Tentando adicionar uma pessoa com a agenda cheia
agenda.armazenaPessoa(Pessoa("Extra", 50))

class Pessoa:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print(f"{self.nome}: {self.matricula}")

pessoa = Pessoa('Daniel', 123)
pessoa.imprimir()

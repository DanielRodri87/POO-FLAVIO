class Funcionario():
    def __init__(self, nome, cpf) -> None:
        self._nome = nome
        self._cpf = cpf

    def imprimir(self):
        print(self._nome, self._cpf)

class Gerente(Funcionario):
    def __init_subclass__(nself, nome, cpf):
        super().__init__(nome, cpf)

    def imprimir(self):
        print("Entrei")
        super().imprimir()

f = Funcionario("Rodrigues", "111")
g = Gerente("daniel", "123")

f.imprimir()
g.imprimir()
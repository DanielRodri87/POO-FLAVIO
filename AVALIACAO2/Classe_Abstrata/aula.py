import abc
class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
    
    @abc.abstractmethod
    def get_bonificacao(self):
        pass

class Gerente(Funcionario):
    def __init_subclass__(nself, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def imprimir(self):
        print("Entrei no gerente")
        super().imprimir()

    def get_bonificacao(self):
        return self.salario * 0.10
    
class Secretario(Funcionario):
    def __init_subclass__(nself, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def imprimir(self):
        print("Entrei no secretario")
        super().imprimir()

    def get_bonificacao(self):
        return self.salario * 0.05 + 100

class ControleBonificacao():
    def __init__(self):
        self.total_bonificacoes = 0

    def calcular_bonificacao(self, funcionario):
        if (isinstance(funcionario, Funcionario)):
            self.total_bonificacoes += funcionario.get_bonificacao()
        else:
            print("Funcionario não é do tipo Funcionario")

    def imprimir(self):
        print(self.total_bonificacoes)

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

g = Gerente("Daniel", "123", 1500)
s = Secretario("Rodrigues", "111", 1000)
cliente = Cliente("Rodrigues", "6666")
c = ControleBonificacao()
c.calcular_bonificacao(g)
c.calcular_bonificacao(s)
c.calcular_bonificacao(cliente)
c.imprimir()

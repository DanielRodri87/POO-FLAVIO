import abc
class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario, senha):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._senha = senha

    @property
    def senha(self):
        return self._senha
    
    @property
    def cpf(self):
        return self._cpf

    @abc.abstractmethod
    def autenticacao(self):
        pass

class Gerente(Funcionario):
    def __init_subclass__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario, senha)

    def imprimir(self):
        print("Entrei no gerente")
        super().imprimir()

    def autenticacao(self, senha, cpf):
        if senha == self.senha and cpf == self.cpf:
            return True
        else:
            return False
    
class Secretario(Funcionario):
    def __init_subclass__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario, senha)

    def imprimir(self):
        print("Entrei no secretario")
        super().imprimir()

    def autenticacao(self, senha, cpf):
        if senha == self.senha and cpf == self.cpf:
            return True
        else:
            return False

class Atendente(Funcionario):
    def __init_subclass__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario, senha)

    def imprimir(self):
        print("Entrei no atendente")
        super().imprimir()

    def autenticacao(self, senha, cpf):
        if senha == self.senha and cpf == self.cpf:
            return True
        else:
            return False
        
class Limpador_Vidro():
    def __init__(self, nome, cpf, salario, senha):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.senha = senha

    def imprimir(self):
        print("Entrei no limpador de vidro")
        super().imprimir()
       
class Controle_Autenticacao():
    def __init__(self):
        self.controle = False
    
    def login(self, funcionario, senha, cpf):
        if (isinstance(funcionario, Funcionario)):
            self.controle = funcionario.autenticacao(senha, cpf)
            if self.controle:
                print("Usuario autenticado")
            else:
                print("Senha ou CPF incorretos")
        else:
            print("Usuario sem permissão")


g = Gerente("Daniel", "123", 1500, "123")
s = Secretario("Rodrigues", "111", 1000, "111")
a = Atendente("Rita", "121", 1000, "121")
lm = Limpador_Vidro("Iago", "666", 2000, "666")

cont = Controle_Autenticacao()
cont.login(g, "123", "123")
cont.login(lm, "666", "666")
cont.login(s, "111", "111")
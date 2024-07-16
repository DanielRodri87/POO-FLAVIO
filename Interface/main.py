import abc

class Autenticavel(abc.ABC):
    def autentica(self, cpf, senha):
        pass

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


class Gerente(Funcionario):
    def __init_subclass__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario, senha)

    def imprimir(self):
        print("Entrei no gerente")
        super().imprimir()

    def autentica(self, senha, cpf):
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

    def autentica(self, senha, cpf):
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

    def autentica(self, senha, cpf):
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
        if (isinstance(funcionario, Autenticavel)):
            self.controle = funcionario.autentica(senha, cpf)
            if self.controle:
                print("Usuario autenticado")
            else:
                print("Senha ou CPF incorretos")
        else:
            print("Usuario sem permissão")


Autenticavel.register(Gerente)
Autenticavel.register(Atendente)

g1 = Gerente("João", "123456789", 10000, "123")
print(isinstance(g1, Autenticavel))
a1 = Atendente("Daniel", "987654321", 2000, "123")
print(isinstance(a1, Autenticavel))
s1 = Secretario("Iago", "123456789", 1000, "123")
print(isinstance(s1, Autenticavel))

ca = Controle_Autenticacao()
ca.login(g1, "123", "123456789")
ca.login(a1, "123", "987654321")
ca.login(s1, "123", "123456789")
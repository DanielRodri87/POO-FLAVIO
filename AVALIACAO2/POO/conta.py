class Conta:
    def __init__(self, titular, saldo, historico):
        self.titular = titular
        self.saldo = saldo
        self.historico = historico
        
    def sacar(self, atributo, valor, historico):
        if self.saldo >= valor and atributo == self.titular:
            self.saldo -= valor
            historico.add_transacao(valor)

            return True, "deu certo"
        
        else:
            return False, "Deu errado"
            
    def depositar(self, atributo, valor, historico):
        if atributo == self.titular:
            self.saldo += valor
            historico.add_transacao(valor)
            
            
    def extrato(self, atributo):
        if self.titular == atributo:
            Titular.imprimir(atributo)
            print(self.saldo)
        else:
            print("Pessoa não encontrada")
            
    def transferir(self, valor, conta, historico):
        if self.saldo >= valor:
            self.saldo -= valor
            conta.saldo += valor
            historico.add_transacao(valor)
            return True
        else:
            return False
        
class Titular:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        
    def imprimir(self):
        print(self.nome, " | ", self.cpf)
        
        
class Historico:
    def __init__(self, lista):
        self.lista = []
        
    def add_transacao(self, transacao):
        self.lista.append(transacao)
        
    def imprimir_transacoes(self):
        for i in self.lista:
            print(i)
        
t1 = Titular("danie", "123", "26/05/2005")
h1 = Historico([])
c1 = Conta(t1, 1000, h1)

c1.sacar(t1, 100, h1)
c1.depositar(t1, 500, h1)

h1.imprimir_transacoes()



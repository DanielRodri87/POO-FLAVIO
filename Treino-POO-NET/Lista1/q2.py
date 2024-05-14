# Implemente uma classe chamada “ContaBancária” que possua atributos para armazenar o número da conta, nome do titular e saldo.
# Adicione métodos para realizar depósitos e saques.

class ContaBancaria:
    def __init__(self, numero, saldo, titular):
        self.numero = numero
        self.saldo = saldo
        self.titular = titular
        
    def depositar(self, conta, valor):
        if conta == self.numero:
            self.saldo += valor
        else:
            print("Conta inexistente")
    def sacar(self, conta, valor):
        if conta == self.numero:
            if self.saldo > valor:
                self.saldo -= valor
            else:
                print("Você não tem saldo suficiente")
        else:
            print("Conta inexistente")
            
    def extrato(self):
        print(self.saldo)        

pessoa = ContaBancaria(111, 10, "daniel")
pessoa.extrato()
pessoa.sacar(111, 20)
pessoa.depositar(111, 30)
pessoa.sacar(112, 20)
pessoa.extrato()
pessoa.sacar(111, 20)
pessoa.extrato()
        
        
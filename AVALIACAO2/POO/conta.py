class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def sacar(self, atributo, valor):
        if self.saldo >= valor and atributo == self.titular:
            self.saldo -= valor
        else:
            print("Saldo Insuficiente")
            
    def depositar(self, atributo, valor):
        if atributo == self.titular:
            self.saldo += valor
            
    def extrato(self, atributo):
        if self.titular == atributo:
            print(self.saldo)
        else:
            print("Pessoa não encontrada")
    
nome = input("Informe seu nome: ")
saldo = float(input("Quanto dinheiro você tem? "))
p1 = Conta(nome, saldo)


while True:
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Extrato")
    menu = int(input("->"))

    if menu == 1:
        input_valor = float(input("Valor a sacar: "))
        p1.sacar(nome, input_valor)
        
    elif menu == 2:
        input_valor = float(input("Valor a sacar: "))
        p1.depositar(nome, input_valor)
    
    else:
        nome = input("Informe seu nome: ")
        p1.extrato(nome)

        
        

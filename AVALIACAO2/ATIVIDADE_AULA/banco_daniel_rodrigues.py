# DESENVOLVIDO POR DANIEL RODRIGUES DE SOUSA



'''
Mapeamento Classes
Cliente 
    - nome
    - cpf
Conta
    - numero
    - cliente
    - saldo
    - historico

Historico
    - lista de transacoes



'''


import datetime as dt

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
    def __str__(self):
        return f'Nome: {self.nome} - CPF: {self.cpf}'

class Historico:
    def __init__(self):
        self.lista = []
        
    def add_transacao(self, transacao):
        self.lista.append(transacao)
        
    def imprimir_transacoes(self):
        for i in self.lista:
            print(i)



class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.historico = Historico()
        
        
        
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.add_transacao(f"Saque: {valor} | Data: {dt.datetime.now().date()} | Hora: {dt.datetime.now().strftime('%H:%M:%S')}")
            return True, "Saque realizado com sucesso"
        else:
            return False, "Saldo insuficiente"
                    
    def depositar(self, valor):
        self.saldo += valor
        self.historico.add_transacao(f"Depósito: {valor} | Data: {dt.datetime.now().date()} | Hora: {dt.datetime.now().strftime('%H:%M:%S')}")
           
    def transferir(self, valor, conta_destino):
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.historico.add_transacao(f"Transferência para conta {conta_destino.numero}: {valor} | Data: {dt.datetime.now().date()} | Hora: {dt.datetime.now().strftime('%H:%M:%S')}")
            conta_destino.historico.add_transacao(f"Transferência recebida da conta {self.numero}: {valor} | Data: {dt.datetime.now().date()} | Hora: {dt.datetime.now().strftime('%H:%M:%S')}")
            return True, "Transferência realizada com sucesso"
        else:
            return False, "Saldo insuficiente"

def main():
    clientes = {}
    contas = {}

    while True:
        print("\n1 - Cadastrar cliente")
        print("2 - Criar conta")
        print("3 - Sacar")
        print("4 - Depositar")
        print("5 - Transferir")
        print("6 - Imprimir histórico")
        print("7 - Sair")
        
        menu = int(input("Escolha uma opção: "))
        
        if menu == 1:
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            if cpf in clientes.keys():
                print("CPF já cadastrado.")
            else:
                cliente = Cliente(nome, cpf)
                clientes[cpf] = cliente
                print("Cliente cadastrado com sucesso.")
                
        
        elif menu == 2:
            print("Clientes cadastrados:")
            for cliente in clientes.values():
                print(cliente)
                
            numero = input("Digite o número da conta: ")
            cpf = input("Digite o CPF do cliente: ")
            if cpf not in clientes:
                print("Cliente não encontrado.")
            
            elif cpf in [conta.cliente.cpf for conta in contas.values()]:
                print("Cliente já possui conta.")
            else:
                cliente = clientes[cpf]
                conta = Conta(numero, cliente)
                contas[numero] = conta
                print("Conta criada com sucesso.")
                conta.historico.add_transacao(f"Conta criada | Data: {dt.datetime.now().date()} | Hora: {dt.datetime.now().strftime('%H:%M:%S')}")

            
        elif menu == 3:
            print("Clientes cadastrados:")
            for cliente in clientes.values():
                print(cliente)
            
            cpf = input("Digite o CPF do cliente: ")
            cliente_encontrado = None
            for numero, conta in contas.items():
                if conta.cliente.cpf == cpf:
                    cliente_encontrado = conta
                    break
            
            if not cliente_encontrado:
                print("Cliente ou conta não encontrada.")
            else:
                print(f"Número da conta: {cliente_encontrado.numero}")
                print(f"Saldo: {cliente_encontrado.saldo}")
                valor = float(input("Digite o valor do saque: "))
                if valor <= 0:
                    print("Valor inválido.")
                else:
                    sucesso, mensagem = cliente_encontrado.sacar(valor)
                    print(mensagem)
            
        elif menu == 4:
            print("Clientes cadastrados:")
            for cliente in clientes.values():
                print(cliente)
            
            cpf = input("Digite o CPF do cliente: ")
            conta_cliente = next((conta for conta in contas.values() if conta.cliente.cpf == cpf), None)
            
            if not conta_cliente:
                print("Cliente ou conta não encontrada.")
            else:
                print(f"Número da conta: {conta_cliente.numero}")
                print(f"Saldo: {conta_cliente.saldo}")
                valor = float(input("Digite o valor do depósito: "))
                if valor <= 0:
                    print("Valor inválido.")
                else:
                    conta_cliente.depositar(valor)
                    print("Depósito realizado com sucesso.")            

        elif menu == 5:
            print("Clientes cadastrados:")
            for cliente in clientes.values():
                print(cliente)
            
            cpf_origem = input("Digite o CPF do cliente de origem: ")
            conta_origem = next((conta for conta in contas.values() if conta.cliente.cpf == cpf_origem), None)
            
            if not conta_origem:
                print("Cliente ou conta de origem não encontrada.")
            else:
                print(f"Número da conta de origem: {conta_origem.numero}")
                print(f"Saldo: {conta_origem.saldo}")
                
                cpf_destino = input("Digite o CPF do cliente de destino: ")
                conta_destino = next((conta for conta in contas.values() if conta.cliente.cpf == cpf_destino), None)
                
                if not conta_destino:
                    print("Cliente ou conta de destino não encontrada.")
                else:
                    valor = float(input("Digite o valor da transferência: "))
                    if valor <= 0:
                        print("Valor inválido.")
                    else:
                        sucesso, mensagem = conta_origem.transferir(valor, conta_destino)
                        print(mensagem)
        

        elif menu == 6:
            numero = input("Digite o número da conta: ")
            if numero not in contas:
                print("Conta não encontrada.")
            else:
                conta = contas[numero]
                conta.historico.imprimir_transacoes()
        
        elif menu == 7:
            break

if __name__ == '__main__':
    main()

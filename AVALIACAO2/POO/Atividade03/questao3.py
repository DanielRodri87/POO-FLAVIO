# Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio. A
# classe deve armazenar o andar atual (térreo = 0), total de andares no prédio (desconsiderando o térreo),
# capacidade do elevador e quantas pessoas estão presentes nele. A classe deve também disponibilizar os
# seguintes métodos:
# a. Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio
# (os elevadores sempre começam no térreo e vazio);
# b. Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
# c. Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
# d. Sobe: para subir um andar (não deve subir se já estiver no último andar);
# e. Desce: para descer um andar (não deve descer se já estiver no térreo);
# f. Encapsular todos os atributos da classe (atributos privados e criar os métodos set e get).
# g. Criar um menu iterativo para controlar as operações do elevador. 

class Elevador:
    def __init__(self, capacidade, total_andares):
        self._andar_atual = 0
        self._total_andares = total_andares
        self._capacidade = capacidade
        self._pessoas_presentes = 0
        
    @property
    def andar_atual(self):
        return self._andar_atual
    
    @andar_atual.setter
    def andar_atual(self, input_andar):
        self._andar_atual = input_andar
        
    @property
    def total_andares(self):
        return self._total_andares
    
    @total_andares.setter
    def total_andares(self, input_total):
        self._total_andares = input_total
        
    @property
    def capacidade(self):
        return self._capacidade
    
    @capacidade.setter
    def capacidade(self, input_capacidade):
        self._capacidade = input_capacidade
        
    @property
    def pessoas_presentes(self):
        return self._pessoas_presentes
    
    @pessoas_presentes.setter
    def pessoas_presentes(self, input_pessoas):
        self._pessoas_presentes = input_pessoas
        
    def inicializa(self, capacidade, total_andares):
        self.capacidade = capacidade
        self.total_andares = total_andares
        self.andar_atual = 0
        self.pessoas_presentes = 0
        
    def entra(self):
        if self.pessoas_presentes < self.capacidade:
            self.pessoas_presentes += 1
        else:
            print("Elevador cheio!")
            
    def sai(self):
        if self.pessoas_presentes > 0:
            self.pessoas_presentes -= 1
        else:
            print("Elevador vazio!")
            
    def sobe(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
        else:
            print("Elevador no último andar!")
    
    def desce(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
        else:
            print("Elevador no térreo!")
    

def menu():
    elevador = Elevador(5, 10)
    while True:
        print("1 - Inicializar")
        print("2 - Entrar")
        print("3 - Sair")
        print("4 - Subir")
        print("5 - Descer")
        print("6 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        
        if opcao == 1:
            capacidade = int(input("Digite a capacidade do elevador: "))
            total_andares = int(input("Digite o total de andares do prédio: "))
            elevador.inicializa(capacidade, total_andares)
        elif opcao == 2:
            elevador.entra()
        elif opcao == 3:
            elevador.sai()
        elif opcao == 4:
            elevador.sobe()
        elif opcao == 5:
            elevador.desce()
        elif opcao == 6:
            break
        else:
            print("Opção inválida!")
            
menu()
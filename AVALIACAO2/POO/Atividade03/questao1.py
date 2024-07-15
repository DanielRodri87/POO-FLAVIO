# Crie uma classe para representar uma pessoa, com os atributos privados de nome, data de nascimento e altura.
# Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos os dados de
# uma pessoa. Crie um método para calcular a idade da pessoa.

from datetime import datetime as dt
import time

class Pessoa:
    def __init__(self, nome, data_nascimento, altura):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._altura = altura
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, input_nome):
        self._nome = input_nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, input_nascimento):
        self._data_nascimento = input_nascimento
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, input_altura):
        self._altura = input_altura
        
    def imprimir_pessoas(self):
        print(f"Nome: {self.nome}\nData Nascimento: {self.data_nascimento}\nAltura: {self.altura}")
        
    def calcular_idade(self):

        idade = dt.now() - dt.strptime(self.data_nascimento, "%d/%m/%Y")
        ano = idade.days//365
        print(f"{self.nome} tem {ano} anos.")
            
            
p1 = Pessoa("Daniel", "17/05/2005", 1.73)

p1.imprimir_pessoas()
p1.calcular_idade()
    
    
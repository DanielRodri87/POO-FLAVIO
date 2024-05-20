
class Conta():
    
    __slots__ = ['_saldo', '_titular'] #permite definir somente os atributos das instancias utilizados. 
    _total_contas = 0
    def __init__(self, titular, saldo):
        self._saldo = saldo
        self._titular = titular
        Conta._total_contas += 1
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor
        
    @staticmethod #usado para atributo da classe
    def get_total_contas():
        return Conta._total_contas

p1 = Conta('Daniel', 1000)

print(p1.saldo)
p1.saldo = 2000
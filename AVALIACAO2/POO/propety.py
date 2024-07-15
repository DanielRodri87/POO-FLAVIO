class Conta:
    def __init__(self, titular, saldo):
        self._saldo = saldo
        self._titular = titular
        
    @property # get
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            assert False, "Saldo não pode ser negativo"
        else:
            self._saldo = valor
    
    
c1 = Conta("Daniel", 100)
print(c1.saldo)
c1.saldo = 1000
print(c1.saldo)
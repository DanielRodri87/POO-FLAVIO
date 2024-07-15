class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"Dados da Conta\nNúmero: {self._numero}\nTitular: {self._titular}\nSaldo: {self._saldo}\nLimite: {self._limite}"

    @property
    def saldo(self):
        return self._saldo


class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * (taxa * 2)
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor - 0.10


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)

    def atualiza(self, taxa):
        self._saldo += self._saldo * (taxa * 3)
        return self._saldo


class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0) -> None:
        self._selic = selic
        self._saldo_total = saldo_total

    def roda(self, conta):
        print(f"Saldo da conta: {conta.saldo}")
        self._saldo_total += conta.atualiza(self._selic)
        print(f"Saldo atualizado: {conta.saldo}")

    @property
    def saldo_total(self):
        return self._saldo_total


if __name__ == "__main__":
    c = Conta("123-4", "João", 1000.0, 2000.0)
    cc = ContaCorrente("123-5", "Jose", 1000.0, 2000.0)
    cp = ContaPoupanca("123-6", "Maria", 1000.0, 2000.0)

    adc = AtualizadorDeContas(0.01)
    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)

    print(f"Saldo Total: {adc.saldo_total}")

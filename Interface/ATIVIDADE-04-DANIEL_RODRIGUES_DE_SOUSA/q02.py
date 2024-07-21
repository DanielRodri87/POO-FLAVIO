import abc

class Veiculo(abc.ABC):
    def calcular_custo_viagem(self, distancia):
        pass

class Carro():
    def __init__(self, consumo_combustivel):
        self.consumo_combustivel = consumo_combustivel

    def calcular_custo_viagem(self, distancia):
        litros_necessarios = distancia / self.consumo_combustivel
        custo = distancia * litros_necessarios
        return custo

class Moto():
    def __init__(self, consumo_combustivel):
        self.consumo_combustivel = consumo_combustivel

    def calcular_custo_viagem(self, distancia):
        litros_necessarios = distancia / self.consumo_combustivel
        custo = distancia * litros_necessarios
        return custo
    
class Caminhao():
    def __init__(self, consumo_combustivel):
        self.consumo_combustivel = consumo_combustivel

    def calcular_custo_viagem(self, distancia):
        litros_necessarios = distancia / self.consumo_combustivel
        custo = (distancia * litros_necessarios) + 200
        return custo

class CalculadoraCustoViagem():
    def __init__(self):
        self.custo_total = 0

    def calcular_e_armazenar_custo(self, veiculo, distancia):
        if isinstance(veiculo, Veiculo):
            self.custo_total += veiculo.calcular_custo_viagem(distancia)
            return True, "Sucesso"
        return False, "Veículo inválido"
    
    def get_custo_total(self):
        return self.custo_total

class Bicicleta():
    def __init__(self, consumo_combustivel):
        self.consumo_combustivel = consumo_combustivel

    def calcular_custo_viagem(self, distancia):
        litros_necessarios = distancia / self.consumo_combustivel
        custo = distancia * litros_necessarios
        return custo
    

Veiculo.register(Carro)
Veiculo.register(Moto)
Veiculo.register(Caminhao)


carro1 = Carro(15)
moto1 = Moto(35)
caminhao1 = Caminhao(8)
calc = CalculadoraCustoViagem()

retorno = calc.calcular_e_armazenar_custo(carro1, 150)
print(retorno[1])
retorno = calc.calcular_e_armazenar_custo(moto1, 150)
print(retorno[1])
retorno = calc.calcular_e_armazenar_custo(caminhao1, 150)
print(retorno[1])


print(f"Custo total: {calc.get_custo_total():.2f}")
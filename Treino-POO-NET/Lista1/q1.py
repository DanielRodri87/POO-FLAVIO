# Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio
# e métodos para calcular a área e o perímetro do círculo.

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        
    def calc_area(self):
        return 3.14 * (self.raio*self.raio)
    
    def calc_perimetro(self):
        return 2 * 3.15 * self.raio
    

circ = Circulo(10)
print(circ.calc_perimetro())
print(circ.calc_area())
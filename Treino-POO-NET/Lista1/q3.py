# Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e a altura.
# Implemente métodos para calcular a área e o perímetro do retângulo.

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
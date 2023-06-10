# Crie uma classe Retangulo para calcular a área e o perímetro.

class Retangulo:
    def __init__(self, comprimento=None, largura=None):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_valor_lados(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def get_valor_lados(self):
        return f'Comprimento {self.comprimento}m e largura {self.largura}m'

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return (self.comprimento * 2) + (self.largura * 2)


retangulo = Retangulo(10, 20)

print('Bem vindo ao programa de cálculo da área e do perímetro de um triângulo!')

print(f'\nDados: {retangulo.get_valor_lados()}'
      f'\nÁrea: {retangulo.calcular_area()}m²'
      f'\nPerímetro: {retangulo.calcular_perimetro()}m')

# Classe Retângulo: Crie uma classe que modele um retângulo:
#   Atributos: Comprimento e Largura (ou Base e Altura)
#   Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local. Depois, deve
# criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, base=0, altura=0):
        self.base = base
        self.altura = altura

    def set_base(self, base):
        self.base = base

    def set_altura(self, altura):
        self.altura = altura

    def get_base(self):
        return self.base

    def get_altura(self):
        return self.altura

    def calcular_area(self, base, altura):
        return self.base * self.altura

    def calcular_perimetro(self, base, altura):
        return (self.base + self.altura) * 2


print('Bem-vindo ao programa de cálculo de quantidade de pisos e rodapés para um local!')

comprimento = float(input('Informe o comprimento (m²): '))
largura = float(input('Largura (m²): '))

valores = Retangulo()
valores.set_base(comprimento)
valores.set_altura(largura)

print(f'\nComprimento informado: {valores.get_base()}m²'
      f'\nLargura: {valores.get_altura()}m²'
      f'\n\nQuantidade de pisos necessários: {valores.calcular_area(comprimento, largura):.2f}m²'
      f'\nRodapés: {valores.calcular_perimetro(comprimento, largura)}m')

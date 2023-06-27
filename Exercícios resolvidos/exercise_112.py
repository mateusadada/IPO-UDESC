# Classe Bola: Crie uma classe que modele uma bola:
#   Atributos: Cor, circunferência, material
#   Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor=None, circunferencia=None, material=None):
        self.cor = cor
        self._circunferencia = circunferencia
        self.__material = material

    def set_cor(self, cor):
        self.cor = cor

    def get_cor(self):
        return self.cor

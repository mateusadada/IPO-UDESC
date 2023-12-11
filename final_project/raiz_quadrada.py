from operacoes import Operacoes
from math import sqrt


class RaizQuadrada(Operacoes):
    def __init__(self, num1, raiz_quadrada=None):
        super().__init__(num1)
        self.raiz_quadrada = raiz_quadrada

    def _calcular_raiz_quadrada(self):
        self.raiz_quadrada = sqrt(self.numero1)
        return self.raiz_quadrada

    def get_raiz_quadrada(self):
        return self.raiz_quadrada

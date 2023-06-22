from operacoes import Operacoes
from math import pow


class Potencia(Operacoes):
    def __init__(self, num1, num2, potencia=None):
        super().__init__(num1, num2)
        self.potencia = potencia

    def calcular_potencia(self):
        self.potencia = pow(self.numero1, self.numero2)
        return self.potencia

    def get_potencia(self):
        return self.potencia

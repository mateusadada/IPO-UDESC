from operacoes import Operacoes


class Soma(Operacoes):
    def __init__(self, num1, num2, soma=None):
        super().__init__(num1, num2)
        self.soma = soma

    def _calcular_soma(self):
        self.soma = self.numero1 + self.numero2
        return self.soma

    def get_soma(self):
        return self.soma

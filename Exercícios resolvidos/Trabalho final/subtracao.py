from operacoes import Operacoes


class Subtracao(Operacoes):
    def __init__(self, num1, num2, subtracao=None):
        super().__init__(num1, num2)
        self.subtracao = subtracao

    def _calcular_subtracao(self):
        self.subtracao = self.numero1 - self.numero2
        return self.subtracao

    def get_subtracao(self):
        return self.subtracao

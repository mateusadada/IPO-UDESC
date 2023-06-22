from operacoes import Operacoes


class Multiplicacao(Operacoes):
    def __init__(self, num1, num2, multiplicacao=None):
        super().__init__(num1, num2)
        self.multiplicacao = multiplicacao

    def _calcular_multiplicacao(self):
        self.multiplicacao = self.numero1 * self.numero2
        return self.multiplicacao

    def get_multiplicacao(self):
        return self.multiplicacao

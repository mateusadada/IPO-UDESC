from operacoes import Operacoes


class Divisao(Operacoes):
    def __init__(self, num1, num2, divisao=None):
        super().__init__(num1, num2)
        self.divisao = divisao

    def _calcular_divisao(self):
        self.divisao = self.numero1 / self.numero2
        return self.divisao

    def get_divisao(self):
        return self.divisao

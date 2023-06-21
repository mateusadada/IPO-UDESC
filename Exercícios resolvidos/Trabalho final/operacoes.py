# superclasse para armazenar os números
class Operacoes:
    def __init__(self, num1=None, num2=None):
        self.numero1 = num1
        self.numero2 = num2

    def set_numero1(self, num1):
        self.numero1 = num1

    def set_numero2(self, num2):
        self.numero2 = num2

    def get_numero1(self):
        return self.numero1

    def get_numero2(self):
        return self.numero2

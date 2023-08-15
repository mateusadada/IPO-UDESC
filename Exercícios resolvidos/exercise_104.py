# Crie e defina a classe Calculadora e os métodos dos objetos dessa classe. Após, cria um objeto da classe Calculadora
# (armazenado na variável 'c') e envia mensagens ao mesmo, solicitando a execução de métodos de instância
# (ou de objetos) para o objeto do tipo Calculadora.

class Calculadora:

    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def adicao(self):
        return self.valor1 + self.valor2

    def subtracao(self):
        return self.valor1 - self.valor2

    def produto(self):
        return self.valor1 * self.valor2

    def divisao(self):
        return self.valor1 / self.valor2


print('Bem-vindo ao programa de cálculo das quatro operações básicas (calculadora) a partir de 2 números!')

numero1 = float(input('1º número: '))
numero2 = float(input('2º número: '))
c = Calculadora(numero1, numero2)

print(f'\nAdição: {c.adicao():.1f}'
      f'\nSubtração: {c.subtracao():.1f}'
      f'\nMultiplicação: {c.produto():.1f}'
      f'\nDivisão: {c.divisao():.1f}')

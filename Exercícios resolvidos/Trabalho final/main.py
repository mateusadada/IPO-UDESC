from operacoes import Operacoes


class Soma(Operacoes):
    def __init__(self, num1, num2):
        super().__init__(numero1, numero2)

    def calcular_soma(self):
        soma = self.numero1 + self.numero2
        historico.append(f'{self.numero1} + {self.numero2} = {soma}')
        return soma


class Subtracao(Operacoes):
    def __init__(self, num1, num2):
        super().__init__(numero1, numero2)

    def calcular_subtracao(self):
        subtracao = self.numero1 - self.numero2
        historico.append(f'{self.numero1} - {self.numero2} = {subtracao}')
        return subtracao


class Multiplicacao(Operacoes):
    def __init__(self, num1, num2):
        super().__init__(numero1, numero2)

    def calcular_multiplicacao(self):
        multiplicacao = self.numero1 * self.numero2
        historico.append(f'{self.numero1} * {self.numero2} = {multiplicacao}')
        return multiplicacao


class Divisao(Operacoes):
    def __init__(self, num1, num2):
        super().__init__(numero1, numero2)

    def calcular_divisao(self):
        divisao = self.numero1 / self.numero2
        historico.append(f'{self.numero1} / {self.numero2} = {divisao}')
        return divisao


historico = []

while True:
    print('*** CALCULADORA ***'
          '\n1. Soma'
          '\n2. Subtração'
          '\n3. Multiplicação'
          '\n4. Divisão'
          '\n5. Potência'
          '\n6. Raiz quadrada'
          '\n7. Histórico'
          '\n9. SAIR ')

    opcao = int(input('Opção: '))

    if opcao == 1:
        print('\n===== SOMA =====')

        numero1 = float(input('1º número: '))
        numero2 = float(input('2º número: '))
        usuario = Soma(numero1, numero2)

        print(f'Resultado: {usuario.calcular_soma()}')

    elif opcao == 2:
        print('\n===== SUBTRAÇÃO =====')

        numero1 = float(input('1º número: '))
        numero2 = float(input('2º número: '))
        usuario = Subtracao(numero1, numero2)

        print(f'Resultado: {usuario.calcular_subtracao()}')

    elif opcao == 3:
        print('\n===== MULTIPLICAÇÃO =====')

        numero1 = float(input('1º número: '))
        numero2 = float(input('2º número: '))
        usuario = Multiplicacao(numero1, numero2)

        print(f'Resultado: {usuario.calcular_multiplicacao()}')

    elif opcao == 4:
        print('\n===== DIVISÃO =====')

        numero1 = float(input('Numerador: '))

        while True:
            numero2 = float(input('Denominador: '))

            if numero2 != 0:
                usuario = Divisao(numero1, numero2)
                break
            else:
                print('## O denominador não pode ser nulo!')

        print(f'Resultado: {usuario.calcular_divisao()}')

    elif opcao == 5:
        print('\n===== POTÊNCIA =====')

        numero1 = float(input('Base: '))
        numero2 = float(input('Potência: '))

    elif opcao == 6:
        print('\n===== RAIZ QUADRADA =====')

        numero1 = float(input('Número: '))

    elif opcao == 7:
        print('\n===== HISTÓRICO =====')

        for e in historico:
            print(e)

    elif opcao == 9:
        print('\nFinalizando o programa... Até logo!')
        break

    else:
        print('Número digitado inválido! Tente novamente.\n')

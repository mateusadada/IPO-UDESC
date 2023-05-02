# Receber 2 número e imprimir a soma, a subtração, multiplicação e divisão entre eles.

print('Bem vindo ao programa de cálculo da soma, subtração, multiplicação e divisão entre dois números!')

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f'\nSoma: {soma:.2f}'
      f'\nSubtração: {subtracao:.2f}'
      f'\nMultiplicação: {multiplicacao:.2f}'
      f'\nDivisão: {divisao:.2f}')

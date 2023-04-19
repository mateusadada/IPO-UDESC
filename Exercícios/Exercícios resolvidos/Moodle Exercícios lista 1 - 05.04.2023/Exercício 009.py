# Crie um algoritmo que leia dois números inteiros e depois mostre:
#  - o primeiro valor vezes o segundo
#  - o segundo valor menos o primeiro
#  - o inverso do primeiro valor vezes o segundo multiplicado por 5
#  - o quadrado do primeiro dividido pelo segundo elevado a -2

print('Bem vindo! Este programa recebe dois números e realiza várias operações.')

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))

print(f'\nO primeiro valor vezes o segundo: {numero1 * numero2}'
      f'\nO segundo valor menos o primeiro: {numero2 - numero1}'
      f'\nO inverso do primeiro valor vezes o segundo multiplicado por 5: {((numero1 * -1) * (numero2 * 5)):.1f}'
      f'\nO quadrado do primeiro dividido pelo segundo elevado a -2: {((numero1 ** 2) / (numero2 ** -2))}')

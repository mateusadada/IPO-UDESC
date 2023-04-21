# Escreva um programa que receberá um número e dirá se ele é positivo, negativo ou nulo

print('Bem vindo! Este programa informa se um número é positivo, negativo ou nulo.')

numero = int(input('Digite um número: '))

if numero < 0:
    print(f'\nO número {numero} é negativo')
elif numero > 0:
    print(f'\nO número {numero} é positivo')
else:
    print(f'\nO número {numero} é nulo')

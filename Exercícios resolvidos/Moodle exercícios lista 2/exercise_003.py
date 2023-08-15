# Calcule se um número é par ou ímpar.

print('Bem vindo ao programa que informa se um número é par ou ímpar!')

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'\nO número {numero} é par')
else:
    print(f'\nO número {numero} é ímpar')

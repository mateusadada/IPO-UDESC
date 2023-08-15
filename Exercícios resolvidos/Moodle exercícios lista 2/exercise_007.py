# Faça um programa que peça dois números e imprima o maior deles.

print('Bem-vindo ao programa de cálculo do maior número entre dois!')

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

maior = numero_1

if numero_1 == numero_2:
    print(f'\nOs dois números são iguais ({numero_1})')
elif numero_2 > numero_1:
    print(f'\nO segundo número ({numero_2}) é maior que o primeiro ({numero_1})')
else:
    print(f'\nO primeiro número ({numero_1}) é maior que o segundo ({numero_2})')

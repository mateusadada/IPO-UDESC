# Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida troque o valor das variáveis
# e exiba na tela - Trocar (inverter) valores de duas variáveis.

print('Bem vindo ao programa que inverte os valores de duas variáveis!')

a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))

print(f'\n1º valor = {a}'
      f'\n2º valor = {b}'
      '\n\n*** INVERTENDO ***')

aux = a
a = b
b = aux

print(f'\n1º valor = {a}'
      f'\n2º valor = {b}')

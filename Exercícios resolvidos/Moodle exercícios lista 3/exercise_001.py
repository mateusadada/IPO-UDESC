# Crie uma lista de números inteiros e exiba o valor máximo e mínimo.

print('Bem-vindo ao programa que exibe os valores máximo e mínimo de uma lista!')

lista = [5, 4, 9, 8, 45, 36, -74, -85, 12, -74]
maximo = lista[0]
minimo = lista[0]

print(f'Lista: {lista}')

for e in lista:
    if e > maximo:
        maximo = e
    if e < minimo:
        minimo = e

print(f'\nMáximo: {maximo}'
      f'\nMínimo: {minimo}')

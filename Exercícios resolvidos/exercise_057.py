# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

print('Bem vindo ao programa que gera uma lista sem números repetidos!')

lista_1 = [1, 2, 9, 7, 5, 6, 4, 3, 1, 12]
lista_2 = [5, 6, 2, 3, 2, 5, 9, 1, 5, 12]
lista_3 = []

print(f'Lista 1: {lista_1}'
      f'\nLista 2: {lista_2}')

for e in lista_1:
    if e not in lista_3:
        lista_3.append(e)

for e in lista_2:
    if e not in lista_3:
        lista_3.append(e)

print(f'\n*** Sem elementos repetidos ***'
      f'\nLista 3: {lista_3}')

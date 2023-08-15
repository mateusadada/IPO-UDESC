# Faça um programa para copiar listas independentemente.

print('Bem vindo ao programa que copia listas independentemente!')

lista_1 = [1, 2, 3]
lista_2 = lista_1[:]

print(f'A lista 1 é {lista_1}'
      f'\nA lista 2 é {lista_2}')

lista_2[1] = 99

print(f'\nModificando a lista 2: {lista_2}'
      f'\nA lista 1 é {lista_1}')

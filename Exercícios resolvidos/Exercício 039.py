# Faça um programa de repetição com tamanho de lista usando len.

print('Bem vindo ao programa que exibe o tamanho da lista e os elementos!')

lista = [2, 4, 5, 9, 6, 7, 8, 3, 4, 10, 55, 22, 147, 17]

print(f'\nA quantidade de elementos é {len(lista)}'
      f'\nOs números são:')

for i in lista:
    print(f'- {i}')

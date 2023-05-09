# Escrever um programa que leia 5 números float e imprima-os em ordem inversa.

print('Bem vindo ao programa que exibe a ordem inversa de uma lista!')

lista = []

for e in range(0, 5):
    lista.append(float(input(f'Digite o {e + 1}º número: ')))

print(f'\nLista: {lista}'
      '\n\nLista inversa: ', end='')

for e in range(4, -1, -1):
    print(lista[e], end=', ')

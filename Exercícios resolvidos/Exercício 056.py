# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
# Lista 3: lista 1 + lista 2

print('Bem vindo ao programa que exibe uma terceira lista a partir de duas informadas!')

lista_1 = []
lista_2 = []

quantidade = int(input('*** LISTA 1 ***'
                       '\nAdicionar quantos números? '))

for e in range(0, quantidade):
    lista_1.append(int(input(f'{e + 1}º número: ')))

lista_3 = lista_1[:]

quantidade = int(input('\n*** LISTA 2 ***'
                       '\nAdicionar quantos números? '))

for e in range(0, quantidade):
    lista_2.append(int(input(f'{e + 1}º número: ')))
    lista_3.append(lista_2[e])

print(f'\nLista 1: {lista_1}'
      f'\nLista 2: {lista_2}'
      f'\nLista 3 (soma das duas): {lista_3}')

# Faça um programa para ordenar a lista em ordem decrescente. L=[2,1,5,4,3] deve ser ordenada como L=[5,4,3,2,1].

print('Bem-vindo ao programa que exibe a lista em ordem decrescente!')

lista = [2, 1, 5, 4, 3]

print(f'Lista: {lista}')

for i in range(0, len(lista) - 1):
    for j in range(i + 1, len(lista)):
        if lista[i] < lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(f'\nLista ordenada: {lista}')

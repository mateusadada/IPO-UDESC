# Crie uma lista de números e ordene do menor para o maior.

print('Bem-vindo ao programa que ordena uma lista em ordem crescente!')

lista = [5, 7, -7, 85, 98, -72, 0, 54, -7, 85, -1200]

print(f'Lista: {lista}')

for i in range(0, len(lista) - 1):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(f'\nLista ordenada: {lista}')

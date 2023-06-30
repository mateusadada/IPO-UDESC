# Crie uma lista de números e remova o primeiro e último elemento.

print('Bem-vindo ao programa que remove o primeiro e o último número de uma lista!')

lista = list(range(1, 50, 4))

print(f'Lista: {lista}')

lista = lista[1:-1]

print(f'\nLista atualizada: {lista}')

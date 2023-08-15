# Crie uma lista de números e encontre a soma dos elementos.

print('Bem-vindo ao programa que soma os números de uma lista!')

lista = list(range(1, 100, 4))
soma = 0

print(f'Lista: {lista}')

for e in lista:
    soma += e

print(f'\nSoma dos elementos: {soma}')

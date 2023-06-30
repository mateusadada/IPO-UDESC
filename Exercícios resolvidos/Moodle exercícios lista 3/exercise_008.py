# Crie uma lista de números e encontre a média.

print('Bem-vindo ao programa de cálculo da média de uma lista!')

lista = list(range(1, 200, 7))
soma = 0

print(f'Lista: {lista}')

for e in lista:
    soma += e

print(f'\nA soma dos números é {soma} e a média é {soma / len(lista)}')

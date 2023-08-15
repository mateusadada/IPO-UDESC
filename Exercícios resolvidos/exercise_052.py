# Inicializar um vetor com valores 2, 4, 6, 8, 10. Calcular e imprimir a soma dos valores.

print('Bem vindo ao programa de cálculo da média dos valores de uma lista!')

lista = [2, 4, 6, 8, 10]
soma = 0

print(f'Lista: {lista}')

for e in lista:
    soma += e

print(f'\nSoma dos valores da lista: {soma}')

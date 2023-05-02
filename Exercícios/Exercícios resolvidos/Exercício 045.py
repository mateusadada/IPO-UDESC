# Faça um programa para ler N notas e imprimir ao final elas e a média aritmética.

print('Bem vindo ao programa de cálculo da média de N notas!')

lista = []
soma = 0
quantidade_notas = int(input('Deseja incluir quantas notas? '))

for i in range(0, quantidade_notas, 1):
    lista.append(float(input(f'Digite a nota ({i + 1}/{quantidade_notas}): ')))
    soma += lista[i]

print(f'\nTodas as {quantidade_notas} notas: {lista}'
      f'\nMédia aritmética: {soma / quantidade_notas:.2f}')

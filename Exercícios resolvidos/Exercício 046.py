# Faça um programa para verificar o maior número dentro de uma lista usando for.

print('Bem vindo ao programa que informa o maior número dentro uma lista!')

lista = [71, 3, 92, 13, 50, 66, 58, 35, 10, 85, 20, 77, 47, 2, 61, 25, 53, 30, 81, 42]

print(f'Lista: {lista}')

maior = lista[0]

for i in lista:
    if i > maior:
        maior = i

print(f'\nO maior número é {maior}')

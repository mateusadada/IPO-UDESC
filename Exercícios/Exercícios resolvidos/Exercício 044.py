# Faça um programa para pesquisar se um elementos está em uma lista usando for.

print('Bem vindo ao programa que pesquisa se um número está em uma lista!')

lista = list(range(1, 200, 22))

print(f'Lista: {lista}')

numero = int(input('Digite um número para pesquisar: '))

for indice, valor in enumerate(lista):
    if valor == numero:
        print(f'\nO número {numero} foi encontrado na posição {indice + 1}')
        break
else:
    print(f'\nO número {numero} não está na lista')

# Faça um programa para pesquisar se um elemento está em uma lista usando while.

print('Bem-vindo ao programa que pesquisa se um número está em uma lista!')

lista = list(range(1, 150, 17))
i = 0

print(f'Lista: {lista}')

numero = int(input('Digite um número para pesquisar: '))

while i < len(lista):
    if numero == lista[i]:
        print(f'\nO número {numero} foi encontrado na posição {i + 1}.')
        break

    i += 1
else:
    print(f'\nNão foi encontrado o número {numero} na lista.')

# Modifique o exercício anterior para pesquisar p e v em toda a lista e informando ao usuário a posição onde
# p e a posição onde v foram encontrados.

print('Bem vindo ao programa que pesquisa dois números em uma lista!')

lista = list(range(1, 50, 4))

print(f'Lista: {lista}')

valor_1 = int(input('Digite um valor: '))
valor_2 = int(input('Digite outro valor: '))

x = 0
flag = 0

while x < len(lista):
    if lista[x] == valor_1:
        print(f'\nFoi encontrado o número {valor_1} na posição {x + 1}')
        flag = 1
    if lista[x] == valor_2:
        print(f'\nFoi encontrado o número {valor_2} na posição {x + 1}')
        flag = 1
        break
    x += 1

if flag == 0:
    print(f'\nNão foram encontrados os números {valor_1} e {valor_2} na lista')

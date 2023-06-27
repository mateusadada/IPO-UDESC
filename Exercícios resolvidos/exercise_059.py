# Modifique o exemplo (slide 21) para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também será
# procurado. Na impressão, indique qual dos dois valores foi achado primeiro.

print('Bem vindo ao programa que pesquisa dois números em uma lista!')

lista = list(range(1, 50, 4))

print(f'Lista: {lista}')

valor_1 = int(input('Digite um valor: '))
valor_2 = int(input('Digite outro valor: '))

x = 0

while x < len(lista):
    if lista[x] == valor_1:
        print(f'\nFoi encontrado o número {valor_1} na posição {x + 1}')
        break
    elif lista[x] == valor_2:
        print(f'\nFoi encontrado o número {valor_2} na posição {x + 1}')
        break
    x += 1
else:
    print(f'\nNão foram encontrados os números {valor_1} e {valor_2} na lista')

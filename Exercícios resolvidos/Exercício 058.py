# Faça um programa para realizar a mesma tarefa do exemplo localizado no slide 21, mas sem utilizar a variável
# achou. Dica: observe a condição de saída do while
# Faça um programa de pesquisa de elementos

print('Bem vindo ao programa que pesquisa um número em uma lista!')

lista = list(range(1, 100, 17))

print(f'{lista}')
numero = int(input('Digite um número para pesquisar na lista: '))

x = 0

while x < len(lista):
    if lista[x] == numero:
        print(f'\nFoi encontrado o número {numero} na posição {x + 1}')
        break
    x += 1
else:
    print(f'\nNão foi encontrado o número {numero} na lista')

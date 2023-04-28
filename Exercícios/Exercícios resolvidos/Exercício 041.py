# Faça um programa para retirar elementos de uma lista usando del.

print('Bem vindo ao programa que retira números de uma lista!')

lista = list(range(1, 11))

while True:
    print(f'\nLista ({len(lista)}): {lista}')
    if len(lista) == 0:
        print('Não há mais nenhum número na lista!')
        break

    numero = int(input('Deseja retirar qual número (0 p/ sair)? '))

    if numero == 0:
        print('Saindo... Até logo!')
        break
    else:
        for indice, valor in enumerate(lista):
            if valor == numero:
                del lista[indice]
                break
        else:
            print('O número digitado não está na lista')

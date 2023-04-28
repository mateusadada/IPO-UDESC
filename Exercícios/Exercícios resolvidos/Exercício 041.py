# Faça um programa para retirar elementos de uma lista usando del.

lista = list(range(1, 11))

while True:
    print(f'\nElementos ({len(lista)}): {lista}')
    if len(lista) == 0:
        print('Não há mais nenhum número na lista!')
        break

    numero = int(input('Deseja retirar qual número (0 p/ sair)? '))

    if numero < 0:
        print('Erro! Digite um número positivo ou nulo')
    elif numero == 0:
        print('Saindo... Até logo!')
        break
    else:
        for i, e in enumerate(lista):
            if e == numero:
                print(i)
                del lista[i]
                break
        else:
            print('O número digitado não está na lista')

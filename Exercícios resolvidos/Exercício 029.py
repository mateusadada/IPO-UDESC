# Faça um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
# Imprima a tabuada da operação escolhida. Repita até que a opção sair seja escolhida

print('Bem vindo ao programa de cálculo de adição, subtração, divisão e multiplicação!')

while True:
    i = 1
    print('\n*** MENU DE TABUADAS ***'
          '\n[1] Adição'
          '\n[2] Subtração'
          '\n[3] Divisão'
          '\n[4] Multiplicação'
          '\n[9] Sair')
    numero = int(input('Opção desejada: '))

    if numero == 9:
        print('\nSAINDO... ATÉ LOGO')
        break

    elif numero == 1:
        print('\n*** TABUADA SOMA ***')
        while i <= 10:
            j = 1
            while j <= 10:
                print(f'{i} + {j} = {i + j}')
                j += 1
            i += 1
            print('---------------')

    elif numero == 2:
        print('\n*** TABUADA SUBTRAÇÃO ***')
        while i <= 10:
            j = 1
            while j <= 10:
                print(f'{i} - {j} = {i - j}')
                j += 1
            i += 1
            print('---------------')

    elif numero == 3:
        print('\n*** TABUADA DIVISÃO ***')
        while i <= 10:
            j = 1
            while j <= 10:
                print(f'{i} / {j} = {i / j:.1f}')
                j += 1
            i += 1
            print('---------------')

    elif numero == 4:
        print('\n*** TABUADA MULTIPLICAÇÃO ***')
        while i <= 10:
            j = 1
            while j <= 10:
                print(f'{i} * {j} = {i * j}')
                j += 1
            i += 1
            print('---------------')

    else:
        print('\nNúmero INVÁLIDO. Verifique e tente novamente!')

# Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos

quantidade = int(input('Deseja ver quantos números primos? '))
numero = 3
contador = 1

if quantidade < 1:
    print('\nVocê optou por ver nenhum número primo :(')
else:
    print(f'\n*** LISTANDO OS {quantidade} PRIMEIROS NÚMEROS PRIMOS ***\n'
          f'{contador}º primo: 2')
    while contador < quantidade:
        impar_divisor = 3
        while True:
            if numero == impar_divisor:
                contador += 1
                print(f'{contador}º primo: {numero}')
                numero += 2
                break

            elif numero % impar_divisor == 0:
                numero += 2
                break

            else:
                impar_divisor += 2

from time import sleep
from soma import Soma
from subtracao import Subtracao
from multiplicacao import Multiplicacao
from divisao import Divisao
from potencia import Potencia
from raiz_quadrada import RaizQuadrada


print('Bem vindo ao programa de cálculo!')

historico = []

while True:
    print('\n*** CALCULADORA ***'
          '\n1. Soma'
          '\n2. Subtração'
          '\n3. Multiplicação'
          '\n4. Divisão'
          '\n5. Potência'
          '\n6. Raiz quadrada'
          '\n7. Histórico'
          '\n8. Limpar a tela'
          '\n9. SAIR ')

    opcao = int(input('Opção: '))

    if opcao == 1:
        print('\n===== SOMA =====')

        numero1 = float(input('1º número: '))
        numero2 = float(input('2º número: '))
        usuario = Soma(numero1, numero2)

        print(f'Resultado: {usuario._calcular_soma()}')

        historico.append(f'{usuario.get_numero1()} + {usuario.get_numero2()} = {usuario.get_soma()}')

        print('=' * 16)

    elif opcao == 2:
        print('\n===== SUBTRAÇÃO =====')

        numero1 = float(input('1º número: '))
        numero2 = float(input('2º número: '))
        usuario = Subtracao(numero1, numero2)

        print(f'Resultado: {usuario._calcular_subtracao()}')

        historico.append(f'{usuario.get_numero1()} - {usuario.get_numero2()} = {usuario.get_subtracao()}')

        print('=' * 21)

    elif opcao == 3:
        print('\n===== MULTIPLICAÇÃO =====')

        numero1 = float(input('1º número: '))
        numero2 = float(input('2º número: '))
        usuario = Multiplicacao(numero1, numero2)

        print(f'Resultado: {usuario._calcular_multiplicacao()}')

        historico.append(f'{usuario.get_numero1()} * {usuario.get_numero2()} = {usuario.get_multiplicacao()}')

        print('=' * 25)

    elif opcao == 4:
        print('\n===== DIVISÃO =====')

        numero1 = float(input('Numerador: '))

        while True:
            numero2 = float(input('Denominador: '))

            if numero2 != 0:
                usuario = Divisao(numero1, numero2)
                break
            else:
                print('## O denominador não pode ser nulo!')

        print(f'Resultado: {usuario._calcular_divisao():.2f}')

        historico.append(f'{usuario.get_numero1()} / {usuario.get_numero2()} = {usuario.get_divisao():.2f}')

        print('=' * 19)

    elif opcao == 5:
        print('\n===== POTÊNCIA =====')

        numero1 = float(input('Base: '))
        numero2 = float(input('Potência: '))
        usuario = Potencia(numero1, numero2)

        print(f'Resultado: {usuario._calcular_potencia()}')

        historico.append(f'{usuario.get_numero1()} elevado a {usuario.get_numero2()} = {usuario.get_potencia()}')

        print('=' * 20)

    elif opcao == 6:
        print('\n===== RAIZ QUADRADA =====')

        numero1 = float(input('Número: '))
        usuario = RaizQuadrada(numero1)

        print(f'Resultado: {usuario._calcular_raiz_quadrada():.2f}')

        historico.append(f'√{usuario.get_numero1()} = {usuario.get_raiz_quadrada():.2f}')

        print('=' * 25)

    elif opcao == 7:
        print(f'\n===== HISTÓRICO - Total {len(historico)} =====')

        for e in historico:
            print(e)

        print('=' * 31)

    elif opcao == 8:
        print('\n===== LIMPANDO A TELA =====')

        for i in list(range(5, -1, -1)):
            sleep(0.6)
            print(' ' * 13, i)

        print("\n" * 100)

    elif opcao == 9:
        print('\nPrograma encerrado. Obrigado por utilizar!')
        break

    else:
        print('Número digitado inválido! Tente novamente.\n')

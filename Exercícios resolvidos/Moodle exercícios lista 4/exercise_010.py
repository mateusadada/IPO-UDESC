# Faça um programa, com um menu, que permita escolher qual das funções dos exercícios anteriores será executada.
# Obs.: - os dados passados como parâmetros podem ser solicitados do usuário via 'input'.
# Sugestão: usar 'função main' e escrever o código em um único bloco.

def produto(a, b, c):
    return a * b * c


def fatorial(fat):
    total = 1
    if fat < 1:
        return 'ERRO! O número informado é negativo ou neutro'
    else:
        while fat > 0:
            total *= fat
            fat -= 1
        return total


def media(a, b, c, d):
    return (a + b + c + d) / 4


def media_ponderada(a, a1, b, b1, c, c1, d, d1):
    return (a * a1 + b * b1 + c * c1 + d * d1) / (a1 + b1 + c1 + d1)


def calculaPreco(valor_inicial, desconto_percentual):
    preco_final = valor_inicial - (valor_inicial * desconto_percentual / 100)
    return preco_final


def valor_maximo(lista):
    maximo = lista[0]
    for i in lista:
        if i > maximo:
            maximo = i
    return maximo


def ordem_inversa(lista):
    lista.reverse()
    return lista


def adicao_numeros_lista():
    lista_numeros = []
    while True:
        numero = input('Digite um número (fim p/ encerrar): ')
        if numero == 'fim':
            break
        else:
            lista_numeros.append(int(numero))
    return media_8_numeros(lista_numeros)


def media_8_numeros(lista):
    total = 0
    for i in lista:
        total += i
    return total / (len(lista))


def procurar_nome(lista, nome):
    for i in lista:
        if i == nome:
            return f'True! O nome {nome} está na lista!'
    else:
        return f'False! O nome {nome} NÃO está na lista!'


while True:
    escolha = int(input('*** ESCOLHA UMA ALTERNATIVA ***'
                        '\n1 - Produto de 3 números'
                        '\n2 - Fatorial'
                        '\n3 - Média de 4 notas'
                        '\n4 - Média ponderada de 4 notas'
                        '\n5 - Desconto'
                        '\n6 - Valor máximo'
                        '\n7 - Lista inversa'
                        '\n8 - Média de n números'
                        '\n9 - Procurar nome na lista'
                        '\nOpção: '))

    if escolha == 1:
        print('\nBem vindo ao programa de cálculo do produto de três números!')

        lista = []

        for i in range(3):
            numero = int(input(f'{i + 1}º número: '))
            lista.append(numero)

        print(f'\nO produto de {lista[0]}, {lista[1]} e {lista[2]} é {produto(lista[0], lista[1], lista[2])}')
        break

    elif escolha == 2:
        print('\nBem vindo ao programa de cálculo de fatorial de um número!')

        numero = int(input('Digite um número inteiro: '))

        print(f'\nO fatorial de {numero} é {fatorial(numero)}')
        break

    elif escolha == 3:
        print('\nBem vindo ao programa de cálculo da média de quatro notas de uma disciplina!')

        lista = []

        for i in range(4):
            nota = float(input(f'{i + 1}º nota: '))
            lista.append(nota)

        print(f'\nA média das notas é {media(lista[0], lista[1], lista[2], lista[3]):.2f}')
        break

    elif escolha == 4:
        print('\nem vindo ao programa de cálculo da média ponderada de quatro notas de uma disciplina!')

        notas = []
        peso_notas = []

        for i in range(4):
            nota = float(input(f'\n{i + 1}º nota: '))
            notas.append(nota)
            peso = int(input(f'{i + 1}º peso: '))
            peso_notas.append(peso)

        print(
            f'\nA média das notas é {media_ponderada(notas[0], peso_notas[0], notas[1], peso_notas[1], notas[2], peso_notas[2], notas[3], peso_notas[3]):.2f}')
        break

    elif escolha == 5:
        print('\nBem vindo ao programa de cálculo de desconto de um produto!')

        preco = float(input('Valor da compra: R$ '))
        desconto = float(input('Desconto (%): '))

        print(f'\nO valor do produto com desconto de {desconto}% é R$ {calculaPreco(preco, desconto):.2f} reais')
        break

    elif escolha == 6:
        numeros = []
        print('\nBem vindo ao programa que retorna o valor máximo de uma lista!')

        while True:
            numero = int(input('Digite um número (0 p/ sair): '))
            if numero == 0:
                break
            else:
                numeros.append(numero)

        print(f'\nLista: {numeros}'
              f'\nO valor máximo é {valor_maximo(numeros)}')
        break

    elif escolha == 7:
        numeros = []

        print('\nBem vindo ao programa que exibe a ordem inversa de uma lista!')

        while True:
            numero = int(input('Digite um número (0 p/ sair): '))
            if numero == 0:
                break
            else:
                numeros.append(numero)

        print(f'\nLista: {numeros}'
              f'\nA ordem inversa é {ordem_inversa(numeros)}')
        break

    elif escolha == 8:
        print('\nBem vindo ao programa de cálculo da média!')
        print(f'\nA média é {adicao_numeros_lista():.2f}')
        break

    elif escolha == 9:
        lista_nomes = ['Mateus', 'Julia', 'Livia', 'Ana', 'João', 'Cristiane', 'Paulo']

        print('\nBem vindo ao programa que verifica se um nome está em uma lista!'
              f'\nLista: {lista_nomes}')

        nome_a_procurar = input('\nProcurar qual nome? ')

        print(procurar_nome(lista_nomes, nome_a_procurar))
        break

    print()

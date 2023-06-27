# Fazer uma função que receba como parâmetro um número inteiro e retorne o fatorial desse número.

def fatorial(fat):
    total = 1
    if fat < 1:
        return 'ERRO! O número informado é negativo ou neutro'
    else:
        while fat > 0:
            total *= fat
            fat -= 1
        return total


print('Bem vindo ao programa de cálculo de fatorial de um número!')

numero = int(input('Digite um número inteiro: '))

print(f'\nO fatorial de {numero} é {fatorial(numero)}')

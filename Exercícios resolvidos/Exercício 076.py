# Exemplo de cálculo de fatorial.

def fatorial(fat):
    total = 1
    if fat < 1:
        return 'Erro! O número é negativo ou nulo'
    else:
        while fat > 1:
            total *= fat
            fat -= 1
        return total


print('Bem vindo ao programa de cálculo de fatorial a partir de uma função!')
numero = int(input('Digite um número: '))

print(f'\nFatorial de {numero}: {fatorial(numero)}')

# Exemplo do problema do fatorial com funções recursivas.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


print('Bem vindo ao programa de cálculo de fatorial a partir de uma função recursiva!')
print(f'\nO fatorial de 5 é {fatorial(5)}')

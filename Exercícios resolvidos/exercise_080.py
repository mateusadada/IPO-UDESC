# Exemplo do problema do fatorial modificado para facilitar o rastreamento.

def fatorial(n):
    print(f'\nCalculando o fatorial de {n}')
    if n == 0 or n == 1:
        print(f'Fatorial de {n} = 1')
        return 1
    else:
        fat = n * fatorial(n - 1)
        print(f'Fatorial de {n} = {fat}')
        return fat


print('Bem vindo ao programa de cálculo de fatorial a partir de uma função recursiva com rastreamento!')
print(f'\nO fatorial de 5 é {fatorial(5)}')

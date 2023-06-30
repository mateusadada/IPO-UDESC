# Faça um programa para copiar os elementos pares da lista V para a P e os ímpares do V para a I.

print('Bem-vindo ao programa que separa os números pares dos ímpares!')

V = list(range(1, 21))
P = []
I = []

for e in V:
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)

print(f'Lista: {V}'
      f'\n\nPares: {P}'
      f'\nÍmpares: {I}')

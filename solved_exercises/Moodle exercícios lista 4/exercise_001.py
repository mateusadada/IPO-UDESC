# Fazer uma função que recebe três argumentos e que retorne o produto desses três argumentos.

def produto(a, b, c):
    return a * b * c


print('Bem vindo ao programa de cálculo do produto de três números!')

lista = []

for i in range(3):
    numero = int(input(f'{i + 1}º número: '))
    lista.append(numero)

print(f'\nO produto de {lista[0]}, {lista[1]} e {lista[2]} é {produto(lista[0], lista[1], lista[2])}')

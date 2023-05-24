# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(a, b, c):
    return a + b + c


print('Bem vindo ao programa de cálculo da soma de três números!')

lista = []

for i in range(3):
    numero = int(input(f'{i + 1}º número: '))
    lista.append(numero)

print(f'\nA soma de {lista[0]}, {lista[1]} e {lista[2]} é {soma(lista[0], lista[1], lista[2])}')

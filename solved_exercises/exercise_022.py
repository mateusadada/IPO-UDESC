# Faça um programa que calcule a soma de 5 números digitados pelo usuário.

print('Bem vindo ao programa de cálculo da soma de cinco números!')

contador = 1
soma_total = 0

while contador <= 5:
    numero = int(input(f'Digite um número ({contador}/5): '))
    soma_total += numero
    contador += 1

print(f'\nSoma dos cinco números: {soma_total}')

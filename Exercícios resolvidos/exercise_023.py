# Faça um programa para calcular e imprimir a média de 5 números digitados pelo usuário.

print('Bem-vindo ao programa de cálculo da média de cinco números!')

contador = 1
soma_total = 0

while contador <= 5:
    numero = int(input(f'Digite um número ({contador}/5): '))
    soma_total += numero
    contador += 1

print(f'\nA média dos cinco números é igual a {soma_total/5:.2f}')

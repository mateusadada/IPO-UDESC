# Faça um programa para calcular e imprimir a média de 5 números digitados pelo usuário

contador = 1
media_total = 0

while contador <= 5:
    numero = int(input(f'Digite um número ({contador}/5): '))
    media_total += numero
    contador += 1

print(f'\nA média dos cinco números é igual a {media_total:.2f}')

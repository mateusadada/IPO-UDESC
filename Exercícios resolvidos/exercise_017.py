# Faça um programa para imprimir os números ímpares de 1 até o número digitado pelo usuário.

print('Bem-vindo ao programa que exibe os números ímpares de 1 até o limite informado!')

fim = int(input('Digite um número positivo: '))
x = 1

while x <= fim:
    print(x)
    x += 2

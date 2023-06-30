# Ler 5 inteiros do teclado e armazenar num vetor. Depois percorrer este vetor mostrando os números ímpares.

print('Bem-vindo ao programa que exibe os números ímpares digitados!')

numeros = []
impares = []

for e in range(0, 5):
    numeros.append(int(input(f'Digite um número inteiro ({e + 1}/5): ')))

for e in numeros:
    if e % 2 != 0:
        impares.append(e)

print(f'\nOs números ímpares são {impares}')

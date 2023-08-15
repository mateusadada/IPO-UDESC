# Faça um programa para somar vários números até que o usuário digite 0 (zero) para parar a leitura.

print('Bem vindo ao programa que soma vários números!')

soma = 0

while True:
    numero = int(input('Digite um número (0 p/ sair): '))
    if numero == 0:
        break
    soma += numero

print(f'\nA soma de todos os número é {soma}')

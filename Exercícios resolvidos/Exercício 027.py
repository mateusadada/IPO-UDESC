# Faça um programa que leia números inteiros do teclado, até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

print('Bem vindo ao programa que conta a quantidade de números digitados, além da soma e média aritmética!')

soma = 0
contador = 0

while True:
    numero = int(input('Digite um número inteiro (0 p/ sair): '))
    if numero == 0:
        break
    soma += numero
    contador += 1

print('\n*** DADOS ***'
      f'\nQuantidade de números digitados: {contador}'
      f'\nSoma: {soma}'
      f'\nMédia aritmética: {soma / contador:.2f}')

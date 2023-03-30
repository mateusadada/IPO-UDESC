# Faça um programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

numero1 = int(input('Digite o 1º valor: '))
numero2 = int(input('Digite o 2º valor: '))
numero3 = int(input('Digite o 3º valor: '))

maior = numero1
menor = numero1

if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3

print(f'\nMaior: {maior}'
      f'\nMenor: {menor}')

# Faça um programa que leia três números e mostre-os em ordem decrescente.

print('Bem-vindo ao programa que mostra três números em ordem decrescente!')

a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
c = int(input('Digite o 3º número: '))

print(f'\nOrdem digitada: {a}, {b} e {c}')

if a < b:
    aux = a
    a = b
    b = aux

if a < c:
    aux = a
    a = c
    c = aux

if b < c:
    aux = b
    b = c
    c = aux

print(f'\nOrdem decrescente: {a}, {b} e {c}')

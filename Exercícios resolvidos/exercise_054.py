# Dado os vetores A=[10, 11, 12, 13, 14, 15, 16, 17] e B=[1, 2, 3, 4, 5, 6, 7, 8], fazer um programa para somar os dois
# vetores e armazenar o resultado em um vetor C ( C[i]=A[i]+B[i] ).

print('Bem vindo ao programa de cálculo de soma de duas listas!')

A = [10, 11, 12, 13, 14, 15, 16, 17]
B = [1, 2, 3, 4, 5, 6, 7, 8]
C = []

print(f'\nLista A: {A}'
      f'\nLista B: {B}'
      f'\nLista C: {C}')

for i, e in enumerate(A):
    C.append(A[i] + B[i])

print(f'\nLista C com a soma de A e B: {C}')

# Escreva um programa que leia um número e verifique se é ou não um número primo.
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os
# números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero,
# o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único primo que é par.

print('Bem vindo ao programa de validação de número primo!')

numero = int(input('Digite um número inteiro: '))

i = 3
FLAG = 0

if numero % 2 == 0 or numero == 0 or numero == 1 or numero == 2:
    print(f'\nO número {numero} NÃO é primo!')

else:
    while True:
        if i >= numero:
            break
        if numero % i == 0:
            print(f'\nO número {numero} NÃO é primo!')
            FLAG = 1
            break
        i += 2
    if FLAG == 0:
        print(f'\nO número {numero} é primo!')

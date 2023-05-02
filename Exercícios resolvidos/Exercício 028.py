# Imprimir as tabuadas de multiplicação de 1 a 10

print('Bem vindo ao programa que mostra as tabuadas de multiplicação de 1 a 10!')

i = 1

while i <= 10:
    print(f'\n*** TABUADA DO {i} ***')
    j = 1
    while j <= 10:
        print(f'{i} x {j} = {i * j}')
        j += 1
    i += 1

# Faça um programa para exibir os resultados no mesmo formato de uma tabuada: 2x1=2, 2x2=4,...

x = 1

while x <= 10:
    print(f'*** TABUADA DO {x} ***')
    i = 1
    while i <= 10:
        print(f'{x} x {i} = {x * i}')
        i += 1
    x += 1
    print()

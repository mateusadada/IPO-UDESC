# Imprimir uma tabuada (de 1 a 10) de adiação de um número digitado pelo usuário

numero = int(input('Digite um número: '))
x = 1

print(f'\n*** TABUADA DO {numero} ***\n')

while x <= 10:
    print(f'{numero} x {x} = {numero * x}')
    x += 1

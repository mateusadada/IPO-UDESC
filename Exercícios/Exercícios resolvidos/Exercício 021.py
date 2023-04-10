# Faça um programa de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 até 10

inicio = int(input('Digite o início de uma tabuada: '))
fim = int(input('Digite o fim de uma tabuada: '))

print('\n*** TABUADA ***\n')
while inicio <= fim:
    print(f'{inicio} x {fim} = {inicio * fim}')
    inicio += 1

# Exemplo 1 do PDF Slides da aula - Parte 5

print('Bem vindo ao programa de cálculo do maior número entre dois digitados!')

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))

if a > b:
    print(f'\nO primeiro número ({a}) é maior!')
elif b > a:
    print(f'\nO segundo número ({b}) é maior!')
else:
    print('\nOs dois números são iguais!')

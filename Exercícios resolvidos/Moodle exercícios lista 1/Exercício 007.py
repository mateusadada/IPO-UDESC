# Calcule a área de um círculo cujo raio será informado pelo usuário e exiba o resultado na tela.

from math import pi

print('Bem vindo ao programa de cálculo da área de um círculo!')

raio = float(input('Digite o raio do círculo (cm²): '))

if raio < 0:
    print('\nErro! O raio informado é negativo')
else:
    area = (raio ** 2) * pi
    print(f'\nA área do círculo é {area:.2f}cm²')

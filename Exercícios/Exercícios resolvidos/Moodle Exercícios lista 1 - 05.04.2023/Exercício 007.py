# Calcule a área de um círculo cujo raio será informado pelo usuário e exiba o resultado na tela

import math

raio = float(input('Digite o raio de um círculo (cm²): '))

if raio < 0:
    print('\nErro! O raio informado é negativo')
else:
    area = (raio ** 2) * math.pi
    print(f'\nA área do círculo é {area:.2f}cm²')

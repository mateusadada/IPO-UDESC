# Escreva uma função que receba o lado de um quadrado e retorne sua área (A = lado²).
# Exemplo de valores esperados: área_quadrado(4) = 16

def area_quadrado(lado):
    return pow(lado, 2)


print('Bem vindo ao programa de cálculo da área de um quadrado!')
lado_quadrado = float(input('Digite o lado (m²): '))

print(f'\nA área é {area_quadrado(lado_quadrado):.1f}m²')

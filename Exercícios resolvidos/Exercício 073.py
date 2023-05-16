# Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A = (base x altura)/2).
# Exemplo de valores esperados: área_triângulo(5,8) = 20

def area_triangulo(base, altura):
    return (base * altura) / 2


print('Bem vindo ao programa de cálculo da área de triângulo!')
base = float(input('Digite a base (m²): '))
altura = float(input('Digite a altura (m²): '))

print(f'\nA área é {area_triangulo(base, altura):.1f}m²')

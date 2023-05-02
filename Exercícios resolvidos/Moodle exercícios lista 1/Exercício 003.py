# Calcule a área, em cm², de um triângulo retângulo, recebendo a base e a altura. Exiba o resultado na tela

print('Bem vindo ao programa de cálculo da área de um triângulo retângulo!')

base = float(input('Digite a base (m²): '))
altura = float(input('Digite a altura (m²): '))

area = (base * altura) / 2

print(f'\nA área do triângulo é {area:.1f}m²')

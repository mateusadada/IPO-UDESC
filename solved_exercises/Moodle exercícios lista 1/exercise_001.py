# Receba três notas de usuários e calcule a média simples, exibindo o resultado na tela.

print('Bem vindo ao programa de cálculo de média simples!')

i = 1
soma = 0

while i <= 3:
    numero = float(input(f'Digite a {i}ª nota: '))
    soma += numero
    i += 1

media = soma / 3

print(f'\nA média das três notas é {media:.2f}')

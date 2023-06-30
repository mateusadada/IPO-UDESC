# Receber as 4 notas de IPO e calcular a média semestral.

print('Bem-vindo ao programa de cálculo da média semestral de IPO!')

i = 1
soma = 0

while i <= 4:
    nota = float(input(f'Digite a {i}ª nota: '))
    soma += nota
    i += 1

media_semestral = soma / 4

print(f'\nA média semestral é {media_semestral:.1f}')

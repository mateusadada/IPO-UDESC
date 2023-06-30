print('Bem-vindo ao programa de cálculo da média de cinco notas informadas!')

notas = [0, 0, 0, 0, 0]
soma = 0
i = 0

while i < 5:
    notas[i] = float(input(f'Digite a {i + 1}º nota: '))
    soma += notas[i]
    i += 1

print(f'\nA média é {soma / i:.2f}')

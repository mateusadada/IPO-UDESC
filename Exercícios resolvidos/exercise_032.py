print('Bem-vindo ao programa de cálculo da média de cinco notas pré-estabelecidas sem informar quais são!')

notas = [6, 7, 5, 8, 9]
soma = 0
i = 0

while i < 5:
    soma += notas[i]
    i += 1

print(f'\nA média das notas é {soma / i:.2f}')

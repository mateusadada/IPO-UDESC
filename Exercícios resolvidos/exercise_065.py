# Faça um programa que calcule a média de cinco notas informadas e mostre qual nota está mais próxima dela.

print('Bem-vindo ao programa que exibe a nota mais próxima da média de cinco notas!')

notas = []
diferenca_com_media = []
soma = 0

for i in range(5):
    notas.append(float(input(f'{i + 1}º nota: ')))
    soma += notas[i]

media = soma / len(notas)
print(f'\nNotas informadas: {notas}'
      f'\nMédia: {media:.1f}')

for i in range(len(notas)):
    diferenca = notas[i] - media
    if diferenca < 0:
        diferenca = diferenca * - 1
    diferenca_com_media.append(diferenca)

for i in range(0, len(diferenca_com_media) - 1):
    for j in range(1, len(diferenca_com_media)):
        if diferenca_com_media[i] > diferenca_com_media[j]:
            aux = diferenca_com_media[i]
            diferenca_com_media[i] = diferenca_com_media[j]
            diferenca_com_media[j] = aux

            aux = notas[i]
            notas[i] = notas[j]
            notas[j] = aux

print(f'\nNota mais próxima da média: {notas[0]}')

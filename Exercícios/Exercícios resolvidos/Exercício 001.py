# Receber as 4 notas de IPOO e calcular a média semestral.

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
nota4 = float(input('Digite a nota 4: '))

media_semestral = (nota1 + nota2 + nota3 + nota4) / 4

print(f'\nA média semestral é {media_semestral:.2f}')

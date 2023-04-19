# Desenvolva um programa para calcular o custo e quantas latas de tintas serão utilizados para pintar tanques 
# cilíndricos de combustível sendo que:
#  - a lata de tinta custa R$120,00
#  - cada lata contém 5 litros
#  - cada litro pinta 4m²
#  - a altura e o raio do tanque serão informados pelo usuário
#  - mostre na tela a área do tanque, a quantidade de latas e o custo total

from math import pi, ceil

altura = float(input('Digite a altura do tanque: '))
raio = float(input('Digite o raio do tanque: '))

area = (raio + altura) * 2 * raio * pi
litro = area / 4
if litro != int(litro):
    litro = ceil(litro)

lata = litro / 5
if lata != int(lata):
    lata = ceil(lata)

custo_total = lata * 120

print(f'\nÁrea do tanque: {area:.2f}m²'
      f'\nQuantidade de latas necessárias: {lata}'
      f'\nCusto total: R$ {custo_total:.2f} reais')

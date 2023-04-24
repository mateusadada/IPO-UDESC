# Faça um programa que leia a idade e a altura de uma pessoa e verifique se ela pode entrar em um parque de diversões.
# Para entrar no parque a pessoa deve ter pelo menos 12 anos e medir mais de 1,50m.

print('Bem vindo! Este programa verifica se uma pessoa pode entrar no parque de diversões.')

idade = int(input('Digite a idade: '))
altura = float(input('Digite a altura (m): '))

if idade >= 12 and altura > 1.5:
    print('\nA pessoa pode entrar!')
else:
    print('\nInfelizmente, a pessoa não pode entrar.')

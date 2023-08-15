# Faça um programa que leia a idade e a altura de uma pessoa e verifique se ela pode entrar em um parque de diversões.
# Para entrar no parque a pessoa deve ter pelo menos 12 anos e medir mais de 1,50 m.

print('Bem vindo ao programa que verifica se uma pessoa entrar em um parque de diversões!'
      '\n- Idade mínima: 12 anos'
      '\n- Altura mínima: 1,51cm')

idade = int(input('\nDigite a idade: '))
altura = float(input('Digite a altura (m): '))

if idade < 12 and altura <= 1.5:
    print('\nA pessoa NÃO pode entrar devido à idade e à altura.')
elif idade < 12 and altura > 1.5:
    print('\nA pessoa NÃO pode entrar devido à idade.')
elif idade >= 12 and altura <= 1.5:
    print('\nA pessoa NÃO pode entrar devido à altura.')
else:
    print('\nA pessoa pode entrar!')

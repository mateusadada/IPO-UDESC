# Faça um programa que calcule se um ano é ou não bissexto (se necessário, procure a regra na internet)

print('Bem vindo ao programa de validação de ano bissexto!')

ano = int(input('Digite um ano: '))

if ano < 1:
    print('\nErro! Não existe ano bissexto negativo')
elif ano % 4 != 0:
    print(f'\nO ano {ano} NÃO é bissexto')
elif ano % 100 == 0 and ano % 400 != 0:
    print(f'\nO ano {ano} NÃO é bissexto')
else:
    print(f'\nO ano {ano} é bissexto')

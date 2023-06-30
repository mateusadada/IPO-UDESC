# Faça um programa que pergunte em que turno você estuda. Peça para digitar M-Matutino, V-Vespertino ou N-Noturno. 
# - Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('Bem-vindo ao programa que faz uma saudação dependendo do turno que você estuda!')

turno = input('Em qual turno você estuda?'
              '\nOpções: M-Matutino, V-Vespertino ou N-Noturno'
              '\nResposta: ')

if turno == 'M' or turno == 'm':
    print('\nBom dia!')
elif turno == 'V' or turno == 'v':
    print('\nBoa tarde!')
elif turno == 'N' or turno == 'n':
    print('\nBoa noite!')
else:
    print('\nValor inválido!')

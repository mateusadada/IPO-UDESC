# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-Matutino, V-Vespertino
# ou N-Noturno. Imprima a mensagem "Bom dia!", "Boa tarde!", "Boa noite!" ou "Valor inválido!", conforme o caso.

print('Bem-vindo ao programa que faz uma saudação dependendo do turno que você estuda!')

turno = input('Em qual turno você trabalha (M-Matutino, V-Vespertino ou N-Noturno)? ')

if turno == 'M':
    print('\nBom dia!')
elif turno == 'V':
    print('\nBoa tarde!')
elif turno == 'N':
    print('\nBoa noite!')
else:
    print('\nValor inválido!')

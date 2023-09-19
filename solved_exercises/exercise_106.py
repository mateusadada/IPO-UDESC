# Exercícios com strings e procurando uma substring em uma string.

print('Bem vindo ao programa que realiza testes com a manipulação de strings!\n')

frase = 'Olá, mundo!'
print(frase)
print(f'Tipo da string: {type(frase)}')
print(f'Tamanho: {len(frase)}')
print('Concatenação:', 'Meu Brasil ' + 'brasileiro')
frase_alterada = frase.replace('mundo', 'meu abacate')

print(frase_alterada)
print(frase.startswith('Olá'))
print(frase.endswith('mundo'))
print(frase_alterada.count('abacate'))

# procurando uma substring em uma string
string = 'Universidade do Estado de Santa Catarina'
substring = 'Estado'
print(substring in string)

if substring in string:
    print('Encontrou')

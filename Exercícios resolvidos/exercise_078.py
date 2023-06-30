# Execute o programa que permite modificar uma variável global numa função, pela instrução global.

def muda_e_imprime():
    global a
    a = 7
    return print(f'A dentro da função: {a}')


a = 5

print('Bem-vindo ao programa que deixa uma varivável global dentro de uma função!')
print(f'\nA antes de mudar: {a}')
muda_e_imprime()
print(f'A fora da função: {a}')

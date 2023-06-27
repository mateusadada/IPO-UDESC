# Variáveis locais e globais (página 13).

def muda_e_imprime():
    a = 7
    print('A dentro da função:', a)


a = 5

print('Bem vindo ao programa que exibe o valor de a usando variáveis locais e globais!')
print('A antes de mudar:', a)
muda_e_imprime()
print('A depois de mudar:', a)

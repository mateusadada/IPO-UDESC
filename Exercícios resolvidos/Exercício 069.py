# Exemplo de reutilização da função épar em outra função.

def e_par(x):
    return x % 2 == 0


def par_impar(x):
    if e_par(x):
        return 'par'
    else:
        return 'ímpar'


print('Bem vindo ao programa que exibe se um número é par ou não; função em função!')
print(f'2: {par_impar(2)}'
      f'\n3: {par_impar(3)}'
      f'\n10: {par_impar(10)}')

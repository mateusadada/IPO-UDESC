# Modifique a classe TV de forma que, se pedir para mudar o canal para baixo, além do mínimo, vá para o canal máximo.
# Se mudar para cima, além do canal máximo, que volte ao canal mínimo. Exemplo:
# >>> tv = TV(2,10)
# >>> tv.muda_canal_para_baixo()
# >>> tv.canal
# 10
# >>> tv.muda_canal_para_cima()
# >>> tv.canal
# 2


class TV:
    def __init__(self, canal, minimo, maximo):
        self.ligada = False
        self.canal = canal
        self.canal_minimo = minimo
        self.canal_maximo = maximo

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.canal_minimo:
            self.canal -= 1
        else:
            self.canal = self.canal_maximo

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_maximo:
            self.canal += 1
        else:
            self.canal = self.canal_minimo


print('Bem-vindo ao programa que exibe o canal caso ultrapasse o máximo ou o mínimo!')

TV_da_sala = TV(10, 1, 10)

print(f'Canal inicial: {TV_da_sala.canal}'
      f'\nMáximo: {TV_da_sala.canal_maximo}'
      f'\nMínimo: {TV_da_sala.canal_minimo}\n')

TV_da_sala.muda_canal_para_cima()

print(f'Canal após aumentar 1: {TV_da_sala.canal}')

TV_da_sala.muda_canal_para_baixo()

print(f'Canal após diminuir 1: {TV_da_sala.canal}')

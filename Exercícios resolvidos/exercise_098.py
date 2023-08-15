# Adicionando comportamento à classe.

class TV:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def muda_canal_para_baixo(self):
        self.canal -= 1

    def muda_canal_para_cima(self):
        self.canal += 1


print('Bem vindo ao programa que adiciona comportamento à classe!')

tv_da_sala = TV()

print(f'Canal atual: {tv_da_sala.canal}')

tv_da_sala.muda_canal_para_cima()
tv_da_sala.muda_canal_para_cima()

print(f'Canal após mudar 2x para cima: {tv_da_sala.canal}')

tv_da_sala.muda_canal_para_baixo()

print(f'Canal após mudar para baixo: {tv_da_sala.canal}')

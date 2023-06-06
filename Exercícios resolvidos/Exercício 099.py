# Passagem de parâmetros.

class TV:
    def __init__(self, minimo, maximo):
        self.ligada = False
        self.canal = 2
        self.canal_minimo = minimo
        self.canal_maximo = maximo

    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.canal_minimo:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.canal_maximo:
            self.canal += 1


print('Bem-vindo ao programa que exibe o canal máximo e mínimo de uma TV!')

TV_da_sala = TV(1, 120)

for x in range(0, 120):
    TV_da_sala.muda_canal_para_cima()

print(f'Canal máximo após subir 120x: {TV_da_sala.canal}')

for x in range(0, 120):
    TV_da_sala.muda_canal_para_baixo()

print(f'Canal mínimo após descer 120x: {TV_da_sala.canal}')

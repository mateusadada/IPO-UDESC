# A classe TV inicializa o canal com 2. Modifique a classe TV para receber o canal inicial no seu construtor.

class TV:
    def __init__(self, canal, minimo, maximo):
        self.ligada = False
        self.canal_inicial = canal
        self.canal_minimo = minimo
        self.canal_maximo = maximo

    def muda_canal_para_baixo(self):
        if self.canal_inicial - 1 >= self.canal_minimo:
            self.canal_inicial -= 1

    def muda_canal_para_cima(self):
        if self.canal_inicial + 1 <= self.canal_maximo:
            self.canal_inicial += 1


print('Bem-vindo ao programa que exibe o canal máximo e mínimo de uma TV após mudar 120x!')

TV_da_sala = TV(47, 1, 120)

print(f'Canal inicial: {TV_da_sala.canal_inicial}\n')

for x in range(0, 120):
    TV_da_sala.muda_canal_para_cima()

print(f'Canal máximo após subir 120x: {TV_da_sala.canal_inicial}')

for x in range(0, 120):
    TV_da_sala.muda_canal_para_baixo()

print(f'Canal mínimo após descer 120x: {TV_da_sala.canal_inicial}')

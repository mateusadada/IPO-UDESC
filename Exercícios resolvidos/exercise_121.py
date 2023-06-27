# Encapsulamento. Para resolver o problema do Banco X, precisa-se de outra classe, Conta (salvar como contas.py,
# (Exercício121.py) incluindo getters e setters), para representar uma conta do banco com seus clientes e seu saldo.

class Conta:
    _saldo = 0
    __clientes = None
    __numero = None

    def __init__(self, clientes, numero, saldo):
        self._saldo = saldo
        self.__clientes = clientes
        self.__numero = numero

    def resumo(self):
        print(f'CC Número; {self.__numero} | Saldo: {self._saldo}')

    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor

    def deposito(self, valor):
        self._saldo += valor

# Crie uma classe Pessoa e outras duas classes derivadas da primeira: PessoaFisica e PessoaJuridica.

class Pessoa:
    __nome = None
    __idade = None

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade


class PessoaFisica(Pessoa):
    __CPF = None

    def __init__(self, CPF, nome, idade):
        super().__init__(nome, idade)
        self.__CPF = CPF

    def set_CPF(self, CPF):
        self.__CPF = CPF

    def get_CPF(self):
        return self.__CPF


class PessoaJuridica(Pessoa):
    __CNPJ = None

    def __init__(self, CNPJ, nome, idade):
        super().__init__(nome, idade)
        self.__CNPJ = CNPJ

    def set_CNPJ(self, CNPJ):
        self.__CNPJ = CNPJ

    def get_CNPJ(self):
        return self.__CNPJ


print('Bem-vindo ao programa de classe e de subclasses (herança)!')

fisica = PessoaFisica('123.456.789-00', 'Fulano da Silva', 18)
juridica = PessoaJuridica('12.123.123/0001-01', 'Empresa XYZ Ltda', 5)

print(f'\n*** Pessoa Física ***'
      f'\nCPF: {fisica.get_CPF()}'
      f'\nNome: {fisica.get_nome()}'
      f'\nIdade: {fisica.get_idade()}')

print(f'\n*** Pessoa Jurídica ***'
      f'\nCNPJ: {juridica.get_CNPJ()}'
      f'\nNome: {juridica.get_nome()}'
      f'\nIdade: {juridica.get_idade()}')

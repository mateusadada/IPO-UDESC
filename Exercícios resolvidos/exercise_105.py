# Criar uma classe Aluno com atributos matricula, nome, nota1 e nota2. Criar métodos para definir e retornar atributos
# e calcular a média de notas de um aluno.

class Aluno:
    def __init__(self, matricula=None, nome=None, nota1=None, nota2=None):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def set_matricula(self, matricula):
        self.matricula = matricula

    def set_nome(self, nome):
        self.nome = nome

    def set_nota1(self, nota1):
        self.nota1 = nota1

    def set_nota2(self, nota2):
        self.nota2 = nota2

    def get_matricula(self):
        return self.matricula

    def get_nome(self):
        return self.nome

    def get_nota1(self):
        return self.nota1

    def get_nota2(self):
        return self.nota2

    def media(self, nota1, nota2):
        return (nota1 + nota2) / 2


print('Bem-vindo ao programa de cálculo da média de um aluno!')

while True:
    nome = input('Informe um nome (fim p/ sair): ')

    if nome == 'fim':
        break

    matricula = int(input('Matrícula: '))
    nota1 = float(input('1º nota: '))
    nota2 = float(input('2º nota: '))

    estudante = Aluno()
    estudante.set_nome(nome)
    estudante.set_matricula(matricula)
    estudante.set_nota1(nota1)
    estudante.set_nota2(nota2)

    print(f'\nAluno {estudante.get_nome()} com a média {estudante.media(nota1, nota2):.2f}\n')

""""Defina os atributos e métodos das seguintes classes:
Pessoa:
"""


class Pessoa:

    def __init__(self, Nome, Idade, Genero,):
        self.Nome = Nome
        self.Idade = Idade
        self.Genero = Genero


    def base(self):
        p = Pessoa

        p.Nome = input("Digite seu nome: ")
        p.Idade = int(input("Digite sua idade: "))
        p.Genero = input("Digite seu gênero: ") #Masculino ou Femnino!

        print('\033[7;97m'+"Nome: ", p.Nome)
        print("Idade: ", p.Idade)
        print("Gênero: ", p.Genero+ '\033[0;0m')


Pessoa.base('a')

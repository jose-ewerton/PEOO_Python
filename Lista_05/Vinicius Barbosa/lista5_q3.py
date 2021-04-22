'''
Defina os atributos e métodos das seguintes classes:
Pessoa:
'''


class Pessoa:

    def __init__(self, Nome, Idade, Genero, vm, Saude, pm):

        self.Nome = Nome
        self.Idade = Idade
        self.Genero = Genero
        self.vm = vm
        self.pm = pm
        self.Saude = Saude

    def base(self):

        p = Pessoa

        p.nome = input("Nome:")
        p.Idade = int(input("Idade:"))
        p.Genero = input("Gênero:")

        print("Nome:", p.nome)
        print("Idade:", p.Idade)
        print("Gênero:", p.Genero)

    def acoes(self):

        p = Pessoa

        p.vm = input("Está Acordado ou Dormindo:")

        if p.vm == "Acordado" or p.vm == "acordado":
            p.saude = input("Como está a sua saúde:")
            p.pm = input("Está parado ou em movimento:")
            print(f'{p.nome} estar, {p.vm}, com a saúde, {p.saude} e também estar {p.pm}')
        elif p.vm == "Dormindo" or p.vm == "dormindo":
            print(p.nome, "está dormindo")


Pessoa.base("a")
Pessoa.acoes("a")

print('')
print('================================')
print('')
print('By: Vinicius Barbosa')
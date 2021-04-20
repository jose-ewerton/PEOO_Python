class Pessoa:
    def __init__(self, nome, idade, genero, altura):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.altura = altura


    def base(self):
        p = Pessoa

        p.nome = input ("Nome: ")
        p.idade = int (input ("Idade: "))
        p.genero = input ("Gênero: ")
        p.altura = float (input("Altura:"))

        print ("Nome:", p.nome)
        print ("Idade:", p.idade)
        print ("Gênero:", p.genero)
        print ("Altura:", p.altura)




Pessoa.base ("a")  # chamada do método pela classe

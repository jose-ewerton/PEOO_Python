""""Defina os atributos e métodos das seguintes classes:
Animal:
"""


class Animal:
    def __init__(self, raca, nome, idade, peso, sexo, cor,):
        self.raca = raca
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.sexo = sexo
        self.cor = cor

    def entradas(self):
        a = Animal
        a.nome = str(input("Qual é o nome? "))
        a.raca = str(input("Qual é a raça? "))
        a.idade = float(input("Qual é a idade do animal? "))
        a.peso = float(input("Qual é o peso? "))
        a.sexo = str(input("Macho ou Fêmea? "))
        a.cor = str(input("Qual é a cor do animal? "))

        print('\033[7;97m' + f"O nome do animal é: {a.nome}")
        print(f"{a.nome} é um/a {a.raca}")
        print(f"{a.nome} tem {a.idade} anos")
        print(f"{a.nome} tem {a.peso}kg")
        print(f"{a.nome} é {a.cor}" + '\033[0;0m')

Animal.entradas("a")
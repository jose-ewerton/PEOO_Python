class Animal:

    def __init__(self):
        self.Nome = None
        self.Raça = None
        self.Cor = None
        self.Idade = None
        self.Peso = None

    def detalhar_animal(self):
        print(25*"-")
        print("Nome = {0}" .format(self.Nome))
        print("Raça = {0}" .format(self.Raça))
        print("Cor = {0}" .format(self.Cor))
        print("Idade = {0}" .format(self.Idade))
        print("Peso = {0}" .format(self.Peso))
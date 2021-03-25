
class Mamifero:
    def __init__(self,nome,peso):
        self.nome = nome
        self.peso = peso
    
    def alimentacao_filhote(self):
        print ('Leite')

    
class Cachorro(Mamifero):
    def __init__(self,nome,peso):
        super().__init__(nome,peso)
        self.som = "Latir"

    def alimentacao_adulta(self):
        print("Carne")

class Boi(Mamifero):
    def __init__(self,nome,peso):
        super().__init__(nome,peso)
        self.som = "Muuuuu"

    def alimentacao_adulta(self):
        print("Capim")












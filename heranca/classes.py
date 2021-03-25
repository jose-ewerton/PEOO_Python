class Mamifero:
    def __init__(self,nome="Mamifero",peso="0"):
        self.nome = nome
        self.peso = peso
        self.nomeclasse = self.__class__.__name__
    
    def alimentacao_filhote(self):
        print(f"O {self.nome} quando FILHOTE, alimenta-se com Leite")


class Gato(Mamifero):
    def alimentacao_adulta(self):
        print(f"O {self.nome} quando ADULTO, alimenta-se com Carne")  

class Cachorro(Mamifero):
    def __init__(self,nome,peso):           #solução para a sobreescrição do método construtor da classe pai
        super().__init__(nome,peso)         #construtor da classe pai sendo invocado com método super
        self.som = "Latir"

    def alimentacao_adulta(self):
        print(f"O {self.nome} quando ADULTO, alimenta-se com Carne")

class Boi(Mamifero):
    def __init__(self,nome,peso):
        super().__init__(nome,peso)
        self.som = "Mugir"

    def alimentacao_adulta(self):
        print(f"O {self.nome} quando ADULTO, alimenta-se com Capim")












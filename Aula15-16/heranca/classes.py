class Mamifero:

    def __init__(self, nome="Animal",peso = 0):
        self.nome = nome
        self.peso = peso
    def alimentacao_filhote(self):
        print(f"O {self.nome} quando FILHOTE, alimenta-se com Leite")


class Gato(Mamifero): #Gato herda os atributos e métodos da classe manifero (extends), mas não tem construtor
    def alimentacao_adulta(self):
        print(f"O {self.nome} quando ADULTO, alimenta-se com CARNE")


class Cachorro(Mamifero):
    def __init__(self,nome,peso):
        super().__init__(nome,peso)
        self.som = "Latir"
    
    def alimentacao_adulta(self):
        print(f"O {self.nome} quando ADULTO, alimenta-se com CARNE")
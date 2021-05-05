class Animal:
    def __init__(self, especie, nome, idade, cor, peso):
        self.especie = especie
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.peso = peso

    def mostrar_animal(self):
        print(f'{self.especie}:\nNome:{self.nome}\nIdade: {self.idade} ano(s)\nCor: {self.cor}\nPeso: {self.peso}kg')

    def comer(self):
        print(f"{self.nome} está comendo")

    def andar(self):
        print(f"{self.nome} está andando")

    def dar_a_pata(self):
        print(f"{self.nome} está dando a patinha")


if __name__ == "__main__":
    A1 = Animal ('Gato', 'Bartolomeu', 1, 'Branco','10')
    A1.mostrar_animal()
    A1.comer()
    A1.andar()
    A1.dar_a_pata()
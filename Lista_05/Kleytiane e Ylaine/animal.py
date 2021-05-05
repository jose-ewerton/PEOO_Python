class Animal:
    
    def __init__(self, especie, porte, cor):
        self.especie = especie
        self.porte = porte
        self.cor = cor

    def base(self):
        a = Animal

        a.especie = input("Digite a especie desse animal:")
        a.porte = input("Digite o porte desse animal:")
        a.cor = input("Digite a cor desse animal:")

        print("Espécie:",a.especie)
        print("Porte:",a.porte)
        print("cor:",a.cor)

    def andar(self):
        print("O animal esta andando!")

    def cacar(self):
        print('O animal esta caçando')

if (__name__ == "__main__"):
        am = Animal("Gato","Pequeno","Branco")
        am.andar()
        am.cacar()
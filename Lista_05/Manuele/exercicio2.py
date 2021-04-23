
#atributos e métodos para a classe ANIMAL.
class Animal():
    def __init__ (self, tipo, especie, cor ):
        self.tipo = tipo
        self.especie = especie
        self.cor = cor
    

    def detalhar_animal(self):
        print("Tipo: {0}".format(self.tipo))
        print("Espécie: {0}".format(self.especie))
        print("Gênero: {0}".format(self.cor))



a = Animal ( "Mamifero","Cachorro", "Albino" )
a.detalhar_animal()
class Animal():
    tipo = None
    especie = None
    genero = None

    def detalhar_animal(self):
        print("Tipo: {0}".format(self.tipo))
        print("Espécie: {0}".format(self.especie))
        print("Gênero: {0}".format(self.genero))



from animal import Animal
a = Animal()
a.tipo = "Cavala"
a.genero = "Arco-iro"
a.especie = "Lupus"

a.detalhar_animal()
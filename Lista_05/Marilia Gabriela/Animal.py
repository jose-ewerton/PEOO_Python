class Animal:
    def __init__(self, especie, tipo):
        self.especie = especie
        self.tipo = tipo

    def informacoes(self):
        print("Especie: {} \nTipo: {}".format(self.especie, self.tipo))

    def comendo(self):
        print("O animal está comendo")

    def dormindo(self):
        print("O animal está dormindo")


while True:
        especie = input('Qual a espécie do animal?')
        tipo = input("O animal é doméstico ou selvagem?")
        animal = Animal(especie, tipo)
        dormindo = str(input("O animal está dormindo?(sim ou não)")).upper()
        if dormindo == "SIM":
            animal.informacoes()
            animal.dormindo()
        else:
            comendo = str(input("O animal está comendo?(sim ou não)")).upper()
            if comendo == "SIM":
                animal.informacoes()
                animal.comendo()
            else:
                animal.informacoes()
        break
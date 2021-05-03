class Animal:
    def __init__ (self,__animal,nome,__raca,cor,peso,habitat):
        self.__animal = __animal
        self.nome = nome
        self.__raca = __raca
        self.cor = cor
        self.peso = peso
        self.habitat = habitat
        self.estado = None

    def detalhar_animal(self):
        print(f"Espécie: {self.__animal}\nNome: {self.nome}\nRaça: {self.__raca}\nCor: {self.cor}\nPeso: {self.peso}\nHabitat: {self.habitat}")

    def correr(self):
        print(f"{self.nome} está correndo")
        self.estado = "correndo"
    
    def comer(self):
        print(f"{self.nome} está comendo")
        self.estado = "comendo"

    def procurar_alimento(self):
        print(f"{self.nome} está procurando alimento")
        self.estado = "procurando alimento"
    
    def dormir(self):
        print(f"{self.nome} está dormindo")
        self.estado = "dormindo"

    def acordar(self):
        print(f"{self.nome} está acordado")
        self.estado = "acordado"

    def aumentar_peso(self,x):
        print(f"{self.nome} engordou {x}kg")
        self.peso += x

    def diminuir_peso(self,x):
        print(f"{self.nome} emagreceu {x}kg")
        self.peso -= x
    
    def alterar_habitat(self,novoHabitat):
        nH = str(novoHabitat)
        self.habitat = nH
        print(f"O animal {self.nome} se mudou para {self.habitat}")

if __name__ == "__main__":
    a1 = Animal("Cachorro","Ralf","Vira lata","Cinza",5,"Quintal")
    a1.detalhar_animal()
    a1.dormir()
    a1.acordar()
    a1.procurar_alimento()
    a1.comer()
    a1.aumentar_peso(1)
    a1.alterar_habitat("casa")

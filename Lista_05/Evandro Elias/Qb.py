class Animal:
    def __init__(self, t, sexo, peso, higine):
        self.t = t
        self.sexo = sexo
        self.peso = peso
        self.higiene = higiene
    def perguntas(self):
        a = Animal
        a.t = str(input("Qual  é o animal? "))
        a.sexo = str(input("Qual o sexo do animal?  "))
        a.peso = str(input("qual o peso do animal?  "))
        print(f"especie:{a.t}")
        print(f"sexo:{a.sexo}")
        print(f"peso:{a.peso}")
    def atributos(self):
        a = Animal
        a.higiene = int(input("como está a higiene do animal?: 1== Ruim  2 == Boa"))
        if a.higiene == 1:
            print("Dê um banho no animal.")
        if a.higiene == 2:
            print("Continue cuidando dele.")
        if a.higiene >> 2:
            print("muito bom")
Animal.perguntas("e")
Animal.atributos("e")


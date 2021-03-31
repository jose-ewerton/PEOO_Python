'''Defina os atributos e métodos das seguintes classes:
Animal:'''
class animal:
    def __init__(self, especie, sexo, peso, altura, saude):
        self.especie = especie 
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
    def base(self):
        a = animal
        a.especie = str(input("qual a especie do animal?: "))
        a.sexo = str(input("qual o sexo do animal?: "))
        a.peso = str(input("qual o peso do animal?: "))
        a.altura = str(input("qual a altura do animal?: "))
        print("especie:",a.especie)
        print("sexo: ",a.sexo)
        print("peso: ",a.peso)
        print("altura:",a.altura)
    def situação(self):
        a = animal
        a.saude = float(input("em uma escala de 0 a 10, como está a saude do animal?: "))
        if a.saude <= 0:
            print("o animal morreu.")
        elif a.saude <= 3 and a.saude >= 1:
            print("o animal está muito doente.")
        elif a.saude >= 4 and a.saude <= 6:
            print ("tome cuidado com o animal, ele pode piorar.")
        elif a.saude >= 7 and a.saude <= 9:
            print("o animal está saudavel.")
        else:
            print("o animal esta em.um estado otimo.")
animal.base("e")
animal.extra("e")
class Animal:
    def __init__(self, especie, sexo, peso, altura, saude):
        self.especie = especie 
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
    def inputs(self):
        a = Animal
        a.especie = str(input("qual a especie do animal?: "))
        a.sexo = str(input("qual o sexo do animal?: "))
        a.peso = str(input("qual o peso do animal?: "))
        a.altura = str(input("qual a altura do animal?: "))
        print(f"especie:{a.especie}")
        print(f"sexo:{a.sexo}")
        print(f"peso:{a.peso}")
        print(f"altura:{a.altura}")
    def situação(self):
        a = Animal
        a.saude = float(input("em uma escala de 0 a 10, como está a saude do animal?: "))
        if a.saude <= 0:
            print("o animal esta morto")
        elif a.saude <= 3 and a.saude >= 1:
            print("o animal está muito doente leve-o a um veterinario")
        elif a.saude >= 4 and a.saude <= 6:
            print ("tome cuidado com o animal, pode ser que o estado dele se agrave")
        elif a.saude >= 7 and a.saude <= 9:
            print("o animal está saudavel, porém mantenha-o sob observação")
        else:
            print("o animal esta perfeitamente saudavel nao ha com o que se preocupar")
Animal.inputs("e")
Animal.situação("e")

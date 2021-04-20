class animal:
    def __init__(self, nome, especie, sexo, peso, altura, tamanho):
        self.nome = nome
        self.especie = especie
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.tamanho = tamanho
    def base(self):
        a = animal
        a.nome = str(input("Qual o nome do animal?: "))
        a.especie = str(input("qual a especie do animal?: "))
        a.sexo = str(input("qual o sexo do animal?: "))
        a.peso = str(input("qual o peso do animal?: "))
        a.altura = str(input("qual a altura do animal?: "))
        
        print("nome:",a.nome)
        print("especie:",a.especie)
        print("sexo: ",a.sexo)
        print("peso: ",a.peso)
        print("altura:",a.altura)

animal.base("e")
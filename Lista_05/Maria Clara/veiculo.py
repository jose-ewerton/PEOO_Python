  
class carro:
    def __init__(self, Marca, Modelo, Ano):
        self.marca = Marca
        self.modelo = Modelo
        self.ano = Ano

    def base(self):
        a = carro

        a.marca = input ("Digite a marca do carro: ")
        a.modelo = input ("Digite o modelo do carro: ")
        a.ano = input ("Digite o ano do carro: ")

        print ('\033[7;97m' + "Marca:", a.marca)
        print ("Modelo:", a.modelo)
        print ("Ano:", a.ano + '\033[0;0m')

carro.base(1)
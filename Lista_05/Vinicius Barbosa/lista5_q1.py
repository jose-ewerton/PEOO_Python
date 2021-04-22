'''
Defina os atributos e métodos das seguintes classes:

Veículos:
'''


class Carro:

    def __init__(self, Marca, Modelo, Ano, Estado, Km_rodados):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Ano = Ano
        self.Estado = Estado
        self.Km.rodados = Km_rodados

    def Base(self):
        c = Carro

        c.Marca = input("Digite a marca do carro:")
        c.Modelo = input("Digite o modo do carro:")
        c.Ano = input("Digite o ano do carro:")

        print('\033[7;96m' + "Marca:", c.Marca)
        print("Modelo:", c.Modelo)
        print("Ano:", c.Ano + '\033[0;0m')

    def Extra(self):
        c = Carro

        c.Estado = input("Digite o estado atual do carro:")
        c.Km_rodados = input("Digite quantos km possui o carro atualmente:")

        print('\033[7;96m' + "O modelo", c.Modelo, ", da marca", c.Marca, "está com estado", c.Estado, "e com",
              c.Km_rodados, "km rodados." + '\033[0;0m')


Carro.Base(1)
Carro.Extra(1)

print('')
print('====================================================================')
print('')
print('By: Vinicius Barbosa')
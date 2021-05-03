class Veículos:
    def __init__(self, tipo, marca, cor):
        self.tipo = tipo
        self.marca = marca
        self.cor = cor

    def info(self):
        print("Tipo: {}".format(tipo))
        print("Marca: {}".format(marca))
        print("Cor: {}".format(cor))

    def ligar(self):
        print("O veículo está ligado!")

    def desligar(self):
        print("O veículo está desligado!")


while True:
    tipo = input("qual o tipo do veículo:")
    marca = input("qual a marca do veículo:")
    cor = input("qual a cor do veículo:")
    veiculos = Veículos(tipo, marca, cor)
    carro = str(input('O seu veículo está Ligado?(Sim ou Não):')).upper()
    if carro == 'SIM':
        veiculos.info()
        veiculos.ligar()
    else:
        veiculos.info()
        veiculos.desligar()
    break
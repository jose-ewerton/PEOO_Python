class Veículos:
    def __init__(self, tipo, marca, ano, cor):
        self.tipo = tipo
        self.marca = marca
        self.ano = ano
        self.cor = cor

    def Acelerar(self):
        print("O veículo está em movimento!")

    def parar(self):
        print("O veículo está parado!")

    def ligar(self):
        print("O veículo está ligado!")

    def desligar(self):
        print("O veículo está deligado!")

    def info(self):
        print("Informações sobre o Veículo:")
        print(f"Tipo: {self.tipo}\nMarca: {self.marca}\nAno: {self.ano}\nCor: {self.cor}")


while True:
    tipo = input("Digite o tipo do veículo:")
    marca = input("Digite a marca do veículo:")
    ano = int(input("Digite o ano de fabricação do veículo:"))
    cor = input("Digite a cor do veículo:")
    veiculos = Veículos(tipo, marca, ano, cor)
    carro = str(input('O seu veículo está Ligado?(S ou N):')).upper()
    if carro == 'S':
        movimento = str(input('O seu veículo está Parado ou Movimento?')).upper()
        if movimento == 'PARADO':
            veiculos.info()
            veiculos.ligar()
            veiculos.parar()
        elif movimento == 'MOVIMENTO':
            veiculos.info()
            veiculos.ligar()
            veiculos.Acelerar()
    elif carro == 'N':
        veiculos.info()
        veiculos.desligar()
    break
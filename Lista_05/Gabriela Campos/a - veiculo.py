class Veículos:
    def __init__(self, tipo, marca, ano, cor):
        self.tipo = tipo
        self.marca = marca
        self.ano = ano
        self.cor = cor

    def acelerar(self):
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
    tipo = input("Digite o tipo de veículo: ")
    marca = input("a marca do veículo: ")
    ano = int(input("o ano de fabricação do veículo: "))
    cor = input("a cor do veículo: ")
    veiculos = Veículos(tipo, marca, ano, cor)
    carro = str(input('O veículo está Ligado?(SIM ou NÃO): ')).upper()
    if carro == 'SIM':
        movimento = str(input('O veículo está Parado ou Movimento? ')).upper()
        if movimento == 'PARADO':
            veiculos.info()
            veiculos.ligar()
            veiculos.parar()
        elif movimento == 'MOVIMENTO':
            veiculos.info()
            veiculos.ligar()
            veiculos.acelerar()
    elif carro == 'NÃO':
        veiculos.info()
        veiculos.desligar()
    break

class Veiculo:
    def __init__(self, cor,marca,Km_Rodados,placa):
        self.cor= cor
        self.marca= marca
        self.Km_Rodados= Km_Rodados
        self.placa = placa

    def Imprimir_Especs (self):
        print("A cor do seu veículo é", self.cor)
        print("A marca do seu veícuo é", self.marca)
        print("Seu veículo já rodou", self.Km_Rodados,"KM")
        print("A placa do seu veículo é:",self.placa)

    def Mudar_de_Cor (self):
        X= input("Digite sua nova cor:")
        self.cor=(X)
        print("A nova cor do seu carro é", X)

    def Mudar_Placa (self):
        Y=input("Qual sua nova placa?")
        self.placa=(Y)
        print("A placa do seu veículo agora é", Y, "Anota aí!!!!")

carro1 = Veiculo("Azul", "Honda", 20000,1234)

carro1.Imprimir_Especs()

carro1.Mudar_de_Cor()

carro1.Imprimir_Especs()

carro1.Mudar_Placa()

carro1.Imprimir_Especs()
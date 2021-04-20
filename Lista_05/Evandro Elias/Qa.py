class Veiculo:
    def __init__(self,Marca,Modelo,Ano,Estado):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Ano = Ano
        self.Estado = Estado
    def basico(self):
        v = Veiculo
        v.Marca = str(input("Marca do carro:"))
        v.Modelo = str(input("Modelo do carro:"))
        v.Ano = str(input("Ano do carro:"))
        v.Estado = str(input("Estado do carro:"))
        print(f"Marca:{v.Marca}")
        print(f"Modelo:{v.Modelo}")
        print(f"Ano:{ v.Ano}")
        print(f"Estado do carro:{v.Estado}")
    def k(self):
        v = Veiculo
        v.km = float(input("Quantos km o carro rodou?:"))
        if v.km >= 100.000:
            print("Rodado")
        if v.km <= 99.999:
            print("Bem novin vum")
Veiculo.basico(1)
Veiculo.k(1)

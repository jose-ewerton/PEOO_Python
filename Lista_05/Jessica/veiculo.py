class Veiculo:
    def __init__(self, tipo, marca, cor, ano):
        self.tipo = tipo
        self.marca = marca
        self.cor = cor
        self.ano = ano

    def mostrar_veiculo(self):
        print (f'O tipo: {self.tipo}\nA marca: {self.marca}\nA cor: {self.cor}\nO ano: {self.ano}')

    def locomover (self):
        print(f'o {self.tipo} está se locomovendo!')

    def parar(self):
        print(f'o {self.tipo} está parado!')






if __name__ == '__main__':
    carro = Veiculo('carro', 'penelopi', 'rosa', 2344)
    carro.mostrar_veiculo()
    carro.locomover()
    carro.parar()
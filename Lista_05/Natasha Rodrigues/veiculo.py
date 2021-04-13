print('Classe:')
print('Veículo')
print('-'*12)       
class Veiculo:
    def __init__(self, tipo, modelo, marca):
        self.tipo = tipo
        self.modelo = modelo
        self.marca = marca
        print('-'*12)
        print('Atributos:')
        print(self.tipo)
        print(self.modelo)
        print(self.marca)
        print('-'*12)
        print('Métodos:')

    def parar(self):
        print(f'O {self.tipo} esta parado.')

    def acelerar(self):
        print(f'O {self.tipo} esta acelerando.')

if __name__ == "__main__":
        tipo = input("Informe o tipo de veiculo: ")
        modelo = input("Informe o modelo do veiculo: ")
        marca = input("Informe a marca do veiculo: ")
        v1 = Veiculo(tipo, modelo, marca)
        parado = input("O {} esta parado, sim ou não? ".format(tipo)).upper()
        if parado == "SIM":
            v1.parar()
        elif parado == "NÃO":
            acelera = input("O {} esta acelerando, sim ou não?".format(tipo)).upper()
            if acelera == "SIM":
                v1.acelerar()
            
        
        


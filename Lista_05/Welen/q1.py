class Veiculo:
    def __init__(self): #atributos
        self.cor = None
        self.marca = None
        self.altura = None

    def ligar(self): #métodos ou ações que a classe executa
        print("O carro está ligado!")

    def ré(self): #métodos ou ações que a classe executa
        print("O carro está dando ré!")
if (__name__ == "__main__"): # isso serve para testar a classe
    v = Veiculo()
    v.cor = "Vermelho"
    v.marca = "Punto"
    v.altura = "1499 mm"
    print(v.cor, v.marca, v.altura)
    v.ligar()
    v.ré()
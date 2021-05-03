class Veiculo:
    def __init__(self): #atributos
        self.cor = None
        self.marca = None
        self.quantidade_rodas = None

    def ligar(self): #métodos ou ações que a classe executa
        print("O carro está ligado!")

    def acelerar(self): #métodos ou ações que a classe executa
        print("O carro está acelerado!")

if (__name__ == "__main__"): # isso serve para testar a classe
    v = Veiculo()
    v.cor = "Preto"
    v.marca = "Gol"
    v.quantidade_rodas = "4"
    print(v.cor,v.marca,v.quantidade_rodas)
    v.ligar()
    v.acelerar()
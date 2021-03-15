class Veiculo:
    def __init__(self, tipo, marca, preco, cor, estado, portas, combustivel):
        self.tipo = tipo
        self.marca = marca
        self.preco = preco
        self.cor = cor
        self.estado = estado
        self.portas = portas
    def inputs(self):
        v = Veiculo
        v.tipo = str(input("qual o tipo do veiculo?: "))
        v.marca = str(input("qual a marca do veiculo?: "))
        v.preco = float(input("qual o preco do veiculo?: "))
        v.cor = str(input("qual a cor do veiculo?: "))
        v.estado = str(input("qual o estado do veiculo?: "))
        v.portas = int(input("quantas portas o veiculo tem?: "))
        print(f"o veiculo e um {v.tipo}")
        print(f"sua marca e {v.marca}")
        print(f"o veiculo custa {v.preco}")
        print(f"sua cor e {v.cor}")
        print(f"o veiculo esta em {v.estado} estado")
        print(f"o veiculo tem {v.portas} portas")
    def modulos(self):
        v = Veiculo
        v.combustivel = float(input("quao cheio esta o tanque numa escala de 0 a 10?: "))
        if v.combustivel <= 0:
            print("encha o tanque")
        if v.combustivel <= 3 and v.combustivel >= 1:
            print("o tanque esta com pouco combustivel encha-o")
        if v.combustivel <= 6 and v.combustivel >= 4:
            print("o tanque esta com aproximadamente metade de combustivel recomendo enche-lo")
        if v.combustivel <= 9 and v.combustivel >= 7:
            print("o tanque esta praticamente cheio não ha necessidade de abastecer")
        else:
            print("o tanque esta cheio, boa viagem")
Veiculo.inputs("a")
Veiculo.modulos("a")

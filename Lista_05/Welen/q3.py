class Pessoa:
    def __init__(self): #atributos
        self.nome = None
        self.altura = None
        self.cor_dos_cabelos = None

    def conversar(self): #métodos ou ações que a classe executa
        print("A pessoa está conversando")

    def felicidade(self): #métodos ou ações que a classe executa
        print("A pessoa está muito feliz")
if (__name__ == "__main__"): # isso serve para testar a classe
    v = Pessoa()
    v.nome = "Wellen"
    v.altura = "1.55m"
    v.cor_dos_cabelos = "cabelos castanho"
    print(v.nome, v.altura, v.cor_dos_cabelos)
    v.conversar()
    v.felicidade()
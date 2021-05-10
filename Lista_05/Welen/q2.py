class Animal:
    def __init__(self): #atributos
        self.cor = None
        self.raça = None
        self.peso = None

    def latir(self): #métodos ou ações que a classe executa
        print("O cachorro está latindo!")

    def correr(self): #métodos ou ações que a classe executa
        print("O cachorro está correndo!")
if (__name__ == "__main__"): # isso serve para testar a classe
    v = Animal()
    v.cor = "Preto"
    v.raça = "Pitbull"
    v.peso = "35kg"
    print(v.cor, v.raça, v.peso)
    v.latir()
    v.correr()
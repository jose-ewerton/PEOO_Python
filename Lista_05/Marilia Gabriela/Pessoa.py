class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def info(self):
        print("Nome: {}".format(self.nome))
        print("Idade: {}".format(self.idade))
        print("Altura: {}".format(self.altura))

    def dormir(self):
        print("a pessoa está dormindo.")

    def comer(self):
        print("a pessoa está comendo.")

    def andar(self):
        print("a pessoa está andando.")

        
while True:
    nome = input("Qual seu nome: ")
    idade = int(input("Qual sua idade: "))
    altura = float(input("Qual sua altura: "))
    dormir = input("quer dormir(Sim ou Não)? ").upper()
    pessoa = Pessoa(nome, idade, altura)

    if dormir == "SIM":
        pessoa.info()
        pessoa.dormir()
    else:
        comer = input("quer comer?(Sim ou Não)? ").upper()
        if comer == "SIM":
            pessoa.info()
            pessoa.comer()
        else:
            andar = input("quer andar(Sim ou Não)? ").upper()
            if andar == "SIM":
                pessoa.info()
                pessoa.andar()
            else:
                pessoa.info()
    break
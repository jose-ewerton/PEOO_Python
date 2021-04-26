class Pessoa:
    def __init__(self, nome, genero, idade, altura):
        self.nome = nome
        self.genero = genero
        self.idade = idade
        self.altura = altura

    def dormir(self):
        print(f"{nome} está Dormindo.")

    def acordar(self):
        print(f"{nome} está Acordada.")

    def comer(self):
        print(f"{nome} está Comendo.")

    def caminhar(self):
        print(f"{nome} está Caminhando.")

    def info(self):
        print("Nome: {} \nGenêro: {} \nIdade: {} \nAltura: {}".format(self.nome, self.genero, self.idade, self.altura))


while True:
    print('='*20)
    nome = input("Digite seu nome: ")
    idade = int(input("sua idade: "))
    gerero = input("seu genêro: ")
    altura = float(input("sua altura: "))
    dormir = input("Deseja dormir(SIM ou NÃO)? ").upper()
    pessoa = Pessoa(nome, gerero, idade, altura)

    if dormir == "SIM":
        pessoa.info()
        pessoa.dormir()
    elif dormir == "NÃO":
        alimentar = input("Deseja comer?(SIM ou NÃO)? ").upper()
        if alimentar == "NÃO":
            caminhar = input("Deseja caminhar(SIM ou NÃO)? ").upper()
            if caminhar == "SIM":
                print('=' * 20)
                pessoa.info()
                pessoa.acordar()
                pessoa.caminhar()
            elif caminhar == 'NÃO':
                print('=' * 20)
                pessoa.info()
                pessoa.acordar()

        elif alimentar == "SIM":
            print('=' * 20)
            pessoa.info()
            pessoa.acordar()
            pessoa.comer()
    break

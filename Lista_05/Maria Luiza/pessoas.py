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
    idade = int(input("Digite sua idade: "))
    gerero = input("Digite seu genêro: ")
    altura = float(input("Digite sua altura: "))
    dormir = input("Deseja dormir(S ou N)? ").upper()
    pessoa = Pessoa(nome, gerero, idade, altura)

    if dormir == "S":
        pessoa.info()
        pessoa.dormir()
    elif dormir == "N":
        alimentar = input("Deseja comer?(S ou N)? ").upper()
        if alimentar == "N":
            caminhar = input("Deseja caminhar(S ou N)? ").upper()
            if caminhar == "S":
                print('=' * 20)
                pessoa.info()
                pessoa.acordar()
                pessoa.caminhar()
            elif caminhar == 'N':
                print('=' * 20)
                pessoa.info()
                pessoa.acordar()

        elif alimentar == "S":
            print('=' * 20)
            pessoa.info()
            pessoa.acordar()
            pessoa.comer()
    break
class Pessoa:
    def __init__(self, nome, idade, sexo, altura, peso):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        self.peso = peso

    def mostrar_pessoa (self):
        print(f'{self.nome}\nidade: {self.idade}\nsexo: {self.sexo}\naltura: {self.altura}\npeso: {self.peso}')

    def andar(self):
        print(f"{self.nome} está andando")

    def comer(self):
        print(f"{self.nome} está comendo")

    def falar(self):
        print(f"{self.nome} está falando")


if __name__ == '__main__':
    p1 = Pessoa('Jessica Natalia', 18, 'feminino', 1.60, 60)
    p1.mostrar_pessoa()
    p1.andar()
    p1.comer()
    p1.falar()
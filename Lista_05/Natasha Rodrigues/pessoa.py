print('-'*12)
print('Classe:')
print('Pessoa')
print('-'*12)       
class Pessoa:
    def __init__(self, nome, idade, cor_da_pele, cidade_nasceu):
        print('Dados:')
        self.nome = nome
        self.idade = idade
        self.cor_da_pele = cor_da_pele
        self.cidade_nasceu = cidade_nasceu
        print('-'*12)
        print('Atributos:')
        print(self.nome)
        print(self.idade)
        print(self.cor_da_pele)
        print(self.cidade_nasceu)
        print('-'*12)
        print('Métodos:')

    def falar(self):
        print(f'{self.nome} esta falando.')

    def andar(self):
        print(f'{self.nome} esta andando.')

    def parar_andar(self):
        print(f'{self.nome} parou de andar.')

    def continua(self):
        print(f'{self.nome} continua andando.')

    def nao(self):
        print(f'{self.nome} não esta andando.')

    def ouvir(self):
        print(f'{self.nome} esta ouvindo.')

if __name__=="__main__":
    nome = input("Informe o seu nome: ")
    idade = int(input("{} informe sua idade: ".format(nome)))
    cor_da_pele = input("{} informe a cor da sua pele: ".format(nome))
    cidade_nasceu = input("{} informe a cidade em que você nasceu: ".format(nome))
    p1 = Pessoa(nome, idade, cor_da_pele, cidade_nasceu)
    anda = input("Você esta andando, sim ou não? ").upper()
    if anda == "SIM":
        p1.andar()
        para_anda = input("Deseja parar de andar, sim ou não?").upper()
        if para_anda == "SIM":
            p1.parar_andar()
        elif para_anda == "NÃO":
            p1.continua()
    elif anda == "NÃO":
        p1.nao()
    fala_ouve = input("Você esta falando ou ouvindo?").upper()
    if fala_ouve == "FALANDO":
        p1.falar()
    elif fala_ouve == "OUVINDO":
        p1.ouvir()
    


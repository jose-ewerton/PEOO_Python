#atributos e métodos para  classe Pessoa.
class Pessoa:
    def __init__(self, nome, idade, endereco, cpf):
        self.nome = nome
        self.idade = idade
        self.endereço = endereco
        self.cpf = cpf
 

    def detalhar_pessoa(self):
        print("Nome: {0}".format(self.nome))
        print("Idade: {0}".format(self.idade))
        print("Endereço: {0}".format(self.endereço))
        print("CPF: {0}".format(self.cpf))

p = Pessoa ("Manullene","20"," Ceara-mirim","000.000.000-00" )
p.detalhar_pessoa()


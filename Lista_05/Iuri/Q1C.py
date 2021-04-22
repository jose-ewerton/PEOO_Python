class Pessoa:
    nome = None
    idade = None
    endereço = None
    cpf = None

    def detalhar_pessoa(self):
        print("Nome: {0}".format(self.nome))
        print("Idade: {0}".format(self.idade))
        print("Endereço: {0}".format(self.endereço))
        print("CPF: {0}".format(self.cpf))



from pessoa import Pessoa
p = Pessoa()
p.nome = "Alfredo"
p.idade = 54
p.endereço = "Santa agueda, n° 181°, Ceará-mirim\RN"
p.cpf = 000.000-00
p.detalhar_pessoa()
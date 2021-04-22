class Pessoa:
    nome = None
    idade = None
    endereco = None
    cpf = None

    def detalhar_pessoa(self):
        print("Nome: {0}".format(self.nome))
        print("Idade: {0}".format(self.idade))
        print("Endereço: {0}".format(self.endereco))
        print("CPF: {0}".format(self.cpf))
class Pessoa:

    def __init__(self):
        self.Nome = None
        self.Idade = None
        self.Email = None
        self.Cpf = None

    def detalhar_pessoa(self):
        print(25*"-")
        print("Nome = {0}." .format(self.Nome))
        print("Idade = {0}." .format(self.Idade))
        print("Email = {0}." .format(self.Email))
        print("Cpf = {0}." .format(self.Cpf))

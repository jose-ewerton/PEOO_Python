class pessoa:
    def __init__(self, nome, idade, CPF, endereço,):
        self.nome = nome
        self.idade = idade
        self.cpf = CPF
        self.endereco = endereço

    def dados(self):
        a = pessoa
        a.nome = str(input("Nome: "))
        a.cpf = str(input("CPF do cliente: "))
        a.idade = str(input("Idade: "))
        a.endereco = str(input("Endereço: "))
        
        print("_"*30)
        print("nome: ",a.nome)
        print("CPF do cliente: ",a.cpf)
        print("Idade: ",a.idade)
        print("Endereço: ",a.endereco)
        print("_"*30)

pessoa.dados("1")
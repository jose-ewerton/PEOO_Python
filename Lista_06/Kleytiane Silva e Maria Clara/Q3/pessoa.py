class Pessoa:
    def __init__(self, nome, cpf, identidade):
        self.__nome = nome
        self.__cpf = cpf
        self.__identidade = identidade 
        self.__lista_endereco = []

    def adc_endereco(self, endereco):
        self.__lista_endereco.append (endereco)

    def listar(self):
        print("Nome:", self.__nome, "CPF:", self.__cpf, "RG:", self.__identidade)
        print("~~~~~~~~~~Endereços~~~~~~~~~~")
        for endereco in self.__lista_endereco:
            
            print("número de residencia:", endereco._num_casa)
            print("Rua:", endereco.__rua)
            print("Cidade:", endereco._cidade)
            print("Estado:", endereco._estado)
            print("País:", endereco._pais)
class pessoa:
    def __init__(self ,nome, cpf, identidade):
        self.__nome = nome
        self.__cpf = cpf
        self.__identidade = identidade
        self.__lista_endereco =  []    

    def adc(self, endereco):
        self.__lista_endereco.append(endereco)

    def listar(self):
        print(" Pessoa:") 
        print("Nome:", self.__nome.format(self.__nome,))
        print("CPF:",self.__cpf.format(self.__cpf,))
        print("RG:", self.__identidade .format(self.__identidade))    
        print("Endereços:")
        for endereco in self.__lista_endereco:
            print("Rua:", endereco ._rua)
            print("Número de residencia:", endereco._num_casa)
            print("Cidade:", endereco._cidade)
            print("Estado:", endereco._estado)
            print("País:", endereco._pais) 
            
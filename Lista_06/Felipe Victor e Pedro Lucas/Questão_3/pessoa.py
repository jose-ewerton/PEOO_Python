class Pessoa:
    def __init__(self, nome, cpf, registro_geral):
        self.__nome = nome
        self.__cpf = cpf
        self.__registro_geral = registro_geral
        self.__lista_endereco = []

    def adc_endereco(self, endereco):
        self.__lista_endereco.append (endereco)

    def listar(self):
        print("Nome:", self.__nome, "CPF:", self.__cpf, "RG:", self.__registro_geral)
        print("~~~~~~~~~~Endereços~~~~~~~~~~")
        for endereco in self.__lista_endereco:
            print("Rua:", endereco._rua)
            print("Numero da residencia:", endereco._num_casa)
            print("Cidade:", endereco._cidade)
            print("Estado:", endereco._estado)
            print("País:", endereco._pais)
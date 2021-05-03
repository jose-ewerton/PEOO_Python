class Revista:
    def __init__(self, __codigo, __titulo, __tipo):
        self.__codigo = __codigo
        self.__titulo = __titulo
        self.__tipo = __tipo
        self.__edicao = []

    def adicionar_edicao(self, numero_da_edicao, data, numero_do_artigo):
        self.__edicao.append(Edicao(numero_da_edicao, data, numero_do_artigo))  

    def apresentar(self):
        print(f"Revista:\nCodigo: {self.__codigo}\nTitulo: {self.__titulo}\nTipo: {self.__tipo}\n")
          
        print("As edições:")
        n = 1
        for edicao in self.__edicao:
            print(f"{n}º Edição:")
            edicao.exibir()
            n += 1

class Edicao:
    def __init__(self, __numero_da_edicao, __data, __numero_do_artigo):
        self.__numero_da_edicao = __numero_da_edicao
        self.__data = __data
        self.__numero_do_artigo = __numero_do_artigo

    def exibir(self):
        print(f"Numero da edicao: {self.__numero_da_edicao}\nData: {self.__data}\nNumero do artigo: {self.__numero_do_artigo}\n")
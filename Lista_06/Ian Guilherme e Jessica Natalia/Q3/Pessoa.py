class Pessoa:
    def __init__(self, __identificador, __nome, __cpf):
        self.__identificador = __identificador
        self.__nome = __nome
        self.__cpf = __cpf
        self.endereco = []

    def adicionar_endereco(self, endereco):
        self.endereco.append(endereco)

    def remover_local(self, numero_do_local):
        l = 0
        n = 0
        for i in self.endereco:
            if i.numero_da_casa == numero_do_local:
                del self.endereco[n]
                l = 1
            else:
                n += 1    

        if l == 0:
            print("Verifique o número do local\n")
        else:
            print(f"O local com o número da casa {numero_do_local} foi apagado com sucesso\n")            

    def apresentar(self):
        print(f"Dados sobre {self.__nome}:")
        print(f"Identificador: {self.__identificador}\nNome: {self.__nome}\nCpf: {self.__cpf}\n")

        print("Os endereços em seu nome: ")
        n = 1
        for i in self.endereco:
            print(f'{n}º endereço: ')
            i.exibir()        
            n += 1

class Endereco:
    def __init__(self,numero_da_casa, rua, cidade, estado, pais):
        self.numero_da_casa = numero_da_casa
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.pais = pais

    def exibir(self):
        print(f"Numero da casa: {self.numero_da_casa}\nRua: {self.rua}\nCidade: {self.cidade}\nEstado: {self.estado}\nPais: {self.pais}\n")
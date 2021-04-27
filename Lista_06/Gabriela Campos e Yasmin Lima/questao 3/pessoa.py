class Endereco:
    def __init__(self,numero_da_casa:int, rua:str, cidade:str, estado:str, pais:str):
        self.numero_da_casa=numero_da_casa
        self.rua=rua
        self.cidade=cidade
        self.estado=estado
        self.pais=pais

    def exibir(self):
        print(" Dados sobre o local:")
        print(" Numero da casa: {} \n Rua: {} \n Cidade: {} \n Estado: {} \n Pais: {}".format(self.numero_da_casa, self.rua, self.cidade, self.estado, self.pais))


class Pessoa:
    def __init__(self,identificador, nome:str, cpf:int):
        self.__identificador=identificador
        self.__nome=nome
        self.__cpf=cpf
        self.endereco=[]

    def adicionar_endereco(self,endereco):
        self.endereco.append(endereco)

    def remover_local(self,numero_do_local):
        verificar=0
        c=0
        for lugar in self.endereco:
            if lugar.numero_da_casa==numero_do_local:
                del self.endereco[c]
                verificar=1
            c+=1    

        if verificar==0:
            print("Erro")

        elif verificar==1:
            print("Local apagado")            


    def apresentar(self):
        print(" Dados sobre {}".format(self.__nome))
        print(" Identificador: {}, \n Nome: {} \n cpf: {} ".format(self.__identificador,self.__nome, self.__cpf))
        print(" Seus enderecos: ")
        c=1
        for local in self.endereco:
            print(" ")
            print("",c)
            local.exibir()        
            c+=1

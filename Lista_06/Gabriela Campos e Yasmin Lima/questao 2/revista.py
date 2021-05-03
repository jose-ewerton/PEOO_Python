class Edicao:
    def __init__(self,numero_da_edicao:int, data:str,numero_do_artigo:int):
        self.__numero_da_edicao=numero_da_edicao
        self.__data=data
        self.__numero_do_artigo=numero_do_artigo

    def exibir(self):
        print("Dados")
        print("Numero da edicao: {} \n Data: {} \n Numero do artigo: {}".format(self.__numero_da_edicao,self.__data, self.__numero_do_artigo))


class Revista:
    def __init__(self,codigo:int, titulo:str, tipo):
        self.__codigo=codigo
        self.__titulo=titulo
        self.__tipo=tipo
        self.__edicao=[]

    def adicionar_edicao(self,numero_da_edicao:int, data:str,numero_do_artigo:int):
        self.__edicao.append(Edicao(numero_da_edicao, data, numero_do_artigo))  

    def apresentar(self):
        print("Dados sobre a revista")
        print("Codigo: {} \n Titulo: {} \n Tipo: {} ".format(self.__codigo, self.__titulo, self.__tipo))    
        print("Sobre suas edições: ")
        c=1
        for edicao in self.__edicao:
            print(' ')
            print(" Edicao",c)
            edicao.exibir()
            c+=1

class Funcionario:
    #primeiro criei o construtor
    #depois coloquei os atributos como private usando 2 underscor
    #inicicializei o atributo horas_trabalhadas com 0;

    
    def __init__(self,horas_trabalhadas=0): #os parâmetros default devem vir por último
        self.__nome = None
        self.__cpf = None
        self.__valor_por_hora = None
        self.__horas_trabalhadas = horas_trabalhadas

    def calcular_salario(self):
        return self.__horas_trabalhadas * self.__valor_por_hora
    
    def incrementar_horas(self,horas):
        self.__horas_trabalhadas += horas
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

    @property
    def valor_por_hora(self):
        return self.__valor_por_hora

    @valor_por_hora.setter
    def valor_por_hora(self,valor_por_hora):
        if (valor_por_hora < 0):
            print("Desculpe mais não existe valor por hora negativo!")
        else:
            self.__valor_por_hora = valor_por_hora

    @property
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas
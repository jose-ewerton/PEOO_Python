class Pessoa:
    def __init__(self, nacionalidade, idade ):
        self.nacionalidade= nacionalidade
        self.idade= idade

    def Imprimir_Especs(self):
        print("Vocé tem a nacionalidade", self.nacionalidade,".")
        print("Você tem",self.idade,"anos de idade.")

    def Mudar_Nacionalidade(self):
        X= input("Qual sua nova nacionalidade?")
        self.nacionalidade=X
        print("Agora você tem a nacionalidade",X,".")

dio1=Pessoa("Espanhola",12)

dio1.Imprimir_Especs()

dio1.Mudar_Nacionalidade()

dio1.Imprimir_Especs()
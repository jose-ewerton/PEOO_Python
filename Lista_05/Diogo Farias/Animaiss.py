class Animal:
    def __init__(self, peso, altura, tipo, comendo=False):
        self.peso= peso
        self.altura= altura
        self.tipo= tipo
        self.comendo=comendo
    def Imprimir_Especs(self):
        print("O seu animal pesa:",self.peso)
        print("O seu animal mede:",self.altura)
        print("O seu animal é um",self.tipo)

    def Comer_Fruta(self,fruta):
        if self.comendo:
            print("Seu", self.tipo ,"já está comendo \o/")
        else:
            print("Seu animal está comendo", fruta)

an1=Animal (12, 23, "Macaco")

an1.Imprimir_Especs()

an1.Comer_Fruta("Maçã") #Qual fruta ele gosta?

an1.Imprimir_Especs()
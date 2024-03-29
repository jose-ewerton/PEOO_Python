class Animal:
    def __init__(self,especie,alimento,esqueleto,local):
        self.especie=especie
        self.alimento=alimento
        self.esqueleto=esqueleto
        self.local=local

    def buscar_alimento(self):
        print("O animal se encontra: Buscando alimento")

    def descansar(self):
        print("O animal se encontra: Descansando")

    def exibir_infor(self):
        print("Dados sobre o animal")
        print("Especie: {} \nClassificado de acordo com o tipo de alimento consumido: {} \nVertebrado ou Invertebrado: {} \nLocal encontrado: {}".format(self.especie,self.alimento,self.esqueleto,self.local))    

if __name__=="__main__":
    c=0
    quantidade=1
    while c==0:
        print("animal",quantidade)
        especie=input("digite o nome da especie do animal: ")
        alimento=input("digite o nome de acordo com o tipo de alimento que {} consome(carnivoro,herbivoro etc...): ".format(especie))
        esqueleto=input("Digite o nome de acordo com o corpo do animal(vertebrado ou invertebrado): ")
        local=input("digite o local onde {} se encontra(aquatico,terreste...): ".format(especie))
        animal=Animal(especie,alimento,esqueleto,local)
        descansa=input("No momento, o animal se encontra descansando(sim ou nao)? ").upper()
        if descansa=="SIM":
            animal.exibir_infor()
            animal.descansar()
        elif descansa=="NAO":
            buscar=input("No momento, o animal busca alimentos(sim ou nao)? ").upper()
            animal.exibir_infor() 
            if buscar=="SIM":
                animal.buscar_alimento()
        pergunta=input("deseja parar(sim ou nao)? ").upper()
        quantidade+=1
        if pergunta=="SIM":
            c+=1        
          

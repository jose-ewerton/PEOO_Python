class Pessoa:
    def __init__(self,nome,idade,altura,peso):
        self.nome=nome
        self.idade=idade
        self.altura=altura
        self.peso=peso

    def dormir(self):
        print("A pessoa se encontra: Dormindo")

    def acordar(self):
        print("Acordada")   

    def se_alimentar(self):
        print("Se alimentando")

    def correr(self):
        print("Correndo")        

    def exibir_informa(self):
        print("Suas informações")
        print("Nome: {} \nIdade: {} \nAltura: {} \nPeso: {}".format(self.nome,self.idade,self.altura,self.peso)) 
               
if __name__=="__main__":        
    c=0
    quantidade=1
    while c==0:
        print("oii,pessoa {}".format(quantidade))
        nome=input("digite seu nome: ")
        idade=int(input("digite sua idade: "))
        altura=float(input("digite sua altura: "))
        peso=float(input("digite seu peso: "))
        dormir=input("deseja dormir(sim ou nao)? ").upper()
        pessoa=Pessoa(nome,idade,altura,peso)
        if dormir=="SIM":
            pessoa.exibir_informa()
            pessoa.dormir()
        elif dormir=="NAO":
            alimentar=input("deseja se alimentar(sim ou nao)? ").upper()
            if alimentar=="NAO":
                correr=input("deseja correr(sim ou nao)? ").upper()
                pessoa.exibir_informa()
                print("A pessoa se encontra: ")
                pessoa.acordar()
                if correr=="SIM":
                    pessoa.correr()


            elif alimentar=="SIM":
                pessoa.exibir_informa()
                print("A pessoa se encontra: ")
                pessoa.acordar()
                pessoa.se_alimentar()
            
        pergunta=input("deseja parar(sim ou nao)? ").upper()
        quantidade+=1
        if pergunta=="SIM":
            c=1       
    
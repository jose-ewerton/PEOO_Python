class Veiculo:
    def __init__(self,tipo,marca,cor,pneus):
        self.tipo=tipo
        self.marca=marca
        self.cor=cor
        self.pneus=pneus

    def parado(self):
        print("O veiculo se encontra: Parado.")

    def movimento(self):
        print("O veiculo se encontra: Em movimento.") 

    def exibir_infor(self):
        print("Dados sobre o veiculo")
        print("Tipo: {} \nmarca: {} \ncor: {} \nQuantidade de pneus: {}".format(self.tipo,self.marca,self.cor,self.pneus))


if __name__=="__main__":
    c=0
    quantidade=1
    while c==0:
        print("Veiculo ",quantidade)
        tipo=input("digite o tipo de veiculo: ")
        marca=input("digite a marca do veiculo: ")
        cor=input("digite a cor do veiculo: ")
        pneus=int(input("Digite a quantidade de pneus do veiculo: "))
        veiculo=Veiculo(tipo,marca,cor,pneus)
        parar=input("Deseja que o veiculo fique parado(sim ou nao)? ").upper()
        veiculo.exibir_infor()
        if parar=="SIM":
            veiculo.parado()
        elif parar=="NAO":
            veiculo.movimento()
        quantidade+=1
        pergunta=input("Desejar finalizar o programa(sim ou nao)? ").upper()
        if pergunta=="SIM":
            c+=1    

altura=[]
peso=[]
sexo=[]
alf=[]
alm=[]
pm=[]
for c in range(1,16):
    print("Pessoa",c)
    altura.append(float(input("digite o valor de sua altura: ")))
    peso.append(float(input("digite o valor do seu peso: ")))
    a=input("digite seu sexo(M ou F): ").upper()
    while a!="M" and a!="F":
        a=input("digite seu sexo(M ou F): ").upper()
    sexo.append(a)
print("Media de altura do grupo: ",sum(altura)/len(altura))
nm=0
nh=0
for i in range(len(sexo)):
    if sexo[i]=="F":
        alf.append(altura[i])
        nm=nm+1
    elif sexo[i]=="M":
        alm.append(altura[i])
        pm.append(peso[i])
        nh=nh+1       
print("Mulher mais alta: ",max(alf))
print("Homem mais baixo: ",min(alm))
con=0
for b in range(len(alm)):
    if alm[b]>1.70:
        con=con+1    
print("quantidade de homens com mais de 1.70m: ",con)
print("Homem mais pesado: ",max(pm))
print("percentual de mulheres: ",(100*nm)/15,"%")
print("percentual de homens:",(100*nh)/15,"%")













        

     



    



i=[]
nota=[]
mi=[]
quan=0
quan2=0 
for c in range(1,16):
    print("Pessoa",c)
    i.append(int(input("digite sua idade: ")))   
    valor=int(input("avalie o filme escolhendo um valor a seguir(otimo-3;bom-2;regular-1): "))
    while valor!=1 and valor!=2 and valor!=3:
        valor=int(input("avalie o filme escolhendo um valor a seguir(otimo-3;bom-2;regular-1): "))
    nota.append(valor)      
for b in range(len(nota)):
    if nota[b]==3:
        mi.append(i[b])
    if nota[b]==1:
        quan=quan+1    
    if nota[b]==2:
        quan2=quan2+1       
print("media das idades que avaliaram com otimo: ",(sum(mi)/len(mi)))
print("Quantidade de pessoas que escolheram regular: ",quan)
print("Percentual da quantidade de pessoas que avaliaram com 2: ",(100*quan2)/15,"%")





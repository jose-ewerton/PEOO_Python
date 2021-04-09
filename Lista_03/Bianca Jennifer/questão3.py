P="P.M"
A="A.M"
def converter(h):
    global hfinal
    global ma
    hfinal=0
    ma=" "
    if h>12:
        hfinal=h-12
        ma=P
    elif h<12 and h>0:
        hfinal=h
        ma=A  
    else:
        if h==0:
            hfinal=12
            ma=A
        elif h==12:
            hfinal=h
            ma=P          
def final(h,m,ap):
    print("resultado ao converter: ",h,":",m,ap)
c=0
while c==0:
    hora=int(input("digite o valor da hora: "))
    minuto=int(input("digite o valor do minuto: "))
    converter(h=hora)
    final(h=hfinal,m=minuto,ap=ma)
    pergunta=(input("deseja parar(sim ou nao)? ")).upper()
    if pergunta=="SIM":
        c+=1
        print("finalizado!")

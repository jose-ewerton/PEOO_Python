valor=0
while valor==0:
    nome=input("digite seu nome: ")
    if nome=="":
        valor=valor+1
        break
    p=float(input("digite o valor da distancia do salto: "))
    s=float(input("digite o valor da distancia do salto: "))
    t=float(input("digite o valor da distancia do salto: "))
    q=float(input("digite o valor da distancia do salto: "))
    qu=float(input("digite o valor da distancia do salto: "))
    print("Atleta: ",nome)
    print("Primeiro salto: ",p,"m")
    print("Segundo salto: ",s,"m")
    print("Terceiro salto: ",t,"m")
    print("Quarto salto: ",q,"m")
    print("Quinto salto: ",qu,"m")
    print("")
    print("resultado:")
    print("Atleta: ",nome)
    print("Saltos: ",p,"-",s,"-",t,"-",q,"-",qu)
    print("media dos saltos: ",(p+s+t+q+qu)/5,"m")

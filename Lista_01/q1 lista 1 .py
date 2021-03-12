hom = []
mul = []
alth = []
altm = []
pesh = []
pesm = []

cont = 0

while cont < 15:
    genero = input("qual o seu genero: ")

    if genero == "h":

        hom.append(genero)
        print("informe sua altura em M e seu peso em Kg")
        alth.append(float(input("digite sua altura: ")))
        pesh.append(float(input("digite seu peso: ")))

        m = []
        for i in alth:
            if i >= 1.70:
                m.append(cont)


        cont += 1
    elif genero == "m":
        mul.append(genero)
        print("informe sua altura em M e seu peso em Kg")
        altm.append(float(input("digite sua altura: ")))
        pesm.append(float(input("digite seu peso: ")))

        cont += 1

S = (sum(alth) + sum(altm))/15

ph = (len(hom)/15)*100
pm = (len(mul)/15)*100

print("Media de altura do grupo = ",S,"m")
print("a mulher mais alta tem ",max(altm),"m e o homem mais baixo tem ",min(alth),"m")
print("ha ",len(m),"acima de 1,70m")
print("o homem mais pesado tem ",max(pesh),"kg")
print("a porcentagem de homens no grupo é de ",ph,"% e de mulheres é de ",pm,"%")

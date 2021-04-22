#Defina um conjunto de dados contendo a altura, peso e o sexo (M ou F) de 15 pessoas, em
# seguida calcule e informe:
# A média de altura do grupo;
# A mulher mais alta e o homem mais baixo;
# O número de homens com mais de 1,70 m de altura;
# O homem mais pesado;
# O percentual de homens e de mulheres.
m=[]
f=[]
hm=[]
hf=[]
pm=[]
pf=[]


for c in range(1, 16):
    s = (int(input("Digite '1' para Masculino, Digite '2' para Feminino: ")))

    h = float(input("Informe sua altura:"))

    p = (input("Digite seu Peso:"))


    if s == 1:
        m.append(s)
        hm.append(h)
        pm.append(p)

    elif s == 2:
        f.append(s)
        hf.append(h)
        pf.append(p)


ht= sum(hm) + sum(hf)
print(ht)

qh= len(hm) + len(hf)
print(qh)

mh= ht/qh   #Média de altura (h) do grupo
print(mh)

mhf= max(hm) #Mulher mais alta
print(mhf)

mhm= min(hm) #Homem mais baixo
print(mhm)

phm= max(pm) #Homem mais pesado
print(phm)

ph= (len(m)/0.15) #Porcentagem de homens
print(ph)

pfe= (len(f)/0.15) #Porcentagem de mulheres
print(pfe)






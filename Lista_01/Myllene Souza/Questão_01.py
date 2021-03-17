#Defina um conjunto de dados contendo a altura, peso e o sexo (M ou F) de 15 pessoas, em
#seguida calcule e informe:
# a. A média de altura do grupo;
# b. A mulher mais alta e o homem mais baixo;
# c. O número de homens com mais de 1,70 m de altura;
# d. O homem mais pesado;
# e. O percentual de homens e de mulheres.

s = 0.0
alt = 0.0
hb = 0.0
ma = 0.0
con = 0
mpe = 0.0
contm = 0
for c in range (1, 16):
    alt = float(input( "Informe sua altura:"))
    sex = input("Para informar seu sexo digite 'M' para masculino ou 'F' para feminino: ")
    peso = float(input( "Informe seu peso:")) 

    s = alt + s
# Masculino
    if sex == 'M' or sex == 'm':
        if alt<hb or hb==0.0:
            hb = alt
        if alt> 1.70:
            con = con + 1
        if peso>mpe:
            mpe=peso
# Feminino        
    elif sex == 'F' or sex == 'f':
        contm = contm + 1
        if alt>ma or ma==0.0:
            ma = alt
        
porcentualF = (contm * 100)/15
porcentualM = 100 - porcentualF

print ("A média da altura do grupo é:",s/15)
print ("O homem mais baixo tem:",hb, "de de altura.")
print ("A mulher mais alta tem:", ma,"de altura." )
print ("O números de homens com 1.70 de altura é :",con)
print ("O homem de maior peso possui:", mpe)
print ("O percetual de mulheres é:", porcentualF)
print ("O percetual de Homens é:", porcentualM)
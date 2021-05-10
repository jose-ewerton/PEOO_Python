h = [] #Homens.
m = [] #Mulheres.
alt_h = [] #Altura dos homens.
alt_m = [] #ALtura das mulheres.
peso_h = [] #Peso dos homens.
peso_m = [] #Peso das mulheres.

cont = 0

while cont < 5:
    genero = input("Qual o seu gênero (masculino ou feminino): ")

if genero == "Masculino":

h.append(genero)
print("Informe sua altura em m e seu peso em kg")
alt_h.append(float(input("Escreva sua altura: ")))
peso_h.append(float(input("Escreva seu peso: ")))

m = []
for i in alt_h:
if i >= 1.70:
m.append(cont)


cont += 1
elif genero == "Feminino":
m.append(genero)
print("informe sua altura em M e seu peso em Kg")
alt_m.append(float(input("Escreva sua altura: ")))
peso_m.append(float(input("Escreva seu peso: ")))

cont += 1

S = (sum(alt_h) + sum(alt_m))/15

ph = (len(h)/15)*100
pm = (len(m)/15)*100

print("Media de altura do grupo = ",S,"m")
print("A mulher mais alta tem ",max(alt_m),"m e o homem mais baixo tem ",min(alt_h),"m")
print("Ha ",len(m),"acima de 1,70m")
print("O homem mais pesado tem ",max(peso_h),"kg")
print("A porcentagem de homens no grupo é de ",ph,"% e de mulheres é de ",pm,"%")
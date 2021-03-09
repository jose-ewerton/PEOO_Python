print("-"*11, "Olá! Seja Bem-vindo(a) avaliação do filme","-"*11,"\nPor gentileza digite sua idade, dê um espaço e digite sua opinião\n","-"*14,"Ótimo - 3 ; Bom - 2 ; Regular - 1","-"*14)

#coletar dados
idade = []
opi = []

for a in range(15):
    x,y = input("Digite: ").split(" ")
    x = int(x)
    y = int(y)
    idade.append(x)
    opi.append(y)

#média das idades das pessoas que responderam ótimo
soma = 0
b = 0
d = 0
for c in range(len(opi)):
    if opi[b] == 3:
        soma += idade[b]
        b += 1
        d += 1
    else:
        b += 1

if d > 0:
    m = soma/d
    print("A média das idades das pessoas que responderam ótimo é {:.1f} anos".format(m))
else:
    print("Nenhuma pessoa respondeu ótimo")

#A quantidade de pessoas que responderam regular
e = 0
g = 0
for f in range(len(opi)):
    if opi[e] == 1:
        e += 1
        g += 1
    else:
        e += 1

if g == 1:
    print(f"{g} pessoa respondeu regular")
elif g > 1:
    print(f"{g} pessoas responderam regular")
else:
    print("Nenhuma pessoa respondeu regular")

#A porcentagem de pessoas que responderam bom
h = 0
j = 0
for i in range(len(opi)):
    if opi[h] == 2:
        h += 1
        j += 1
    else:
        h += 1

porc = (100*j)/len(opi)
p = "%"

if porc > 0:
    print("{:.1f}{} das pessoas responderam bom".format(porc,p))
else:
    print("Nenhuma pessoa respondeu bom")
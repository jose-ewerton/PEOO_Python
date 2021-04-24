#definir conjunto
#altura, peso e sexo de 15 pessoas
#informar média de altura do conjunto
#a mulher mais alta
#o homem mais baixo
#o número de homens com mais de 1,70
#o homem mais pesado
#o percentual de homens e de mulheres

#altura
h = 0
#mulher mais alta
a = 0
#homem mais baixo
b = 0
#homens com mais de 1,70
c = 0
#homem mais pesado
d = 0
#total de homens
t = 0
#total de mulheres
t1 = 0

for cont in range (1,16):
    print ("Informe:")
    s = input("SEXO (M para masculino e F para feminino): ").lower()
    p = int(input("PESO: "))
    al = float(input("ALTURA: "))
    h += al
    if s in 'm':
        t += 1
    else:
        t1 += 1
    if al >= 1.70 and s in 'm':
        c += 1
    if cont == 1 and s in 'm':
        b = al
        d = p
    if s in 'm' and al < b:
        b = al
    if s in 'm' and al > d:
        d = peso
    if cont == 1 and s in 'f':
        a = al
    if s in 'f' and al > a:
        a = al

media = h/15
phomem = t*100/15
pmulher = t1*100/15

print ("A média de altura do conjunto de pessoas foi de ", media)
print ("A mulher mais alta tem", a," metros de altura")
print ("O homem mais baixo tem", b," metros de altura")
print ("Há", c," homens com mais de 1.70 de altura")
print ("O homem mais pesado tem", d," kg")
print ("A porcentagem de homens é ",phomem"%")
print ("A porcentagem de mulheres é ",pmulher"&")

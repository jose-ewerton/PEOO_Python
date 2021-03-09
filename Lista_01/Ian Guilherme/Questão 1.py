a = []
p = []
s = []
zig = 1

#coletagem de dados
for zac in range(15):
    a.append(int(input("Altura {}º pessoa (cm): ".format(zig))))
    p.append(float(input("Peso {}º pessoa (kg): ".format(zig))))
    s.append(input("Sexo {}º pessoa: ".format(zig)))
    zig += 1

print("-" * 41)

#média de altura
media_a = sum(a)/len(a)
print("A média de altura é %.0f cm" % (media_a))

#mulher mais alta e o homem mais baixo
beg = 0
m = []

for big in s:
    if big == "f" or big == "F":
        m.append(a[beg])
        beg += 1
    else:
        beg += 1

m1 = max(m,key=int)
n = 0
das = 0

for dasd in m:
    if m[das] == m1:
        n = das+1
    else:
        das += 1 
        
print("A mulher mais alta é a {}º com {} cm".format(n,m1))

#homem mais baixo
teg = 0
h = []

for tig in s:
    if tig == "m" or tig == "M":
        h.append(a[teg])
        teg += 1
    else:
        teg += 1

h1 = min(h,key=int)
j = 0
tas = 0

for tasd in h:
    if h[tas] == h1:
        j = tas+1
    else:
        tas += 1 
        
print("O homem mais baixo é o {}º com {} cm".format(j,h1))

#número de homens com mais de 170 cm de altura
zic = zoc = 0 
zub = 0

for zec in s:
    if zec == "m" or zec == "M":
        if a[zoc] > 170:
            zic += 1
            zoc += 1
        else:
            zub = 1
            zoc += 1
    else:
        zoc += 1

if zic > 1:
    print("{} homens com altura maior que 170cm".format(zic))
elif zic == 1:
    print("Apenas 1 homem com altura maior que 170cm")
elif zic == 0 and zub == 1:
    print("Nenhum homem é maior que 170cm")
else:
    print("Não tem homens")

#o homem mais pesado
fleg = 0
hp = []

for vig in s:
    if vig == "m" or vig == "M":
        hp.append(p[fleg])
        fleg += 1
    else:
        fleg += 1

hp1 = max(hp,key=int)
r = 0
vas = 0

for asd in hp:
    if hp[vas] == hp1:
        r = vas+1
    else:
        vas += 1 
        
print("O homem mais pesado é o {}º com {}kg".format(r,hp1))

#o percentual de homens e mulheres
toma = 0
pm = []

for nada in s:
    if nada == "m" or nada == "M":
        pm.append(1)
        toma += 1
    else:
        toma += 1

pms = (sum(pm)*100)/len(s)
porcen = "%"

print("O percentual de homens é de {:.1f}{}".format(pms, porcen))

receba = 0
pf = []

for nada1 in s:
    if nada1 == "f" or nada1 == "F":
        pf.append(1)
        receba += 1
    else:
        receba += 1

pfs = (sum(pf)*100)/len(s)
porcen = "%"

print("O percentual de mulheres é de {:.1f}{}".format(pfs, porcen))
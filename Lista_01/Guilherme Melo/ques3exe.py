r = []
i = []
c = 0
bom = 0
regular = 0
otimo = 0
while c < 15:
    print("")
    print("Determine sua opinião do filme com um número abaixo!")
    print("1 - regular\n2 - bom\n3 - ótimo")
    resp = int(input("Classifique: "))
    idade = int(input("Digite sua idade: "))
    i.append(idade)
    if resp == 1:
        regular += 1
    elif resp == 2:
        bom += 1
    elif resp  == 3:
        otimo += 1
    c += 1
mida = sum(i)/15
print("A média das idades são %d." %mida)
print("{} responderam regular." .format(regular))
porc = (100/15) * bom
#print("{:2.f}% responderam bom. " .format(porc))
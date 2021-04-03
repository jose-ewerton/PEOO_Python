#RECEBENDO AS RESPOSTAS
print ("RESPONDA COM 'sim' ou 'não'")
print("DO MESMO JEITO, POR FAVOR!")
r1 = str(input("Telefonou para a vitima? "))
r2 = str(input("Esteve no local do crime? "))
r3 = str(input("Mora perto da vitima? "))
r4 = str(input("Devia para a vitima? "))
r5 = str(input("Ja trabalhou com a vitima? "))

#VERIFICAÇÃO
lolo = 0
if r1 == "não":
    lolo = 0
elif r1 == "sim":
    lolo += 1


if r2 == "não":
    lolo = 0
elif r2 == "sim":
    lolo += 1


if r3 == "não":
    lolo = 0
elif r3 == "sim":
    lolo += 1


if r4 == "não":
    lolo = 0
elif r4 == "sim":
    lolo += 1


if r5 == "não":
    lolo = 0
elif r5 == "sim":
    lolo += 1

#CLASSIFICAÇÃO
if lolo == 0:
    lolo = "inocente"
if lolo == 1:
    lolo = "inocente"
if lolo == 2:
    lolo = "suspeito"
if lolo == 3:
    lolo = "cumplice"
if lolo == 4:
    lolo = "cumplice"
if lolo == 5:
    lolo = "assassino"
print("o interrogado é temporariamente {}." .format(lolo))
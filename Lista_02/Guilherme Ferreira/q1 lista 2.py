print ("RESPONDA APENAS COM SIM E NAO")
r1 = str(input("Telefonou para a vitima? "))
r2 = str(input("Esteve no local do crime? "))
r3 = str(input("Mora perto da vitima? "))
r4 = str(input("Devia para a vitima? "))
r5 = str(input("Ja trabalhou com a vitima? "))
respostas = ["Telefonou para a vitima?", r1
             , "Esteve no local do crime?", r2
             , "Mora perto da vitima?", r3
             , "Devia para a vitima?", r4
             , "Ja trabalhou com a vitima?", r5]
veredito = 0
if r1 == "nao":
    veredito = veredito
elif r1 == "sim":
    veredito = veredito + 1
if r2 == "nao":
    veredito = veredito
elif r2 == "sim":
    veredito = veredito + 1
if r3 == "nao":
    veredito = veredito
elif r3 == "sim":
    veredito = veredito + 1
if r4 == "nao":
    veredito = veredito
elif r4 == "sim":
    veredito = veredito + 1
if r5 == "nao":
    veredito = veredito
elif r5 == "sim":
    veredito = veredito + 1
if veredito == 0:
    veredito = "inocente"
if veredito == 1:
    veredito = "inocente"
if veredito == 2:
    veredito = "suspeito"
if veredito == 3:
    veredito = "cumplice"
if veredito == 4:
    veredito = "cumplice"
if veredito == 5:
    veredito = "assassino"
print("o interrogado é: %s"%veredito)
print("respostas dadas pelo interrogado: %s"%respostas)

print ("RESPONDA APENAS COM SIM E NAO")
res1 = str(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
res2 = str(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
res3 = str(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
res4 = str(input("Devia para a vítima? 1/Sim ou 0/Não: "))
res5 = str(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))
soma_respostas = res1 + res2 + res3 + res4 + res5


veredito = 0
if res1 == "nao":
    veredito = veredito
elif res1 == "sim":
    veredito = veredito + 1
if res2 == "nao":
    veredito = veredito
elif res2 == "sim":
    veredito = veredito + 1
if res3 == "nao":
    veredito = veredito
elif res3 == "sim":
    veredito = veredito + 1
if res4 == "nao":
    veredito = veredito
elif res4 == "sim":
    veredito = veredito + 1
if res5 == "nao":
    veredito = veredito
elif res5 == "sim":
    veredito = veredito + 1
if (soma_respostas == 0):
    veredito == "Inocente"
if (soma_respostas == 1):
    veredito == "Inocente"
if (soma_respostas == 2):
    veredito == "Suspeito"
if (soma_respostas == 3):
    veredito == "Cúmplice"
if (soma_respostas == 4):
    veredito == "Cúmplice"
if (soma_respostas == 5):
    veredito == "Assassino"
print("o interrogado é: %s"%veredito)
print("respostas dadas pelo interrogado: %s"%res1, res2, res3, res4, res5)
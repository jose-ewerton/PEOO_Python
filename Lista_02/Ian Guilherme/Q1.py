perg = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou para a vítima?"]
resp = []

print("-Bem vindo ao interrogatório!-\n*Responda somente com S ou N!*\n{}".format("-"*30))

tig = 0

for i in range(5):
    resp.append(input("{}: ".format(perg[tig])))
    tig += 1

cont = 0
tag = 0

for j in resp:
    if resp[tag] == "S":
        cont += 1
        tag += 1
    else:
        tag += 1
    
if cont == 5:
    print("Classificado como ASSASSINO")
elif 2 < cont < 5:
    print("Classificado como CÚMPLICE")
elif cont == 2:
    print("Classificado como SUSPEITO")
else:
    print("Classificado como INOCENTE")
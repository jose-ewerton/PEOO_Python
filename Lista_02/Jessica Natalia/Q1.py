perg = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para vítima?","Já trabalhou com a vítima?"]
resp = []

resp.append(input("{} ".format(perg[0])))
resp.append(input("{} ".format(perg[1])))
resp.append(input("{} ".format(perg[2])))
resp.append(input("{} ".format(perg[3])))
resp.append(input("{} ".format(perg[4])))

verdades = 0

if resp[0] == "Sim":
    verdades += 1
if resp[1] == "Sim":
    verdades += 1
if resp[2] == "Sim":
    verdades += 1
if resp[3] == "Sim":
    verdades += 1
if resp[4] == "Sim":
    verdades += 1

if verdades == 5:
    print("Você é assasino")
elif 2 < verdades < 5:
    print("Você é cúmplice")
elif verdades == 2:
    print("Você é suspeito(a)")
else:
    print("Você é inocente")

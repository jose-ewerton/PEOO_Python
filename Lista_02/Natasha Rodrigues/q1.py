print("-"*35)
print("Responda apenas com 'sim' ou 'não'.")
print("-"*35)

perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para vítima?","Já trabalhou com a vítima?"]
respostas = []

respostas.append(input("{} ".format(perguntas[0])))
respostas.append(input("{} ".format(perguntas[1])))
respostas.append(input("{} ".format(perguntas[2])))
respostas.append(input("{} ".format(perguntas[3])))
respostas.append(input("{} ".format(perguntas[4])))

resp_verd = 0

if respostas[0] == "sim":
    resp_verd += 1
if respostas[1] == "sim":
    resp_verd += 1
if respostas[2] == "sim":
    resp_verd += 1
if respostas[3] == "sim":
    resp_verd += 1
if respostas[4] == "sim":
    resp_verd += 1

if resp_verd == 5:
    print("Você é considerado assasino")
elif 2 < resp_verd < 5:
    print("Você é considerado cúmplice")
elif resp_verd == 2:
    print("Você é considerado suspeito(a)")
else:
    print("Você é considerado inocente")
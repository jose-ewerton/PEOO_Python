print("Olá! Você foi intimado(a) para responder algumas pergutinhas! :)")
print("Digite 1 para responder 'não'"
      " \nDigite 2 para responder 'sim'")

res = []
res.append(input("Telefonou para a vítima?"))
res.append(input("Esteve no local do crime?"))
res.append(input("Mora perto da vítima?"))
res.append(input("Devia para a vítima?"))
res.append(input("Já trabalhou com a vítima?"))

soma_respostas = 0

for i in res:
    soma_respostas = soma_respostas + int(i)

if (soma_respostas < 2):
 print("Esta pessoa é inocente. Podem liberar")
elif (soma_respostas == 2):
 print("Você é Suspeita!")
elif (3 <= soma_respostas <= 4):
 print("Você é Cúmplice!")
elif (soma_respostas == 5):
 print("Assassino!")
else:
    print("Esta pessoa é inocente. Podem liberar")

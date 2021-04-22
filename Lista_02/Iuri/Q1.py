count = 0

resp = str(input("Telefonou para a vítima? "))
resp = resp.lower()
if resp == "Sim" or resp == "s":
  count += 1

resp = str(input("Esteve no local do crime? "))
resp = resp.lower()
if resp == "Sim" or resp == "s":
  count += 1

resp = str(input("Mora próxomo a vítima? "))
resp = resp.lower()
if resp == "Sim" or resp == "s":
  count += 1

resp = str(input("Devia para a vítima? "))
resp = resp.lower()
if resp == "Sim" or resp == "s":
  count += 1

resp = str(input("Já trabalhou com a vítima? "))
resp = resp.lower()
if resp == "Sim" or resp == "s":
  count += 1

if count == 2:
  print ("Você é uma pessoa suspeita, por enquanto estaremos te vigiando.")
elif count == 3 or count == 4:
  print ("Você é cúmplice desse assassinato, o segurem.")
elif count == 5:
  print("Ele é o assassino, algemem-o agora!")
else:
  print("Libertem, é inocente.")
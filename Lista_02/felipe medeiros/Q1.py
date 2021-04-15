''' "1. Utilizando listas crie um programa que faça 5 perguntas para uma pessoa sobre um crime.
 As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre 
a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões 
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como 
"Assassino". Caso contrário, ele será classificado como "Inocente". '''

print("Responda usando apenas S para sim e N para não.")

x1 = str(input("telefonou para vitima?: "))

x2 = str(input("esteve no local do crime?: "))

x3 = str(input("mora perto da vitima?: "))

x4 = str(input("devia para a vitima?: "))

x5 = str(input("trabalhou com a vitima?: "))

total=[]

if x1 == "S":
	total += [1]
if x2 == "S":
	total += [1]
if x3 == "S":
	total += [1]
if x4 == "S":
	total += [1]
if x5 == "S":
	total += [1]
total = len(total)

if total < 2:
	a = ("Inocente")
elif total == 2:
	a = ("suspeito")
elif 2 > total or total <= 4:
	a = ("cumplice")
elif total > 4:
	a = ("culpado")

print("você é", a, "e tem", total, "provas contra você.")

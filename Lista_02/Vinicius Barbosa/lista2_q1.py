'''Utilizando listas crie um programa que faça 5 perguntas para uma pessoa sobre um crime. As
perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre
a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente".'''



print("Responda usando apenas S para sim e N para não.")

a1 = str(input("telefonou pra vitima?:"))

a2 = str(input("esteve no local do crime?:"))

a3 = str(input("mora perto da vitima?:"))

a4 = str(input("devia para a vitima?:"))

a5 = str(input("rabalhou com a vitima?: "))

R=[]

if a1 == "S":
	R += [1]
if a2 == "S":
	R += [1]
if a3 == "S":
	R += [1]
if a4 == "S":
	R += [1]
if a5 == "S":
	R += [1]
r = len(R)

if r < 2:
	z = ("Inocente")
elif r == 2:
	z = ("suspeito")
elif 2 > r or r <= 4:
	z = ("cumplice")
elif r > 4:
	z = ("culpado")

print(f'você é "{z.upper()}" e tem "{r}" provas contra você.')

print('')
print('====================================================')
print('')
print('By: Vinicius Barbosa')
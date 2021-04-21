"""Utilizando listas crie um programa que faça 5 perguntas para uma pessoa sobre um crime. As
perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre
a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente"."""


#Responda apenas com Sim ou Não!

p1 = str(input("Voce telefonou pra vitima? ")) #Pergunta a.
p2 = str(input("Voce esteve no local do crime? ")) # Pergunta b.
p3 = str(input("Voce mora perto da vitima? ")) #Pergunta c.
p4 = str(input("Voce devia para a vitima? ")) #Pergunta d.
p5 = str(input("Vc trabalhou com a vitima? ")) #Pergunta e.

R=[]

if p1 == "Sim":
	R += [1]
if p2 == "Sim":
	R += [1]
if p3 == "Sim":
	R += [1]
if p4 == "Sim":
	R += [1]
if p5 == "Sim":
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

print("Você é", z, "e tem", r, "provas contra você.")

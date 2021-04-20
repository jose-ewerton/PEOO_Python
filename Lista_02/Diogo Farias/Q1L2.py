#Utilizando listas crie um programa que faça 5 perguntas para uma pessoa sobre um crime. As
#perguntas são:
#a. "Telefonou para a vítima?"
#b. "Esteve no local do crime?"
#c. "Mora perto da vítima?"
#d. "Devia para a vítima?"
#e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre
#a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões
#ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
#"Assassino". Caso contrário, ele será classificado como "Inocente".

#RESPONDA COM: 15 = NÃO / 25 = SIM
A= (int(input("Telefonou para a vítima?")))
B=(int(input("Esteve no local do crime?")))
C=(int(input("Mora perto da vítima?")))
D= (int(input("Devia para a vítima?")))
E= (int(input("Já trabalhou com a vítima?")))

Sentenca= []
if A == 25:
    Sentenca += ["A"]
if B == 25:
    Sentenca += ["B"]
if C == 25:
    Sentenca += ["C"]
if D == 25:
    Sentenca += ["D"]
if E == 25:
    Sentenca += ["E"]

X = len(Sentenca)

if X < 2:
    print("VOCÊ É INOCENTE")
elif X == 2:
    print("VOCÊ É SUSPEITO")
elif X >= 2 and X <= 4:
    print("VOCÊ É CÚMPLICE")
elif X == 5:
    print("VOCÊ É CULPADO")

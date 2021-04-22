"""Utilizando listas crie um programa que faça 5 perguntas para uma pessoa sobre um crime. As
perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre
a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente"."""

lista = []
print("-"*33)
print("QUESTIONÁRIO SOBRE O ASSASSINATO")
print("-"*33)

a = str(input("Telefonou para a vítima? (Sim ou Não): ")).upper()
if 'S' in a:
    lista.append(a)
b = str(input("Esteve no local do crime? (Sim ou Não): ")).upper()
if 'S' in b:
    lista.append(b)
c = str(input("Mora perto da vítima? (Sim ou Não): ")).upper()
if 'S' in c:
    lista.append(c)
d = str(input("Devia para a vítima? (Sim ou Não): ")).upper()
if 'S' in d:
    lista.append(d)
e = str(input("Já trabalhou com a vítima? (Sim ou Não): ")).upper()
if 'S' in e:
    lista.append(e)

if len(lista) == 2:
    print("Resultado:\033[34m Suspeito(a)"'\033[m')

elif len(lista) == 3:
    print("Resultado:\033[33m Cúmplice"'\033[m')

elif len(lista) == 4:
    print("Resultado:\033[33m Cúmplice"'\033[m')

elif len(lista) == 5:
    print("Resultado:\033[31m Assassino!"'\033[m')

else:
    print("Resultado:\033[32m Inocente!"'\033[m')
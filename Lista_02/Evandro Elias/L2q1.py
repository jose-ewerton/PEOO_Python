print("------------------------------------------------------------------------------------------------")
print(" 0 = não --- 1 = sim")
Q1 = int(input("Telefonou pra vitima?:  "))
Q2 = int(input("Esteve no local do crime?: "))
Q3 = int(input("Mora perto da vitima?:  "))
Q4 = int(input("Devia para a vitima?:  "))
Q5 = int(input("Já trabalhou com a vitima?:  "))
lista = []
if Q1 == 1:
    lista += ['a']
if Q2 == 1:
    lista += ['b']
if Q3 == 1:
    lista += ['c']
if Q4 == 1:
    lista += ['d']
if Q5 == 1:
    lista += ['e']
Y = len(lista)
print("existem {} evidências contra você, Você é".format(Y))
if Y < 2:
    print("Inocente")
elif Y == 2:
    print("Suspeito")
elif Y >= 2 and Y <= 4:
    print("Cumplice")
elif Y == 5:
    print(" Assasino")

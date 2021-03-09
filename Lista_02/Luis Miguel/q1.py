#responda as perguntas como 0 = não e 1 = sim
p1 = int(input("telefonou pra vitima?:  "))
p2 = int(input("esteve no local do crime?: "))
p3 = int(input("mora perto da vitima?:  "))
p4 = int(input("devia para a vitima?:  "))
p5 = int(input("ja trabalhou com a vitima?:  "))
lista = []
if p1 == 1:
    lista += ['a']
if p2 == 1:
    lista += ['b']
if p3 == 1:
    lista += ['c']
if p4 == 1:
    lista += ['d']
if p5 == 1:
    lista += ['e']
ev = len(lista)
print(f"existem {ev} evidências contra vc")
if ev < 2:
    print("vc eh inocente")
elif ev == 2:
    print("vc eh suspeito")
elif 2 > ev < 4:
    print("vc eh cúmplice")
elif ev == 5:
    print(" vc eh culpado")
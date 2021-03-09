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

print("você é", z, "e tem", r, "provas contra você.")
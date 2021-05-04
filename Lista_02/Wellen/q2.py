s = []
a = str(input("Nome do atleta:"))
for d in range(1, 6):
    salto = float(input("{}º Salto:".format(d)))
    s.append(salto)
print("Atleta: {}\n1 salto: {}\n2 salto: {}\n3 salto: {}\n4 salto: {}\n5 salto: {}".format(a, s[0], s[1], s[2], s[3], s[4]))
m = sum(s)/5
print("Resultado:")
print("Atleta: {}".format(a))
print("Saltos: {}".format(s))
print("Média: {}".format(m))
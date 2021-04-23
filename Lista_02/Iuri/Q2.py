z = 0
n = list()

atleta = input("Digite seu nome: ")
for c in range(1, 5):
  n.append(int(input("{}° salto: ".format(c))))
  z += 1
m = sum(n) / len(n)

# print ("Resultado:")
# print ("Saltos: {}".format(n))
print ("Média: {}".format(m))

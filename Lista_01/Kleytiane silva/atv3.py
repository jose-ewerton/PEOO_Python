print("Por favor, nós informe uma nota sobre o filme: ")
print("Digite 1 para regular, digite 2 para bom e digite 3 para ótimo.")
reg = 0
bo = 0
ot = 0
idade = list()
for c in range(1, 16):
 idade.append(int(input("{}° candidato, digite sua idade: ".format(c))))
 c = int(input("Digite um número conforme sua opinião: "))
 if c == 3:
   ot += c
 elif c == 2:
   bo += 1
 else:
   reg += 1

me = sum(idade)/len(idade)
por = (100 * bo)/15

print("A média de idade: {}".format(me))
print("A quantidade de respostas regulares: {}".format(reg))
print("A porcentagem de respostas de n°2: {}%".format(por))

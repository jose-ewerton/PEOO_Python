'''Faça um programa que receba a idade e a opinião de 15 espectadores de um cinema em relaçãoa um determinado filme, sendo ótimo - 3, bom - 2, regular -1, em seguida calcule e informe:
a. A média das idades das pessoas que responderam ótimo;
b. A quantidade de pessoas que responderam regular;
c. A porcentagem de pessoas que responderam bom entre todos os espectadoresanalisados.''' 

idade = []
opniao = []
i= 0 
while i < 15:
	print("Para sua opinião use 3 para ótimo, 2 para bom e 1 para regular.")
	idade.append(int(input("Diga sua idade:")))
	nota.append(int(input("Diga sua opinião:")))
	i += 1
total = sum(idade)
print("A média da idade das pessoas foi de", total/len(idade))

N = []
pe = []
for cont in nota:
 		if ((cont % 2 != 0) and (cont == 1)):
 				N.append(cont)
 		if (cont % 2 == 0):
 			pe.append(cont)
 
print(list(idade))
print(list(nota))

P = (len(pe)/15)*100
print("O numero de pessoas que responderam regular foi", len(N))
print(round(P),"% que votaram bom.")
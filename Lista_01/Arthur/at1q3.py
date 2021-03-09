'''Faça um programa que receba a idade e a opinião de 15 espectadores de um cinema em relação
a um determinado filme, sendo ótimo - 3, bom - 2, regular -1, em seguida calcule e informe:
a. A média das idades das pessoas que responderam ótimo;
b. A quantidade de pessoas que responderam regular;
c. A porcentagem de pessoas que responderam bom entre todos os espectadores
analisados.'''

id = []
nota = []
i= 0

while i < 15:
	print("Para sua opinião use 3 para ótimo, 2 para bom e 1 para regular.")
	id.append(int(input("Diga sua idade:")))
	nota.append(int(input("Diga sua opinião:")))
	i += 1	

total = sum(id)

print("A média da idade dos participantes foi de", total/len(id))

N = []
p = []
for cont in nota:	
	if ((cont % 2 != 0) and (cont == 1)):
		N.append(cont)
	if (cont % 2 == 0):
    		p.append(cont)	

print(list(id))
print(list(nota))
    	
P = (len(p)/15)*100		
print("O numero de pessoas que responderam regular foi", len(N))	
print(round(P),"% que votaram bom.")
	
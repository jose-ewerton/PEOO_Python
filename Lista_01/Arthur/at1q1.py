'''
Defina um conjunto de dados contendo a altura, peso e o sexo (M ou F) de 15 pessoas, em
seguida calcule e informe:
a. A média de altura do grupo;
b. A mulher mais alta e o homem mais baixo;
c. O número de homens com mais de 1,70 m de altura;
d. O homem mais pesado;
e. O percentual de homens e de mulheres'''

M = []  #Homens
F = []  #Mulheres
alm = [] #Altura dos homens
alf = []  #Altura das mulheres
pem = []  #Peso dos homens
pef = []  #Peso das mulheres

i = 0

while i < 2:
	print("Use M para masculino e F para feminino")
	genero = input("Qual seu gênero:")
	
	if ((genero == "M") or (genero == "m")):
		
		M.append(genero)
		for item in M:
    			print ("Aqui")
    			print(item)
		print("Digite sua altura em m e seu em Kg")
		alm.append(float(input("Qual a sua altura:")))
		pem.append(float(input("Qual seu peso:")))
		
		m = []
		for cont in alm:
			if cont >= 1.70:
				m.append(cont)
		
		i += 1
		
	elif ((genero == "F") or (genero == "f")):
		F.append(genero)
		for item in F:
    			print(item)
						    			
		print("Digite sua altura em m e seu em Kg")
		alf.append(float(input("Qual a sua altura:")))
		pef.append(float(input("Qual seu peso:")))
		i +=1


S = (sum(alm) + sum(alf))/ (len(M)+len(F))

pm = round((len(M)/15)*100)
pf = round((len(F)/15)*100)

print("A média da altura do grupo foi",S, "m")
print("A mulher do grupo mais alta tem a altura de",max(alf),"M e o homem mais baixo do grupo tem",min(alm),"M")
print("O número de homens que tem altura acima de 1,70 são",len(m))
print("O homem mais pesado do grupo tem",max(pem),"kg")
print("O percentual de homens no grupo é de",pm,"% e de mulheres é de",pf,"%")
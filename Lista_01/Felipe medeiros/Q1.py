'''Defina um conjunto de dados contendo a altura, peso e o sexo (M ou F) de 15 pessoas, emseguida calcule e informe:a. A média de altura do grupo;b. A mulher mais alta e o homem mais baixo;c. O número de homens com mais de 1,70 m de altura;d. O homem mais pesado;e. O percentual de homens e de mulheres'''
H = []
M = [] 
alh = [] 
alm = [] 
pdh = []
pdm = [] 
i = 0 
while i < 2:
   	print("Use H para Homens e M para mulheres: ")
   	genero = input("Qual seu gênero: ")
   	if(genero == "H"):
   		M.append(genero)
   		for item in H:
   			print ("Aqui")
   			print(item)
   		print("Digite sua altura em metros e seu peso em Kg")
   		alh.append(float(input("Qual é a sua altura: ")))
   		pdh.append(float(input("Qual é seu peso: ")))
   		
   		m = []
   		for cont in alh:
   				if cont >= 1.70:
   					m.append(cont)
   				
   		i += 1
   	elif (genero == "M" ):
   			M.append(genero)
   			for item in M:
   				print(item)
   				print("Digite sua altura em m e seu em Kg")
   				alm.append(float(input("Qual é a sua altura: ")))
   				pdm.append(float(input("Qual é seu peso: ")))
   				i +=1 
S = (sum(alh) + sum(alm))/ (len(H)+len(M))
ph= round((len(M)/15)*100)
pm = round((len(F)/15)*100)

print("A média da altura do grupo foi",S, "m")
print("A mulher mais alta tem a altura de",max(alm),"M e o homem mais baixo do grupo tem",min(alh),"M")
print("O número de homens que tem altura acima de 1,70 são",len(m))
print("O homem mais pesado do grupo tem",max(pdh),"kg")
print("O percentual de homens no grupo é de",ph,"% e de mulheres é de",pm,"%")

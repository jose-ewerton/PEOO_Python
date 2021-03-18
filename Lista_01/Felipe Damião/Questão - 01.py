mulheres = []  
homens = []  
alturasdoshomens = [] 
alturasdasmulheres = []  
pesosdoshomens = []  
pesosdasmulheres = []  

numerovariavel = 0

while numerovariavel < 15:
	print("Use M para masculino e F para feminino")
	genero = input("Qual seu gênero:")
	
	if ((genero == "M") or (genero == "m")):
		
		homens.append(genero)
		for qualquercoisa in homens:
    			print(qualquercoisa)
		print("Digite a sua altura em metros(m) e seu em quilogramas(Kg)")
		alturasdoshomens.append(float(input("Qual a sua altura:")))
		pesosdoshomens.append(float(input("Qual seu peso:")))
		
		homem = []
		for contagem in alturasdoshomens:
			if contagem >= 1.70:
				homem.append(contagem)
		
		numerovariavel += 1
		
	elif ((genero == "F") or (genero == "f")):
		mulheres.append(genero)
		for qualquerrcoisa in mulheres:
    			print(qualquerrcoisa)
						    			
		print("Digite a sua altura em metros(m) e seu em quilogramas(Kg)")
		alturasdasmulheres.append(float(input("Qual a sua altura:")))
		pesosdasmulheres.append(float(input("Qual seu peso:")))
		numerovariavel +=1


soma = (sum(alturasdasmulheres) + sum(alturasdoshomens))/ (len(homens)+len(mulheres))

pesosdoshomensfinal = round((len(pesosdoshomens)/15)*100)
pesosdasmulheresfinal = round((len(pesosdasmulheres)/15)*100)

print("A média da altura do grupo foi",soma, "m")
print("A mulher do grupo mais alta tem a altura de",max(alturasdasmulheres),"M e o homem mais baixo do grupo tem",min(alturasdoshomens),"M")
print("O número de homens que tem altura acima de 1,70 são",len(homem))
print("O homem mais pesado do grupo tem",max(pesosdoshomens),"kg")
print("O percentual de homens no grupo é de",pesosdoshomensfinal,"% e de mulheres é de",pesosdasmulheresfinal,"%")

numerosprimos=[]
numerosimpares = []
numeroqualquer2 = 0
contaprimos = 0
numerosvariaveis = 0
variavelqualquer = 0

while variavelqualquer < 10:
	numerosprimos.append(int(input('Digite qualquer número: ')))
	variavelqualquer += 1
	
	for listadenumeros in numerosprimos:
		if listadenumeros % 2 != 0:
			numerosimpares.append(listadenumeros)	

for primos in range(10):
	for numeroqualquer in range(1, numerosprimos[numeroqualquer2] + 1):
		if numerosprimos[numeroqualquer2] % numeroqualquer == 0:
			numerosvariaveis += 1
	if numerosvariaveis == 2:
		contaprimos += numerosprimos[numeroqualquer2]
	numeroqualquer2 += 1
	numerosvariaveis = 0 

somadosimpares = sum(set(numerosimpares))

print("A soma dos números impares é", somadosimpares)

print("A soma dos números primos é",contaprimos)

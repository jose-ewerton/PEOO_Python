'''Faça um programa que receba 10 números, calcule e imprima a soma dos números ímpares e
a soma dos números primos.'''
numero=[]
imp = []
x = 0
y = 0
mult = 0
i = 0

while i < 10:
	numero.append(int(input("Digite um numero: ")))
	i += 1
	
	for cont in numero:
		if cont % 2 != 0:
			imp.append(cont)	

for a in range(10):
	for b in range(1, numero[x] + 1):
		if numero[x] % b == 0:
			mult += 1
	if mult == 2:
		y += numero[x]
	x += 1
	mult = 0 

Impares = sum(set(imp))

print("A soma dos números impares são de", Impares)

print("A soma dos números primos são de",y)
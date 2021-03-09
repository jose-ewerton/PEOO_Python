'''Faça um programa que receba 10 números, calcule e imprima a soma dos números ímpares e
a soma dos números primos.
'''
num=[]
impar = []
x = 0
s = 0
mult = 0
i = 0

while i < 10:
	num.append(int(input("Digite um numero:")))
	i += 1
	
	for cont in num:
		if cont % 2 != 0:
			impar.append(cont)	

for a in range(10):
	for b in range(1, num[x] + 1):
		if num[x] % b == 0:
			mult += 1
	if mult == 2:
		s += num[x]
	x += 1
	mult = 0 

Impares = sum(set(impar))

print("A soma dos números impares são de", Impares)

print("A soma dos números primos são de",s)
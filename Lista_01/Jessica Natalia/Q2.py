#Faça um programa que receba 10 números, calcule e imprima a soma dos números ímpares e
#a soma dos números primos
# Quando não souber o que fazer use a lógica

#Recebi valores
num = []

for ahhh in range(10):
    num.append(int(input('Adicione um número: ')))

#saber quem são os ímpares e somar
oi = 0
imp = 0
for bhhh in range(10):
    if num[oi] % 2 > 0:
        imp += num[oi] 
        oi += 1
    else:
        oi += 1
print ("A soma dos números ímpares é {}".format(imp)) 

#Números primos
oe = 0
somap = 0
tat = 0

for chhh in range(10):
    for c in range(1, num[oe]+1):
        if num[oe] % c == 0:
            tat += 1
    if tat == 2:
        somap += num[oe]
    oe += 1
    tat = 0

print ('A soma dos números primos é {}'.format(somap))
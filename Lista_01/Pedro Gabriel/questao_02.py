"""Faça um programa que receba 10 números, calcule e imprima a soma dos números ímpares e
a soma dos números primos."""


n = [] #Números.
imp = [] #Ímpares.
p = 0
g = 0
mult = 0
i = 0

while i < 10:
    n.append(int(input("Digite um numero: ")))
    i += 1

    for cont in n:
        if cont % 2 != 0:
            imp.append(cont)

for a in range(10):
    for b in range(1, n[p] + 1):
        if n[p] % b == 0:
            mult += 1
    if mult == 2:
        g += n[p]
    p += 1
    mult = 0

Impares = sum(set(imp))

print("A soma dos numeros impares sao de:", Impares)

print("A soma dos numeros primos sao de:", g)



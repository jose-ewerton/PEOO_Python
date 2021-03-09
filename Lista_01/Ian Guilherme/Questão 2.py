n = []

for a in range(10):
    n.append(int(input("Digite um número: ")))

#numeros impares
impares = []

for b in n:
    if b % 2 != 0:
        impares.append(b)

print(f"A soma dos números impares é {sum(impares)}")

#numeros primos
primos = 0
c = 1
indice = 0
conta = 0

while c < 10:
    for d in range(1, n[indice]+1):
        if n[indice] % d == 0:
            conta += 1
    if conta == 2:
        primos += n[indice]
    c += 1
    indice += 1
    conta = 0

print(f"A soma dos números primos é {primos}")